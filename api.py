# Social Networks analysis HW-1
# Michal
# Gal Meir - 305382137


# Input: the path for the input file
# Description:
# •	Loads a graph from a text file to the memory.
# •	The csv file is given as an edge list – i.e, <source, destination> pairs of node names.
# •	The file does not include headers.
# •	See Wikipedia_votes.csv as an example. However, treat the input node names as strings
# •	Make sure to load the graph into an efficient data structure
# Return Value: None
def load_graph(path):
    return 0


# Input: default values: β = 0.85, δ = 0.001 (the epsilon in the lecture slides)
#        and maxIterations – maximum number of page rank iterations, default value = 20.
# Description:
# •	Calculates the PageRank for each of the nodes in the graph.
# •	The calculation will end in one of two stop conditions: after maxIterations iterations,
#   or when the difference between two iterations is smaller than δ.
# •	Save the results into an internal data structure for an easy access
# Return Value: None
def calculate_page_rank(beta=0.85, delta=0.001, maxIterations=20):
    return 0


# input: str-The node name
# Description:
# •	Returns the PageRank of a specific node.
# •	Return “-1” for non-existing name
# Return Value: Double- The PageRank of the given node name
def get_PageRank(node_name):
    return 0


# input: Integer- How many nodes
# Description:
# •	Returns a list of n nodes with the highest PageRank.
# Return Value: List of pairs <node name, PageRank value >
def get_top_nodes(n):
    return 0


# Input: None
# Description:
# •	Returns a list of the PageRank for all the nodes in the graph
# •	The list should include pairs of node id, PageRank value of that node.
# •	The list should be ordered according to the PageRank values from high to low
# Return Value: List of pairs <node name, PageRank value >
def get_all_PageRank():
    return 0
