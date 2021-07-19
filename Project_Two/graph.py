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
        self.vert_dict = {}  # example: key = 1, value = " "
        self.num_vertices = 0  # this will be the id for each node since repeating characters are possible

    # id was added to give same characters a unique identifier
    def add_vertex(self, id, node, row, col):
        new_v = Vertex(id, node, row, col)
        self.vert_dict[id] = new_v  # NN: key = id , value = new_v
        self.num_vertices = self.num_vertices + 1

    def add_edge(self, from_edge, to_edge, weight=1):
        # if it isn't currently on the dictionary, then add it

        if from_edge not in self.vert_dict:
            print("Error: From_Edge does not exist")

        if to_edge not in self.vert_dict:
            print("Error: To_Edge does not exist")

        # add the neighbors for both from_edge and to_edge
        self.vert_dict[from_edge].add_neighbour(self.vert_dict[to_edge], weight)

    def get_vertices(self):
        return self.vert_dict.keys()  # returns all keys objects as an array

    def get_node(self, node_value):
        for node_id in self.vert_dict:
            current_char = self.vert_dict[node_id].get_node()
            if current_char == node_value:
                return node_id

    def graph_summery(self):
        for n in self.get_vertices():
            vertex_n = self.vert_dict[n]
            for v in vertex_n.get_connections():
                print(vertex_n.get_node(), '->', v.get_node(), ' : ', vertex_n.get_weight(v))


class Vertex:
    def __init__(self, id, node, row, col):
        self.id = id
        self.node = node
        self.adjacent = {}
        self.row_location = row
        self.col_location = col

    # returns the node id when converted to string
    def __str__(self):
        return str(self.id)

    # returns the adjacent nodes
    def get_connections(self):
        return self.adjacent.keys()

    # default weight is 1
    def add_neighbour(self, objNeighbour, weight=1):
        self.adjacent[objNeighbour] = weight

    # returns iterable of row and column location values
    def get_location(self):
        return self.row_location, self.col_location

    def get_id(self):
        return self.id

    def get_node(self):
        return self.node

    def get_weight(self, neighbour):
        return self.adjacent[neighbour]
