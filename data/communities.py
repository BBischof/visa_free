import networkx as nx
import json
from CommunityDetection import GirvanNewman



# Reciprocal network
G = 

# choose number of communities
nComm = 

# perform community detection
GN = GirvanNewman(network)
comm = GN.communities(nCommunities=nComm)

for x in comm:
	print json.dumps(list(x))


