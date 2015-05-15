register s3n://uw-cse-344-oregon.aws.amazon.com/myudfs.jar

-- load the test file into Pig
-- raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/cse344-test-file' USING TextLoader as (line:chararray);
-- later you will load to other files, example:
raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/btc-2010-chunk-000' USING TextLoader as (line:chararray); 

-- parse each line into ntriples
ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);

--group the n-triples by object column
subjects = group ntriples by (subject) PARALLEL 50;

-- flatten the objects out (because group by produces a tuple of each object
-- in the first column, and we want each object ot be a string, not a tuple),
-- and count the number of tuples associated with each object
count_by_subject = foreach subjects generate flatten($0), COUNT($1) as count PARALLEL 50;

-- count_by_subject is of the form (subject, number of subjects)
--  now we have to group by counts
count_groups = group count_by_subject by (count) PARALLEL 50;

histogram = foreach count_groups GENERATE flatten($0) as counts, COUNT($1) as no_of_subjects PARALLEL 50;





-- store the results in the folder /user/hadoop/2a_histogram
store histogram into '/user/hadoop/2b2_histogram' using PigStorage();
-- Alternatively, you can store the results in S3, see instructions:
-- store count_by_object_ordered into 's3n://superman/example-results';

-- this is to transfer the output file which is stores in the hdfs onto our aws master node. 
fs -getmerge /user/hadoop/2b2_histogram 2b2_histogram
-- this is to copy it to our local machine
scp -o "ServerAliveInterval 10" -i kp.pem -r hadoop@<master.public-dns-name.amazonaws.com>:2b2_histogram .
