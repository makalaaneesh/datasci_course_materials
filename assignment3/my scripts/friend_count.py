import MapReduce
import sys

"""
calculatinf the friend count
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: person
    # value: friend
     
    key = record[0]
    value = record[1]
    words = value.split()
    mr.emit_intermediate(key,1)

def reducer(key, list_of_values):
    # key: word
    # value: list of docs it appears in 
    total=0
    for item in list_of_values:
      total=total+item

    mr.emit((key, total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
