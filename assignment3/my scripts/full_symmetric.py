import MapReduce
import sys

"""
creating a full symmetric friendship assuming that friend(a,b) means friend(b,a)
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: a
    # value: b( b is friend of a)
    a=record[0]
    b=record[1]
    mr.emit_intermediate(a,b)
    mr.emit_intermediate(b,a)

def remove_all_duplicates(l,val):# condition that a maximum of 2 duplicates is possible
  l.remove(val)
  if val in l:
    l.remove(val)
  else:
    l.append(val)


def reducer(key, list_of_values):
    # key: a
    # value: list of friends of a that may include duplicates
    dup=[]
    list_of_values2=list(set(list_of_values))# just to store all the list items to iterate through the main list and remove duplicates
    for item in list_of_values2:
      remove_all_duplicates(list_of_values,item)
    for friend in list_of_values:
      mr.emit((key,friend))
    
    

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
