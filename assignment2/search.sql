create view frequency_search as 
select * from frequency
union
select 'q' as docid, 'washington' as term, 1 as count
union
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count;

create view temp as select f1.docid as row, f2.docid as col, f1.count*f2.count as val from frequency_search f1, frequency_search f2 where f1.term=f2.term and f1.docid='q' and f1.docid!=f2.docid;
//multiplying the corressponding rows and columns for a matrix * transpose(matrix) multiplication
// only for docid being ='q' because i want only the documents which match with the keyword in q(query)

create view sim_matrix as 
select row, col, sum(val) value from temp
group by row,col;
//generating the similarity matrix


select * from sim_matrix;	

