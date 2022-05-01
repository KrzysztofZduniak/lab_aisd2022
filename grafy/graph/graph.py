from random import randint

class Graph:

    def nodes(self):
        raise NotImplementedError()

    def add_egde(self, v, w):
        raise NotImplementedError()

    def successors(self, v):
        raise NotImplementedError()

    def add_edges_from_list(self, l):
        raise NotImplementedError()

    def number_of_nodes(self):
        raise NotImplementedError()


class ListGraph(Graph):
    def __init__(self, n):
        self.n_and_e = [set() for _ in range(n)]

    def nodes(self):
        return list(range(len(self.n_and_e)))

    def add_egde(self, v, w):
        self.n_and_e[v].add(w)

    def successors(self, v):
        return self.n_and_e[v]

    def add_edges_from_list(self, l):
        for item in l:
            self.add_egde(*item)

    def number_of_nodes(self):
        return len(self.n_and_e)

class MatrixGraph(Graph):
    def __init__(self, n, directed=False):
        self.n_and_e = [[0]*n for _ in range(n)]
        self.directed = directed
        self.edge_count = 0
        self.size = n

    def nodes(self):
        return list(range(len(self.n_and_e)))

    def add_egde(self, v, w):
        if self.directed:
            self.edge_count += 1
            self.n_and_e[v][w] = 1
        else:
            value = randint(1, 1001)
            self.n_and_e[v][w] = value
            self.n_and_e[w][v] = value
            self.edge_count += 1


    def successors(self, v):
        s = []
        for i in range(len(self.n_and_e)):
            if self.n_and_e[v][i] == 1:
                s.append(i)
        return s
        #return [i for i, x in enumerate(self.n_and_e[v]) if x == 1]

    def add_edges_from_list(self, l):
        for item in l:
            self.add_egde(*item)

    def number_of_nodes(self):
        return len(self.n_and_e)

    def fulfilment(self):
        max_edge_count = (self.size-1)**2 / 2
        return self.edge_count / max_edge_count * 100

    def make_dag(self, pr):
        while self.fulfilment() < pr:
            i = randint(0, self.size-1)
            j = randint(i, self.size-1)
            print(i, j)
            while self.n_and_e[i][j] == 1:
                i = randint(0, self.size-1)
                j = randint(i, self.size-1)
            self.add_egde(i, j)
            edge_count += 1
