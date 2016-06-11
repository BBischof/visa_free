# -*- coding: utf-8 -*-
"""
Community detection by Girvan - Newman algorithm.

@reference - Community structure in social and biological networks  
@reference_URL - http://www.pnas.org/content/99/12/7821

@author - Janu Verma
Created on 02/14/2016
"""

import networkx as nx




class GirvanNewman:
	"""
	Implements the Girvan - Newman algorithm for community detection in a graph. 
	"""

	def __init__(self, graph):
		"""
		Instantiates the class.

		Parameters
		-----------
		graph - A networkx graph or digraph. 
		"""
		self.g = graph




	def communitySplits(self, graph, weight=None):
		"""
		Compute the splits for the formation of communities. 

		Parameters
		----------
		graph -  A networkx graph of digraph.
		weight (string) - If None, all edge weights are considered equal. 
			Otherwise holds the name of the edge attribute used as weight


		Returns
		-------
		The graph with weak edges removed. 


		Usage
		-----
		>>> G = nx.path_graph(10)
		>>> out = GirvanNewman(G)
		>>> comm = out.communities(G, weight=None)
		>>> for x in comm:
				print x
		"""

		nConnComp = nx.number_connected_components(graph)
		nComm = nConnComp

		while (nComm <= nConnComp):
			betweenness = nx.edge_betweenness_centrality(graph, weight=weight)
			if (len(betweenness.values()) != 0 ):
				max_betweenness = max(betweenness.values())
			else:
				break	
			for u,v in betweenness.iteritems():
				if float(v) == max_betweenness:
					# print u,v
					graph.remove_edge(u[0], u[1])
			nComm = nx.number_connected_components(graph)			
		return graph		




	def communities(self, nCommunities, weight=None):
		"""
		Compute communities.

		Parameters
		----------
		nCommunities - number of communities to be returned.
			This is added to simplify the process, the original GN algorithm doesn't 
			need predecided number of communities. 
			Other measures like a threshold on betweenness centrality can be used instead.
		
		weight (string) - If None, all edge weights are considered equal. 
			Otherwise holds the name of the edge attribute used as weight. 


		Returns
		--------
		A list of communities where each community is a list of the nodes in the community.	 
		"""
		gr = self.g
		n = nx.number_connected_components(gr)
		components = nx.connected_components(gr)

		while (n < nCommunities):
			gr = self.communitySplits(gr, weight=weight)
			components = nx.connected_components(gr)
			n = nx.number_connected_components(gr)
			if gr.number_of_edges() == 0:
				break
		return components
					
		


