# -----------------------------------------------------------------------
#
#   (c) 2021 Rishika Baranawl and Nikko Chan
#
#   Date: 08/10/2021
#   Name(s): Rishika Baranwal and Nikko Chan
#   Student ID: 016064033 (Nikko), 026354235 (Rishika)
#   E-Mail: Nikko.Chan@student.csulb.edu, rishika.baranwal@student.csulb.edu
#   Version: 1.0.0
# -----------------------------------------------------------------------

class DFSNodeColor(object):

    def __init__(self, graph, size, start_node):
        self.graph = graph
        self.size = size
        self.start_node = start_node

    def DFS_util(self, s):
        s.set_visited(True)

        print("Start Domain:", s.get_id(), ' :', s.domain)
        # set the color of the node
        s.color = s.domain.popitem()  # stores a tuple of <id, value> (which is iterable) (example: (0, 'red'))

        # update domain to the rest of the neighbors (to make it arc-consistent)
        self.mac(s)

        # output
        print(s.get_id(), '->', s.color[1])

        for v in s.adjacent:
            n = self.graph.get_vertex(v.get_id())
            if not n.get_visited():
                self.DFS_util(n)

    def DFS_recursive(self):
        self.DFS_util(self.start_node)

    def mac(self, v):  # used to update the vertex's connected node's domain after choosing a color
        print("Vertex:", v.get_id(), "-> ", v.color[1])
        for node in v.get_connections():
            print(node.get_id(), " Domain (Before):", node.domain)
            if v.color[0] in node.domain.keys():  # checks to see if the color is in the domain or not
                del node.domain[v.color[0]]

            print(node.get_id(), " Domain (After):", node.domain)


    # ------------------------[End of DFS class]----------------------------------------------------------------
