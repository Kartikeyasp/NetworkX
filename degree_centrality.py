import networkx as nx
import matplotlib.pyplot as plt

def degree_centrality(G):
    N = len(G.nodes)

    in_degree_centrality = dict.fromkeys(G.nodes, 0.0)
    out_degree_centrality = dict.fromkeys(G.nodes, 0.0)

    for node in G.nodes():
        in_degree_centrality[node] = {node: G.in_degree(node)/(N-1)}

    for node in G.nodes():
        out_degree_centrality[node] = {node: G.out_degree(node)/(N-1)}
    
    return in_degree_centrality, out_degree_centrality

    


# Create the graph
G = nx.DiGraph()

#Adding nodes
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)

#Adding edges
G.add_edge(1,2, weight = -0.5)
G.add_edge(2,5, weight = 0.8)
G.add_edge(1,5, weight = 0.3)
G.add_edge(1,3, weight = -0.6)
G.add_edge(3,5, weight = 0.2)
G.add_edge(1,4, weight = 0.6)
G.add_edge(4,3, weight = -0.7)

in_degree, out_degree = degree_centrality(G)

print("Indegree")
print(in_degree)
print("Outdegree")
print(out_degree)