import networkx as nx
import matplotlib.pyplot as plt
from bfs import bfs
from dfs import dfs
from id_dfs import iddfs

# Your graph
graph = {
    1: [2, 3],  #Root node 1 connects with 2 and 3
    2: [4, 5],  #2 connects with 4 and 5
    3: [6, 7],  #3 connects with 6 and 7
    4: [8, 9],  #4 connects with 8 and 9
    5: [],      #5 has no children
    6: [],      #6 has no children
    7: [11]     #7 connects with 10
}

# Create directed graph
G = nx.DiGraph()

# Add edges
for node, neighbors in graph.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

# Draw
plt.figure(figsize=(6, 5))
pos = nx.spring_layout(G)  # auto layout

nx.draw(
    G, pos,
    with_labels=True,
    node_color='lightblue',
    node_size=2000,
    font_size=12,
    font_weight='bold',
    arrows=True
)

plt.title("Graph Representation")
plt.show()

# Determine the root node (starting point)
start_node = '1'

# Calculating max depth for IDDFS (adjusted from my tree)
max_depth = 3 #my tree level is 4

print("BFS:", bfs(graph, start_node)) 
print("DFS:", dfs(graph, start_node)) 
print("IDDFS:", iddfs(graph, start_node, max_depth)) 