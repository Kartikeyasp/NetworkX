import networkx as nx

def edge_betweenness(G):
    #dictionnary with keys as edges from graph and values as 0.0
    betweenness = dict.fromkeys(G.edges(), 0.0)
    #list of nodes to iterate through as source
    nodes = list(G.nodes())
    
    for s in nodes:
        #using bellman ford create a dictionary with source as key and shortest path to each destination as value
        paths = nx.single_source_bellman_ford_path(G, s, weight='weight')
        
        #Iterate through each shortest path giving source to t and shortest path to sp
        for t, sp in paths.items():
            #Ignore paths going from node to itself
            if t == s:
                continue
            #Using zip and slicing get edges in shortest path ((u,v) pairs) and increment by 1 
            for u, v in zip(sp[:-1], sp[1:]):
                betweenness[(u, v)] += 1.0
    
    return betweenness


#Creating the graph
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

#calling betweenness function
betweenness = edge_betweenness(G)

#printing betweenness
print("Edge Betweenness Centrality:")
for edge, val in betweenness.items():
    print(f"{edge}: {val}")
