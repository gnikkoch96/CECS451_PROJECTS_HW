# -----------------------------------------------------------------------
#   Constructs a graph data structure
#   (c) 2021 Rishika Baranawl and Nikko Chan
#
#   Date: 07/20/2021
#   Name(s): Rishika Baranwal and Nikko Chan
#   Student ID: 016064033 (Nikko), 026354235 (Rishika)
#   E-Mail: Nikko.Chan@student.csulb.edu, rishika.baranwal@student.csulb.edu
#   Version: 1.0.0
# -----------------------------------------------------------------------


# Graph Class
class Graph(object):
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    # id was added to give same characters a unique identifier
    def add_vertex(self, node):
        new_v = Vertex(node)
        self.vert_dict[node] = new_v  # NN: key = id , value = new_v
        self.num_vertices = self.num_vertices + 1

    def add_edge(self, from_edge, to_edge, weight=1):
        # if it isn't currently on the dictionary, then add it
        if from_edge not in self.vert_dict:
            self.add_vertex(from_edge)

        if to_edge not in self.vert_dict:
            self.add_vertex(to_edge)

        # add the neighbors for both from_edge and to_edge
        self.vert_dict[from_edge].add_neighbour(self.vert_dict[to_edge], weight)

    def get_vertices(self):
        return self.vert_dict.keys()  # returns all keys objects as an array

    def graph_summery(self):
        for n in self.get_vertices():
            vertex_n = self.vert_dict[n]
            for v in vertex_n.get_connections():
                print(n, '->', v, ' : ', vertex_n.get_weight(v))


class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    # returns the node id when converted to string
    def __str__(self):
        return self.id

    # returns the adjacent nodes
    def get_connections(self):
        return self.adjacent.keys()

    # default weight is 1
    def add_neighbour(self, objNeighbour, weight=1):
        # NN: appends the objNeighbour to the adjacent list if it doesn't already exist in the dictionary
        self.adjacent[objNeighbour] = weight

    def get_id(self):
        return self.id

    def get_weight(self, neighbour):
        return self.adjacent[neighbour]