# Graph Class
class Graph(object):  # Nikko Notes (NN): object is inherited (remove all NN when submitting)
    # NN: self is used to refer to instance properties
    def __init__(self):  # NN: _init_ is kind of like a constructor
        self.vert_dict = {}
        self.num_vertices = 0

    def add_vertex(self, node):
        new_v = Vertex(node)
        self.vert_dict[node] = new_v  # NN: key = node , value = new_v
        self.num_vertices = self.num_vertices + 1

    def add_edge(self, from_edge, to_edge, weight):
        # if it isn't currenlty on the dictionary, then add it
        if from_edge not in self.vert_dict:
            self.add_vertex(from_edge)

        if to_edge not in self.vert_dict:
            self.add_vertex(to_edge)

        # add the neighbors for both from_edge and to_edge
        self.vert_dict[from_edge].add_neighbour(self.vert_dict[to_edge], weight)
        # self.vert_dict[to_edge].add_neighbour(self.vert_dict[from_edge], weight)

    def get_vertices(self):
        return self.vert_dict.keys()  # returns all keys objects as an array

    def graph_summery(self):
        for n in self.get_vertices():
            # NN: n is the str key that points to the actual vertex object
            vertex_n = self.vert_dict[n]
            for v in vertex_n.get_connections():
                # print(type(v))
                print(n, '->', v, ' : ', vertex_n.get_weight(v))


class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    # returns the node id when converted to string
    def __str__(self):
        return self.get_id()

    # returns the adjacent nodes
    def get_connections(self):
        return self.adjacent.keys()

    def add_neighbour(self, objNeighbour, weight):
        # NN: appends the objNeighbour to the adjacent list if it doesn't already exist in the dictionary
        self.adjacent[objNeighbour] = weight

    def get_id(self):
        return self.id

    def get_weight(self, neighbour):
        return self.adjacent[neighbour]