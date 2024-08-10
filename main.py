import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node("Singapore")
G.add_node("San Francisco")
G.add_node("Tokyo")

G.add_nodes_from(["Riga", "Copenhagen"])

G.add_edge("Sinagore", "San Francisco")
G.add_edge("San Francisco", "Tokyo")
G.add_edges_from([
    ("Riga", "Copenhagen"),
    ("Copenhagen", "Singapore"),
    ("Singapore", "Tokyo"),
    ("Riga", "San Francisco"),
    ("San Francisco", "Singapore")
])
pos = nx.circular_layout(G)
print(G)
nx.draw(G, pos, with_labels=True)
nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels={
        ("Singapore", "Tokyo"): '2 flights daily',
        ("San Francisco", "Singapore"): '5 flights daily'
    },
    font_color='red')
options = {
    'node_color': 'yellow',
    'node_size': 3500,
    'width': 1,
    'arrowstyle': '-|>',
    'arrowsize': 18,
    'edge_color': 'blue',
}
nx.draw(G, pos, with_labels=True, arrows=True, **options)
plt.show()
