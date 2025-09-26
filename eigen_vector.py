import numpy as np
import networkx as nx




# --- Eigenvector centrality by power iteration ---
def eigenvector_centrality(adj_matrix, max_iter=1000, tol=1e-6):
    A = np.array(adj_matrix, dtype=float)  #changing adj_matrix to a numpy array
    n = A.shape[0]                         #number of rows of A
    x = np.ones(n)                         #column matrix with all 1's

    for _ in range(max_iter):
        x_new = A @ x  # multiply
        norm = np.linalg.norm(x_new)       #calculate normalization (root of sum of squares)
        if norm == 0:                      #if norm == 0 (disconnect graph)
            return x_new
        x_new /= norm                      #normalize
        if np.linalg.norm(x - x_new) < tol: #if difference less than tolerance break and return
            x = x_new
            break
        x = x_new                           #otherwise give x_new to x and continue iterating
    return x

# --- Create your graph ---
G = nx.Graph()

# Adding nodes
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)

# Adding edges with weights
G.add_edge(1,2, weight=0.5)
G.add_edge(2,5, weight=0.8)
G.add_edge(1,5, weight=0.3)
G.add_edge(1,3, weight=0.6)
G.add_edge(3,5, weight=0.2)
G.add_edge(1,4, weight=0.6)
G.add_edge(4,3, weight=0.7)

# --- Build adjacency matrix from G ---
# Ensure nodes are in a fixed order:
nodes = list(G.nodes())
n = len(nodes)
A = np.zeros((n, n), dtype=float)  #Creates an n*n matrix with all zeroes

for i, u in enumerate(nodes):           #enumerate gives a index, iterable value pair
    for j, v in enumerate(nodes):
        if G.has_edge(u, v):            #If there exists an edge between u and v nodes
            A[i, j] = G[u][v]['weight'] #In index i,j insert the weight of the edge

centralities = eigenvector_centrality(A)

# Map back to node labels
centrality_dict = {node: centralities[i] for i, node in enumerate(nodes)}

print("\nEigenvector centrality scores:")
for node, score in centrality_dict.items():
    print(f"Node {node}: {score:.4f}")

print(nx.eigenvector_centrality(G, weight="weight"))