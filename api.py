# Social Networks analysis HW-1
# Michal Lorberbom - 311120133
# Gal Meir - 305382137
import pandas as pd
import heapq
from operator import itemgetter


adjacency_list, reverse_adjacency_list = {}, {}
inOrder = []
byValue = {}


# Input: the path for the input file
# Description:
# •	Loads a graph from a text file to the memory.
# •	The csv file is given as an edge list – i.e, <source, destination> pairs of node names.
# •	The file does not include headers.
# •	See Wikipedia_votes.csv as an example. However, treat the input node names as strings
# •	Make sure to load the graph into an efficient data structure
# Return Value: None
def load_graph(path):
    global reverse_adjacency_list
    global adjacency_list
    df = pd.read_csv(header=None, index_col=None, filepath_or_buffer=path, names=['Source', 'Dest'])
    nodes = pd.unique(df[['Source', 'Dest']].values.ravel())
    reverse_adjacency_list = dict.fromkeys(nodes)
    adjacency_list = dict.fromkeys(nodes)
    # foreach row in the csv with its index
    for index, row in df.iterrows():
        # add to adjacency_list
        if adjacency_list[row[0]] is not None:
            adjacency_list[row[0]].append(row[1])
        else:
            adjacency_list[row[0]] = [row[1]]
        # add to reverse_adjacency_list
        if reverse_adjacency_list[row[1]] is not None:
            reverse_adjacency_list[row[1]].append(row[0])
        else:
            reverse_adjacency_list[row[1]] = [row[0]]


# Input: default values: β = 0.85, δ = 0.001 (the epsilon in the lecture slides)
#        and maxIterations – maximum number of page rank iterations, default value = 20.
# Description:
# •	Calculates the PageRank for each of the nodes in the graph.
# •	The calculation will end in one of two stop conditions: after maxIterations iterations,
#   or when the difference between two iterations is smaller than δ.
# •	Save the results into an internal data structure for an easy access
# Return Value: None
def calculate_page_rank(beta=0.85, delta=0.001, maxIterations=20):
    global adjacency_list, reverse_adjacency_list, inOrder, byValue
    prev_value, tmp_value = {}, {}
    nodes_amount = len(inOrder)
    bigger_than_delta = True
    byValue = dict.fromkeys(adjacency_list.keys(), 1.0/float(nodes_amount))         # page rank initialization to 1/N
    while maxIterations > 0 and bigger_than_delta:   # stop conditions
        maxIterations -= 1
        prev_value = byValue.copy()             # page rank of the previous iteration
        sum, epsilon = 0.0, 0.0                     #sum is S from leaked PageRank calculation , epsilon is for the difference between two iterations
        for node in adjacency_list.keys():      # calculate temporary PageRank
            if node not in reverse_adjacency_list or reverse_adjacency_list[node] is None:
                tmp_value[node] = 0.0           # node in-deg. is 0
            else:
                current_value = 0.0
                for node_in in reverse_adjacency_list[node]:
                    current_value += beta * float(prev_value[node_in]) / float(len(adjacency_list[node_in]))
                tmp_value[node] = current_value
                sum += tmp_value[node]
        for node in adjacency_list.keys():         # calculate the leaked PageRank
            byValue[node] = tmp_value[node] + ((1-sum)/float(nodes_amount))
            epsilon += abs(byValue[node]-prev_value[node])          # calculate the difference between two iterations
        bigger_than_delta = epsilon >= delta    # if the difference between two iterations is smaller than delta the PageRank calculate will stop


# input: str-The node name
# Description:
# •	Returns the PageRank of a specific node.
# •	Return “-1” for non-existing name
# Return Value: Double- The PageRank of the given node name
def get_PageRank(node_name):
    global byValue
    if node_name in byValue.keys():
        return byValue[node_name]
    return -1


# input: Integer- How many nodes
# Description:
# •	Returns a list of n nodes with the highest PageRank.
# Return Value: List of pairs <node name, PageRank value >
def get_top_nodes(n):
    global byValue
    top_items = heapq.nlargest(n, byValue.items(), key=itemgetter(1))
    return list(top_items)


# Input: None
# Description:
# •	Returns a list of the PageRank for all the nodes in the graph
# •	The list should include pairs of node id, PageRank value of that node.
# •	The list should be ordered according to the PageRank values from high to low
# Return Value: List of pairs <node name, PageRank value >
def get_all_PageRank():
    global byValue
    all_items = sorted(byValue.items(), key=itemgetter(1), reverse=True)
    return list(all_items)

if __name__ == '__main__':
    print("***" * 25 + "Wikipedia_votes" + "***" * 25)
    load_graph('Wikipedia_votes.csv')
    calculate_page_rank()
    get_top_nodes(10)