# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt


def main():
    G = nx.Graph()
    G.add_nodes_from([0, 1, 2, 3, 4, 5])
    G.add_edges_from([(0, 1), (1, 2), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5)])
    pos = {
        0: (0, 0),
        1: (1, 0),
        2: (2, 0),
        3: (3, 0),
        4: (3.5, 1.732 / 2),
        5: (3.5, -1.732 / 2)
    }
    labels = {v: '{}'.format(v) for v in G.nodes()}
    fig = plt.figure(figsize=(5, 5))
    ax = fig.gca()
    nx.draw_networkx_nodes(G, pos, ax=ax)
    nx.draw_networkx_labels(G, pos, labels, ax=ax)
    nx.draw_networkx_edges(G, pos, ax=ax)
    ax.axis("off")
    ax.set_position([0, 0, 1, 1])
    ax.set_xlim(-0.4, 3.8)
    ax.set_ylim(-2.1, 2.1)

    plt.show()
    plt.close()

if __name__ == '__main__':
    main()
