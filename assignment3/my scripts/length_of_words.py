import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
	lengths={
		"big":0,
		"medium":0,
		"small":0}
	#big is >=10 small is <=4
	key = record[0]
	value = record[1]
	words = value.split()
	for w in words:
		if len(w)<4:
			lengths["small"]+=1
		elif len(w)<10:
			lengths["medium"]+=1
		else:
			lengths["big"]+=1
	
	for key in lengths.keys():
		mr.emit_intermediate(key,lengths[key])    


def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = 0
    for v in list_of_values:
      total += v
    mr.emit((key, total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
