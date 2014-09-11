"""
AlgorithmicThinking-Project1-DegreeDistributionsForGraphs
"""
EX_GRAPH0 = {0: set([1,2]),
             1: set(),
             2: set()}
EX_GRAPH1 = {0: set([1,4,5]),
             1: set([2,6]),
             2: set([3]),
             3: set([0]),
             4: set([1]),
             5: set([2]),
             6: set()}
EX_GRAPH2 = {0: set([1,4,5]),
             1: set([2,6]),
             2: set([3,7]),
             3: set([7]),
             4: set([1]),
             5: set([2]),
             6: set(),
             7: set([3]),
             8: set([1,2]),
             9: set([0,3,4,5,6,7])}

def make_complete_graph(num_nodes):
    """ Makes a 'complete' graph having a given no. of nodes """
    complete_graph = {}
    if num_nodes > 1:
        for node_no in range(0, num_nodes):
            complete_graph[node_no] = set([num for num in range(0, num_nodes) if num!=node_no])
    elif num_nodes == 1:
        complete_graph[0] = set([])
    return complete_graph;

def compute_in_degrees(digraph):
    """ Computes the in_degrees for the nodes in a digraph """
    in_degrees_dict = {}
    if len(digraph) > 0:
        for node, to_nodes in digraph.iteritems():
            if node not in in_degrees_dict:
                in_degrees_dict[node] = 0
            if(len(to_nodes) > 0):
                for to_node in to_nodes:
                    if to_node in in_degrees_dict:
                        in_degrees_dict[to_node] += 1
                    else:
                        in_degrees_dict[to_node] = 1
    return in_degrees_dict;

def in_degree_distribution(digraph):
    """ Computes the unnormalized distribution of the in-degrees of the graph """
    in_degrees_dist = {}
    in_degrees_dict = {}
    if len(digraph) > 0:
        for node, to_nodes in digraph.iteritems():
            if node not in in_degrees_dict:
                in_degrees_dict[node] = 0
            if(len(to_nodes) > 0):
                for to_node in to_nodes:
                    if to_node in in_degrees_dict:
                        in_degrees_dict[to_node] += 1
                    else:
                        in_degrees_dict[to_node] = 1
        for to_node, in_degree in in_degrees_dict.iteritems():
            if in_degree in in_degrees_dist:
                in_degrees_dist[in_degree] += 1
            else:
                in_degrees_dist[in_degree] = 1
    return in_degrees_dist;
