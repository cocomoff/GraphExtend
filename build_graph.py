# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt

def example():
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
    return G, pos, labels


def main():
    G, pos, labels = example()
    T = 5
    # 0 -> 1 layer
    # for l in range(1, T):
    #     p1 = {n: (pos[n][0], pos[n][1] + (l - 1) * fh) for n in pos}
    #     p2 = {n: (pos[n][0], pos[n][1] + l * fh) for n in pos}


class LayerManager(object):
    def __init__(self, G, pos, labels, T):
        assert list(G.nodes()) == list(range(G.number_of_nodes()))
        self.G = G
        self.pos = pos
        self.labels = labels
        self.T = T
        self.setup()

    def setup(self):
        self.N = self.G.number_of_nodes()
        idlist = []
        id2info = {}
        for layer in range(self.T):
            for n in G.nodes():
                nid = n + layer * self.N
                idlist.append(nid)
                id2info[nid] = (n, layer)

        print(idlist)
        print(id2info)


if __name__ == '__main__':
    G, pos, labels = example()
    T = 5
    idm = LayerManager(G, pos, labels, T)
