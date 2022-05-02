class Graph:

    def nodes(self):
        raise NotImplementedError()

    def add_edge(self, v, w, weight=1):
        raise NotImplementedError()

    def successors(self, v):
        raise NotImplementedError()

    def add_edges_from_list(self, l):
        raise NotImplementedError()

    def number_of_nodes(self):
        raise NotImplementedError()

    def get_weight(self, v, w):
        raise NotImplementedError()


class ListGraph(Graph):
    def __init__(self, n, directed=False):
        self.n_and_e = [{} for _ in range(n)]
        self.directed = directed
        self.edge_count = 0
        self.size = n

    def nodes(self):
        return range(self.size)

    def add_edge(self, v, w, weight=1):
        if w in self.n_and_e[v]:
            raise RuntimeError("Added already existing edge")  # Just in case
        if self.directed:
            self.edge_count += 1
            self.n_and_e[v][w] = weight
        else:
            self.n_and_e[v][w] = weight
            self.n_and_e[w][v] = weight
            self.edge_count += 1

    def successors(self, v):
        return self.n_and_e[v].keys()

    def add_edges_from_list(self, l):
        for item in l:
            self.add_edge(*item)

    def number_of_nodes(self):
        return len(self.n_and_e)

    def get_weight(self, v, w):
        if w in self.n_and_e[v]:
            return self.n_and_e[v][w]
        else:
            return 0


class MatrixGraph(Graph):
    def __init__(self, n, directed=False):
        self.n_and_e = [[0]*n for _ in range(n)]
        self.directed = directed
        self.edge_count = 0
        self.size = n

    def nodes(self):
        return range(self.size)

    def add_edge(self, v, w, weight=1):
        if self.n_and_e[v][w] != 0:
            raise RuntimeError("Added already existing edge")  # Just in case
        if self.directed:
            self.edge_count += 1
            self.n_and_e[v][w] = weight
        else:
            self.n_and_e[v][w] = weight
            self.n_and_e[w][v] = weight
            self.edge_count += 1

    def successors(self, v):
        s = []
        for i in range(len(self.n_and_e)):
            if self.n_and_e[v][i] != 0:
                s.append(i)
        return s
        # return [i for i, x in enumerate(self.n_and_e[v]) if x == 1]

    def add_edges_from_list(self, l):
        for item in l:
            self.add_edge(*item)

    def number_of_nodes(self):
        return self.size

    def get_weight(self, v, w):
        return self.n_and_e[v][w]
