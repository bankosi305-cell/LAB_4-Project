import networkx as nx
import matplotlib.pyplot as plt
from bfs import bfs
from dfs import dfs
from id_dfs import iddfs

# Your graph
graph = {
    'A': ['B', 'C'],    #Root node A connects with B and C
    'B': ['D', 'E'],    #B connects with D and E
    'C': ['F'],         #C connects with F
    'D': [],            #D has no children
    'E': ['G'],         #E connects with 
    'F': [],            #F has no children
    'G': []             #G has no children
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
start_node = 'A'

# Calculating max depth for IDDFS (adjusted from my tree)
max_depth = 3 #my tree level is 4

print("BFS:", bfs(graph, start_node)) 
print("DFS:", dfs(graph, start_node)) 
print("IDDFS:", iddfs(graph, start_node, max_depth)) 