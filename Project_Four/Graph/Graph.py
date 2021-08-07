# ----------------------------------------------------------------------------------------


import pandas as pd
from Data.LoadData import LoadData


class Graph(object):
    """ Constructs a graph data structure. """

    def __init__(self, data_file_path=""):

        ld = LoadData(data_file_path)
        self.data = ld.LoadData_Pandas()
        self.columns_count = ld.ColumnsCount()
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def graph_length(self):
        return self.columns_count

    def graph_build(self):
        """ This method construct graph from a data file """
        # column count value is also the same as the row count
        for row in range(self.columns_count):
            self.add_vertex(row)  # the id is the row number of the node
            for column in range(self.columns_count):
                if self.data.loc[
                    row, column] != 0:  # checks to see if there is a connection between 'row' node and 'column' node (note: row and column are node_ids)
                    self.add_edge(row, column, self.data.loc[
                        row, column])  # if there is a connection then we take note of that in our graph

    def add_vertex(self, node):

        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):

        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost=0):

        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)

    # The line below will be enabled if the graph is not directed
    # self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def graph_summary(self):
        # v is vertices in our dictionary (not the ids that we would have gotten if we did vert_dict.keys())
        # w is the neighboring vertices to v
        print('( %s , %s, %3s, %s)' % ("Vertex ID", "Neighbor ID", "Weight", "Visited"))
        for v in self.vert_dict.values():
            for w in v.get_connections():
                vid = v.get_id()
                wid = w.get_id()
                visited = w.get_visited()
                print('( %s , %s, %3d, %s)' % (vid, wid, v.get_weight(w), visited))

        for v in self.vert_dict.values():
            print('g.vert_dict[%s]=%s' % (v.get_id(), self.vert_dict[v.get_id()]))

    def get_popular_node(self):  # returns the node that has the most connections
        # iterate through the vertex dictionary and return the vertex with the max node
        popular_node = None
        max_neighbors = 0
        for v in self.vert_dict.values():
            # we can just count the length of the get_connections() list
            if max_neighbors < len(v.get_connections()):
                max_neighbors = len(v.get_connections())
                popular_node = v

        return popular_node


# -------------------[End of class]-------------------------------------------------------

class Vertex:
    """ keeps a node information """

    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.visited = False
        self.color = None  # the color will be chosen during the DFS recursion
        self.domain = {0: 'red', 1: 'blue', 2: 'green'}  # starting domain of each node

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def set_visited(self, visited):
        self.visited = visited

    def get_visited(self):
        return self.visited

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]
