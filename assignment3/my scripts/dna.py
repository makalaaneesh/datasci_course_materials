import MapReduce
import sys

"""
removing the last 10 characters off a dna sequence and printing all the uniue dna sequences
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: dna sequence identifier
    # value: dna sequence
     
    key = record[0]
    value = record[1]
    value=value[:-10]
    mr.emit_intermediate(value,1)

def reducer(key, list_of_values):
    # key: dna sequence
    # value: list of 1s indicating duplicates
 

    mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
