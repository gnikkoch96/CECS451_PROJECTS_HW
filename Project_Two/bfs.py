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

import graph
import queue

# takes in the graph problem to search through
#use a q 
class BFS:
    def bfs(v):
        queue = []
        v.parent = v
        v.distance = 0
        queue.append('v')

        while not queue.empty():
            q = queue.pop()

            for neighbour in q.get_connections():
                if neighbour.parent == None:
                    neighbour.parent = v
                    neighbour.distance = q.distance + 1
                    queue.append(neighbour)






