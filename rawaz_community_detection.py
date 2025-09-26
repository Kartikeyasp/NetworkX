import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, fcluster

# --- Step 1: Build graph from Slide 36 ---
G = nx.Graph()
edges = [
    ("A","B"), ("A","C"), ("B","C"),     # ABC triangle
    ("C","D"), ("D","E"), ("D","I"),     # D connections
    ("E","F"), ("E","G"), ("F","G"),     # EFG triangle
    ("G","H"),                           # weak link
    ("H","I"), ("H","J"), 
    ("I","J"), ("I","K"), ("J","K")      # HIJK clique
]
G.add_edges_from(edges)
nodes = list(G.nodes())
n = len(nodes)

# --- Step 2: Compute similarity matrix (Ravasz topological overlap) ---
similarity = np.zeros((n, n))

for i in range(n):
    for j in range(i+1, n):
        ni, nj = set(G.neighbors(nodes[i])), set(G.neighbors(nodes[j]))
        common = len(ni & nj)
        if G.has_edge(nodes[i], nodes[j]):
            common += 1
        ki, kj = len(ni), len(nj)
        if min(ki, kj) > 0:
            sij = common / min(ki, kj)
        else:
            sij = 0
        similarity[i, j] = similarity[j, i] = sij

# --- Step 3: Agglomerative clustering (average linkage) ---
dist = 1 - similarity
condensed = dist[np.triu_indices(n, 1)]
Z = linkage(condensed, method="average")

# --- Step 4: Cut dendrogram to form communities ---
# Adjust t depending on how strict you want merging to be
clusters = fcluster(Z, t=0.4, criterion="distance")

# --- Step 5: Assign communities ---
community_dict = {nodes[i]: clusters[i] for i in range(n)}

print("Communities found:")
for c in set(clusters):
    print(f"Community {c}: {[node for node in nodes if community_dict[node]==c]}")

# --- Step 6: Draw graph with detected communities ---
colors_map = {
    1: "purple",   # ABC
    2: "green",    # EFG
    3: "royalblue",# HIJK
    4: "teal"      # D (connector)
}
node_colors = [colors_map[community_dict[n]] for n in G.nodes()]

pos = {
    "A": (-1, 2), "B": (1, 2), "C": (0, 1.5),
    "D": (0, 0.8),
    "E": (-1, 0), "F": (-1.5, -0.8), "G": (-0.5, -0.8),
    "H": (0.5, -0.5), "I": (1, 0), "J": (0.5, -1), "K": (1.2, -0.8)
}

plt.figure(figsize=(8,6))
nx.draw_networkx(G, pos, node_color=node_colors, edgecolors="black",
                 with_labels=True, node_size=700, font_color="white")

plt.title("Communities detected using Ravasz Algorithm (Slide 36 Graph)")
plt.axis("off")
plt.show()