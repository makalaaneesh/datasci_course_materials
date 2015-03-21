import MapReduce
import sys

"""
multiplying two matrices
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line
dim=5 # square matrix 5x5

def mapper(record):
    # key: depends on the matrix.
    # value: the whole record
    value=record
    if record[0]=="a":
      key_1=record[1]
      for k in range(0,dim):
        mr.emit_intermediate((key_1,k),value)
    elif record[0]=="b":
      key_1=record[2]
      for k in range(0,dim):
        mr.emit_intermediate((k,key_1),value)
    




def reducer(key, list_of_values):
    # key: the row,col for the final matrix 
    # value: the a and b values that need to be combined
    a_list=[]
    b_list=[]
    for item in list_of_values:
      if item[0]=="a":
        a_list.append(item)
      elif item[0]=="b":
        b_list.append(item)

    total=0
    for a_item in a_list:
      for b_item in b_list:
        if a_item[2]==b_item[1]:   # if a.col=b.row
          total=total+(a_item[3]*b_item[3])   #multiplying the values
          break
    mr.emit([key[0],key[1],total])
    
    

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
