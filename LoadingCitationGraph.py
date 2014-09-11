"""
Provided code for Application portion of Module 1

Imports physics citation graph 
"""

# general imports
# import collections
# import math
import random
import sys
import urllib2

import matplotlib.pyplot as plt

sys.path.append("/AlgorithmicThinking/Project1/")
from DPATrialClass import DPATrial


# Set timeout for CodeSkulptor if necessary
# import codeskulptor
# codeskulptor.set_timeout(20)
###################################
# Code for loading citation graph
CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"

def load_graph(graph_url):
    """
    FOR QUESTION 1: 
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ :-1]
    
    print "Loaded graph with", len(graph_lines), "nodes"
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 :-1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph

def calculate_in_degree_distribution(digraph):
    """ FOR QUESTION 1: Computes the unnormalized distribution of the in-degrees of the graph """
    in_degrees_dist = {}
    in_degrees_dict = {}
    if len(digraph) > 0:
        for from_node, to_nodes in digraph.iteritems():
            if from_node not in in_degrees_dict:
                in_degrees_dict[from_node] = 0
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
    return in_degrees_dist

def normalize_distribution(dist_dict):
    """ FOR QUESTION 1: TO NORMALIZE A DISTRIBUTION INPUTTED AS A DICTIONARY """
    total_count = 0.0
    normalized_dist_dict = {}
    for node, node_count in dist_dict.iteritems():
        total_count += node_count;
    # "NODE" IS A COUNT OF CITATIONS, NODE_COUNT IS THE NO. OF PAPERS WITH THAT MANY CITATIONS
    if total_count > 0:
        normalized_dist_dict = {node: float(node_count / total_count) for node, node_count in dist_dict.iteritems()}
#         normalized_dist_dict = collections.OrderedDict(sorted(normalized_dist_dict.items()))
#         print(normalized_dist_dict)
    return normalized_dist_dict

def generate_er_graph(num_nodes,prob):
    """ FOR QUESTION 2 """
    random_digraph = {}
    for nodex in range(0,num_nodes):
        for nodey in range(0,num_nodes):
            if nodey != nodex:
                rand = random.random()
                if nodex not in random_digraph:
                    random_digraph[nodex] = set([])
                if (rand < prob):
                    random_digraph[nodex].add(nodey)
    return random_digraph

def calculate_out_degrees(digraph):
    """ FOR QUESTION 3: COMPUTES THE UNNORMALIZED DISTRIBUTION OF THE OUT-DEGREES OF A GIVEN GRAPH (REPRESENTED AS ADJACENCY LIST """
    out_degrees_dict = {}
    if len(digraph) > 0:
        for from_node, to_nodes in digraph.iteritems():
            if from_node in out_degrees_dict:
                out_degrees_dict[from_node] += len(to_nodes)
            else:
                out_degrees_dict[from_node] = len(to_nodes)
    return out_degrees_dict

def calculate_average_value(values_dict):
    """ FOR QUESTION 3: COMPUTES THE UNNORMALIZED DISTRIBUTION OF THE OUT-DEGREES OF A GIVEN GRAPH (REPRESENTED AS ADJACENCY LIST """
    values_total = 0.0
    avg_val = 0
    if len(values_dict) > 0:
        # value IS A NO. OF NODES HAVING AN OUT-DEGREE = NODE 
        for node, value in values_dict.iteritems():
            values_total += value
        avg_val = int(values_total/len(values_dict))
    return avg_val

def make_complete_graph(num_nodes):
    """ FOR QUESTION 4 """
    complete_graph = {}
    if num_nodes > 1:
        for node_no in range(0, num_nodes):
            complete_graph[node_no] = set([num for num in range(0, num_nodes) if num!=node_no])
    elif num_nodes == 1:
        complete_graph[0] = set([])
    return complete_graph;

def generate_dpa_graph(tot_num_nodes,min_nodes):
    """ FOR QUESTION 4 : Algorithm DPA"""
#     DPATrial CLASS USAGE
#     SELECT A RANDOM NODE FROM THOSE IN THE DPA OBJECT
#     random.choice(dpa_object._node_numbers)
#     GET NO. OF NODES IN THE DPA OBJECT (INCL. DUPLICATES THAT REPRESENT INCREASED PROBABILITY OF SELECTION OF THOSE NODES)
#     dpa_object._num_nodes
#     LOOP count TIMES AND CHOOSE A NODE NUMBER AT RANDOM IN EACH LOOP AND ADD IT TO A SET THAT WILL FORM THE NEW EDGES  
#     dpa_object.run_trial(count)

    dpa_graph = make_complete_graph(min_nodes)
    dpa_object = DPATrial(min_nodes+1);
   
    for new_node in range(min_nodes, tot_num_nodes):
        dpa_graph[new_node] = set([])
        dpa_object.run_trial(min_nodes+1)
        for edge_to in range(0,min_nodes+1):
            dpa_graph[new_node].add(random.choice(dpa_object._node_numbers))
    return dpa_graph;

# QUESTION 1: PLOTTING CITATION GRAPH

# citation_graph = load_graph(CITATION_URL)
# in_deg_dist_cit_graph = calculate_in_degree_distribution(citation_graph)
# norm_dist_cit_graph = normalize_distribution(in_deg_dist_cit_graph)

# plt.xlabel('No. of Citations')
# plt.ylabel('Fraction of Papers cited a given No. of times')
# plt.title('Normalized distribution of No. of Citations of Physics theory papers')
# plt.loglog(norm_dist_cit_graph.keys(),norm_dist_cit_graph.values(),'ro',basex=2,basey=2,markersize=4)
# plt.show()
# plt.loglog(norm_dist_cit_graph.keys(),norm_dist_cit_graph.values(),'ro',norm_dist_rand_digraph.keys(),norm_dist_rand_digraph.values(),'b^',basex=2,basey=2,markersize=4)


# QUESTION 2: PLOTTING ER GRAPH

# random_digraph = generate_er_graph(300,0.5)
# print(random_digraph)
# in_deg_dist_rand_digraph = calculate_in_degree_distribution(random_digraph)
# norm_dist_rand_digraph = normalize_distribution(in_deg_dist_rand_digraph)
# 
# plt.xlabel('In-degree of Nodes')
# plt.ylabel('Fraction of Nodes having a given In-degree')
# plt.title('Normalized in-degree distribution for an ER graph (n=300,p=0.5)')
# plt.loglog(norm_dist_rand_digraph.keys(),norm_dist_rand_digraph.values(),'bo',basex=2,basey=2,markersize=5)
# plt.show()

# QUESTION 3: PLOTTING OUT-DEGREES OF ER GRAPH 
# citation_graph = load_graph(CITATION_URL)
# out_degrees_cit_graph = calculate_out_degrees(citation_graph)
# avg_out_deg = calculate_average_value(out_degrees_cit_graph)
# print(avg_out_deg)

# QUESTION 4: COMPUTE DPA GRAPH, PLOT IN-DEGREE DISTRIBUTION
dpa_graph = generate_dpa_graph(27770,13)
in_deg_dist_dpa_graph = calculate_in_degree_distribution(dpa_graph)
norm_in_deg_dist_dpa_graph = normalize_distribution(in_deg_dist_dpa_graph)
print(norm_in_deg_dist_dpa_graph)

plt.title("Normalized log/log plot of Points in DPA Graph's in-degree distribution")
plt.xlabel('In-degree of Points')
plt.ylabel('Fraction of Points having a given In-degree')
plt.loglog(norm_in_deg_dist_dpa_graph.keys(),norm_in_deg_dist_dpa_graph.values(),'ro',basex=2,basey=2,markersize=4)
plt.show()

# REFERENCE CODE
# plt.loglog(norm_dist_rand_digraph.keys(),norm_dist_rand_digraph.values(),'b^',basex=2,basey=2,markersize=4)
# plt.xlim([0, 2**12])
# plt.ylim([-1000, 1])
# plt.bar(range(len(norm_dist)), [math.log(value) for value in norm_dist.values()], align='center')
# plt.xticks(range(len(norm_dist)), [-1000 if value <= 0 else math.log(value) for value in norm_dist.keys()])
