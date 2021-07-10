# -----------------------------------------------------------------------
#   Constructs a graph data structure
#   (c) 2021 Rishika Baranawl and Nikko Chan
#
#   Date: 07/12/2021
#   Name(s): Rishika Baranwal and Nikko Chan
#   Student ID: 016064033 (Nikko), 026354235 (Rishika)
#   E-Mail: Nikko.Chan@student.csulb.edu, rishika.baranwal@student.csulb.edu
#   Version:
# -----------------------------------------------------------------------

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


# Main
if __name__ == '__main__':
    g = Graph()

    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('s')

    g.add_edge('a', 'b', 1)
    g.add_edge('a', 'c', 2)
    g.add_edge('b', 'd', 4)
    g.add_edge('c', 'a', 3)
    g.add_edge('c', 'b', 9)
    g.add_edge('c', 'd', 2)
    g.add_edge('d', 's', 7)
    g.add_edge('d', 'b', 6)
    g.add_edge('s', 'a', 10)
    g.add_edge('s', 'c', 5)
    g.graph_summery()






