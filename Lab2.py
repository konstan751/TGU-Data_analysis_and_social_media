#2. Требуется получить центральность для четырёх узлов, среди которых три имеют одинаковую центральность,
#а четвёртый отличающуюся от них в большую сторону.

import networkx

# Для визуализации графа
# in Linux: apt-get install elementary-icon-theme
import matplotlib
import matplotlib.pyplot as plt

G = networkx.Graph()
G.add_nodes_from([1, 2, 3, 4])
G.add_edges_from([(1, 4), (2, 4), (3, 4)])

# Центральность узлов (важность узлов)
x = sorted(list(networkx.degree_centrality(G).items()), key=lambda i: i[1], reverse=True)
print(*x[:4], sep='\n')
print (G)
networkx.draw(G, node_size=500, with_labels=True, node_color='y')
plt.show()