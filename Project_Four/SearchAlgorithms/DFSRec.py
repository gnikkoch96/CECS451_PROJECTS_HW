# -----------------------------------------------------------------------
#   Simulate DFS Algorithm
#   (c) 2021 Rishika Baranawl and Nikko Chan
#
#   Date: 08/10/2021
#   Name(s): Rishika Baranwal and Nikko Chan
#   Student ID: 016064033 (Nikko), 026354235 (Rishika)
#   E-Mail: Nikko.Chan@student.csulb.edu, rishika.baranwal@student.csulb.edu
#   Version: 1.0.0
# -----------------------------------------------------------------------

class DFSRec(object):
	
    def __init__(self, graph, size, start_node):

        self.graph = graph
        self.size = size
        self.start_node = start_node

    def DFS_util(self, s):
        
        s.set_visited(True)
        print (s.get_id())
        node = self.graph.get_vertex(s.get_id())
        for v in node.adjacent:
            n = self.graph.get_vertex(v.get_id())
            if n.get_visited() == False:
                self.DFS_util(n)

    def DFS_recursive(self):
        s_node = self.graph.get_vertex(self.start_node)
        self.DFS_util(s_node)
   
#------------------------[End of DFS class]----------------------------------------------------------------