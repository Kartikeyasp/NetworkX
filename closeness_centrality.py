import networkx as nx
import matplotlib.pyplot as plt


def closeness_centrality(G):
    #creating a dictionary for centrality
    centrality = dict.fromkeys(G.nodes,0.0)
    #calculating total number of nodes
    n = len(G.nodes)
    
    for node in G.nodes:
        #Calculating lengths of shortest paths from each source to every other node
        length = nx.single_source_bellman_ford_path_length(G, node, weight='weight')
        
        #Adding lenghts of shortest paths
        total_distance = sum(length.values())
        
        #Calculate centrality for every node using formula
        if total_distance != 0 and n > 1:
            centrality[node] = (n - 1) / total_distance
    
    return centrality


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

#calling closeness function
closeness = closeness_centrality(G)

#printing closeness
for node, val in closeness.items():
    print(f'{node}: {val}')




# pos = nx.circular_layout(G)  # Layout for positioning the nodes
# plt.figure(figsize=(8, 6))  # Set the figure size

# # Draw nodes and edges
# nx.draw(G, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=10, font_weight='bold', arrows=True)

# # Draw edge labels (weights)
# edge_labels = nx.get_edge_attributes(G, 'weight')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# # Display the graph
# plt.title("Directed Graph with Weights")
# plt.show()

# for i in range(1,6,1):
#     try:
#         lengths,paths = nx.single_source_bellman_ford(G,source = i, weight = 'weight')

#         print(f"Shortest path from node{i}:")
#         for target in paths:
#                 print(f"Path to {target}: {paths[target]} with total weight {lengths[target]}")
#     except nx.NetworkXUnbounded:
#          print("Graph contains a neagative weight cycle. Bellman-Ford cannot proceed.")