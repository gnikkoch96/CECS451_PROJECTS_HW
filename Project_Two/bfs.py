# -----------------------------------------------------------------------
#   Utilize Breadth First-Search to Find the Path from Point to Goal
#   (c) 2021 Rishika Baranwal and Nikko Chan
#
#   Date: 07/20/2021
#   Name(s): Rishika Baranwal and Nikko Chan
#   Student ID: 016064033 (Nikko), 026354235 (Rishika)
#   E-Mail: Nikko.Chan@student.csulb.edu, rishika.baranwal@student.csulb.edu
#   Version: 1.0.0
# -----------------------------------------------------------------------

import graph
import queue


class BFS:

    @staticmethod
    def bfs(graph, gameboard):
        # frontier/fringe (FIFO)
        fringe = queue.Queue()

        # p_node is the first node
        p_node = graph.vert_dict[graph.get_node('P')]
        p_node.parent = ''
        fringe.put(p_node)

        # creates a visited hashset (prevents duplicates)
        visited = set()

        # path to goal (LIFO Queue)
        path = queue.LifoQueue()

        max_fringe_value = 0

        # perform bfs
        found = False  # used to tell if the solution was found or not
        while not fringe.empty():
            if fringe.__sizeof__() > max_fringe_value:
                max_fringe_value = fringe.__sizeof__()

            node = fringe.get()

            if node.get_node() == '.':  # goal node
                found = True

            if found:  # go from goal -> parent -> parent and etc... until the start node is reached
                while node.parent != '':  # start goal should have None
                    path.put(node)
                    node = node.parent
                    # print(node.get_id(), " parent: ", node.parent)
                break

            else:
                if node not in visited:
                    visited.add(node)

                    for neighbor in node.get_connections():
                        if neighbor.parent is None:
                            neighbor.parent = node
                            fringe.put(neighbor)

        # stores the path
        list_path = []
        for element in list(path.queue):
            list_path.append(element.get_id())
        list_path.append(graph.vert_dict[graph.get_node('P')].get_id())
        list_path.reverse()

        # Update gameboard
        path_cost = 1 # including the cost from the initial node to the second node
        while not path.empty():
            node = path.get()
            path_cost = path_cost + 1
            row, col = node.get_location()
            gameboard.maze_to_array[row][col] = '.'


        # output
        print("Path Taken: ", list_path)
        print("Path Cost:", path_cost)
        print("Number of Nodes Expanded:", len(visited))
        print("Maximum Fringe:", max_fringe_value, "\n")
