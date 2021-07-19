# -----------------------------------------------------------------------
#   Utilize Breadth First-Search to Find the Path from Point to Goal
#   (c) 2021 Rishika Baranawl and Nikko Chan
#
#   Date: 07/20/2021
#   Name(s): Rishika Baranwal and Nikko Chan
#   Student ID: 016064033 (Nikko), 026354235 (Rishika)
#   E-Mail: Nikko.Chan@student.csulb.edu, rishika.baranwal@student.csulb.edu
#   Version: 1.0.0
# -----------------------------------------------------------------------

import queue

class DFS:

    @staticmethod
    # graph - used for search
    # gameboard - update the 2d array
    def depth_first(graph, gameboard):
        # fringe queue (LIFO)
        fringe = queue.LifoQueue()

        # first node to explore is the start node
        fringe.put(graph.vert_dict[graph.get_node('P')])

        # creates a visited hashset (prevents duplicates)
        visited = set()

        # path to goal (hash map)
        path = {}


        # visit each node possible from P
        while fringe.not_empty:
            node = fringe.get()

            if node.get_node() == '.':
                return path

            if node not in visited:
                visited.add(node)
                
                # add adjcent nodes to fringe
                for next in node.get_connections():
                    fringe.put(next)
                    path[next] = node






