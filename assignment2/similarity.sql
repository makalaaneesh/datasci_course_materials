create view temp as select f1.docid as row, f2.docid as col, f1.count*f2.count as val from frequency f1, frequency f2 where f1.term=f2.term;
//multiplying the corressponding rows and columns for a matrix * transpose(matrix) multiplication

create view sim_matrix as 
select row, col, sum(val) from temp
group by row,col;
//generating the similarity matrix


select * from sim_matrix where row='10080_txt_crude' and col='17035_txt_earn';

