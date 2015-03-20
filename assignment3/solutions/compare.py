# a python script to compare two json files to see if my json solution mathces with the json solution provided in the course
import json
import sys
list1=[]
list2=[]
def check(f1,f2):
	
	for line in f1:
		list1.append(json.loads(line))
	for line in f2:
		list2.append(json.loads(line))
# this is code specific to comparing the solutions to the inverted_index.jsonfile	
	# for item in list1:
	# 	item[1]=[s.encode('utf-8') for s in item[1]]
	# 	item[1]=sorted(item[1])
	# for item in list2:
	# 	item[1]=[s.encode('utf-8') for s in item[1]]
	# 	item[1]=sorted(item[1])
# end of block of code

	flag=True
	for item in list1:
		if item not in list2:
			flag=False
	for item in list2:
		if item not in list1:
			flag=False
	print flag
	
if __name__ == '__main__':
	f1=open(sys.argv[1])
	f2=open(sys.argv[2])
	check(f1,f2)





