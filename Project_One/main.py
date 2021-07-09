# -----------------------------------------------------------------------
#   Constructs a graph data structure
#   (c) 2021 Rishika Baranawl and Nikko Chan
#
#   Date: 07/12/2021
#   Name(s): Rishika Baranawl and Nikko Chan
#   Student ID: 016064033 (Nikko)
#   E-Mail: Nikko.Chan@student.csulb.edu
#   Version:
# -----------------------------------------------------------------------

# Graph Class
class Graph(object): # Nikko Notes (NN): object is inherited (remove all NN when submitting)
    # NN: self is used to refer to instance properties
    def _init_(self): # NN: _init_ is kind of like a constructor
        self.vert_dict = {}
        self.num_vertices = 0

    def add_vertex(self, node):
        new_v = Vertex(node)
        self.vert_dict[node] = new_v # NN: key = node , value = new_v
        self.num_vertices = self.num_vertices + 1

    def get_vertex(self, node):



# Vertex Class (NN: represents a single node on the graph)
class Vertex:






