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
    fw, fh = 4, 4
    fig = plt.figure(figsize=(fw, fh))
    ax = fig.gca()
    n = nx.draw_networkx_nodes(G, pos, ax=ax, node_color='white')
    n.set_edgecolor("blue")
    nx.draw_networkx_labels(G, pos, labels, ax=ax)
    nx.draw_networkx_edges(G, pos, ax=ax)
    ax.axis("off")
    ax.set_position([0, 0, 1, 1])
    ax.set_xlim(-0.4, 3.8)
    ax.set_ylim(-2.1, 2.1)
    # plt.savefig("f_output/graph.png", format="png", dpi=240)
    plt.close()

    # build layererd graphs
    T = 5
    newfw, newfh = fw, (fh // 4 * 2) * T
    # layerG = nx.Graph()

    fig = plt.figure(figsize=(newfw, newfh))
    ax = fig.gca()
    for layer in range(T):
        posL = {n: (pos[n][0], pos[n][1] + layer * fh) for n in pos}
        ax.text(-0.5, layer * fh + 0.5, '(t={})'.format(layer))
        n = nx.draw_networkx_nodes(G, posL, ax=ax, node_color='white')
        n.set_edgecolor("blue")
        nx.draw_networkx_labels(G, posL, labels, ax=ax)
        nx.draw_networkx_edges(G, posL, ax=ax)

    # 0 -> 1 layer
    for l in range(1, T):
        p1 = {n: (pos[n][0], pos[n][1] + (l - 1) * fh) for n in pos}
        p2 = {n: (pos[n][0], pos[n][1] + l * fh) for n in pos}
        for u, v in G.edges():
            ax.plot([p1[u][0], p2[v][0]], [p1[u][1], p2[v][1]], 'r-', alpha=0.3)
            ax.plot([p1[v][0], p2[u][0]], [p1[v][1], p2[u][1]], 'b-', alpha=0.3)


    ax.axis("off")
    # ax.set_position([0, 0, 1, 1])
    # ax.set_xlim(-0.4, 3.8)
    # ax.set_ylim(-2.1, 2.1)
    plt.savefig("f_output/graph_T{}.png".format(T), format="png", dpi=240)
    plt.show()
    plt.close()


if __name__ == '__main__':
    main()
