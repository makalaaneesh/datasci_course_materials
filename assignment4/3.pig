register s3n://uw-cse-344-oregon.aws.amazon.com/myudfs.jar

-- load the test file into Pig
-- raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/cse344-test-file' USING TextLoader as (line:chararray);
-- later you will load to other files, example:
raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/btc-2010-chunk-000' USING TextLoader as (line:chararray); 


-- parse each line into ntriples
ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);

copy1= FILTER ntriples by (subject matches '.*rdfabout\\.com.*') PARALLEL 50;

-- creating a copy in order to join
copy2 = FOREACH copy1 GENERATE subject as subject2, predicate as predicate2, object as object2 PARALLEL 50;
-- join operation
joined = JOIN copy1 by object, copy2 by subject2 PARALLEL 50;
-- removing duplicates
joined_distinct = DISTINCT joined;
-- storing in the debug mode
-- store joined_distinct into '/tmp/finaloutput' using PigStorage();
store joined_distinct into '/user/hadoop/3b' using PigStorage();
-- merging the output(which is divided into many parts into one file and storing it onto the aws master node)
fs -getmerge /user/hadoop/3b 3b
-- copyting the file onto your local machine
scp -o "ServerAliveInterval 10" -i kp.pem -r hadoop@<master.public-dns-name.amazonaws.com>:3b .
