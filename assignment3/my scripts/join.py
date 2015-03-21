import MapReduce
import sys

"""
performing relational join using map reduce.
realtional join on the common attribute order_id
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: the table name: order/ line_item
    # value: the attributes of the tuple

    order_id= record[1]#key
    mr.emit_intermediate(order_id,record)

def reducer(key, list_of_values):
    # key: the common attribute
    # value: list of records from botht the tables where the key occurs
    order_list=[]
    line_item_list=[]
    for item in list_of_values:
      if item[0]=='order':
        order_list.append(item)
      elif item[0]=='line_item':
        line_item_list.append(item)

    for order in order_list:
      for line_item in line_item_list:
        mr.emit(order+line_item)
    

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
