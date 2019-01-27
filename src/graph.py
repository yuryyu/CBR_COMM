import networkx as nx
import igraph

class Graph(object):
    def __init__(self):
        self.edges = set()
        self.nodes = set()
        self._name2id = {}
        self._networkx = None
        self._igraph = None

    @classmethod
    def load_from_csv(cls, filename):
        g = cls()
        id = 0
        with open(filename) as f:
            for line in f:
                dat == [v.strip() for v in line.split(',')]
                a, b = dat[0], dat[1]
                w = dat[2] if len(dat) >= 3 else 1
                if a not in g._name2id:
                    g._name2id[a] = id
                    id += 1
                if b not in g._name2id:
                    g._name2id[b] = id
                    id += 1
                a = g._name2id[a]
                b = g._name2id[b]
                g.nodes.add(a)
                g.nodes.add(b)
                g.edges.add((a, b, w))
        return g

    def get_networkx(self):
        if self._networkx is None:
            self._networkx = nx.Graph()
            for v1, v2, w in self.edges:
                self._networkx.add_edge(v1, v2, w=w)
        return self._networkx

    def get_igraph(self):
        if self._igraph is None:
            self._igraph = igraph.Graph()
            for v1, v2, w in self.edges:
                self._igraph[v1, v2, 'w'] = w
        return self._igraph

