import MapReduce
import sys

"""
create an inverted index from books.json which prints word,(doc1,doc2,doc3)
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    l=[]  
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
      if [w,key] not in l:
        l.append([w,key])
    for item in l:
      mr.emit_intermediate(item[0], item[1])

def reducer(key, list_of_values):
    # key: word
    # value: list of docs it appears in 
    
    mr.emit((key, list_of_values))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
