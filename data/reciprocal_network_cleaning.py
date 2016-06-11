import sys
import json





graph = {"nodes":[], "links":[]}

node_set = set()
edge_set = []

input_file = open(sys.argv[1])
for line in input_file:
	record = line.rstrip().split('-')
	node_set.add(record[0])
	node_set.add(record[1])
	edge_set.append(record)


node_index = {}
for i,x in enumerate(node_set):
	node_index[x] = i
	node_entry = {'name': x}
	graph["nodes"].append(node_entry)


for edge in edge_set:
	s = edge[0]
	t = edge[1]
	edge_entry = {'source': node_index[s], 'target': node_index[t], 'value':0}
	graph["links"].append(edge_entry)


print json.dumps(graph)


	
