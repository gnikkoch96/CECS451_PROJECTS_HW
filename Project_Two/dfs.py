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

import queue


class DFS:
    # counts the max fringe value
    max_fringe_value = 0

    @staticmethod
    def dfs_util(v, visited, path):
        visited.add(v)

        # needs to let previous node know that it was the end, so this node should point back to the node it was
        # called and so forth
        if v.get_node() == '.':
            return True

        # checks the neighbours of this node
        for neighbour in v.get_connections():
            DFS.max_fringe_value += 1
            if neighbour not in visited:
                path.put(neighbour)
                found = DFS.dfs_util(neighbour, visited, path)

                # if the goal has been found, then keep returning v otherwise it will get removed
                if found:
                    return True
                else:  # remove it from queue if it doesn't find the result
                    path.get()

        return False

    @staticmethod
    # graph - used for search
    # gameboard - update the 2d array
    def depth_first(graph, gameboard):
        p_node = graph.vert_dict[graph.get_node('P')]

        # creates a visited hashset (prevents duplicates)
        visited = set()

        # path to goal (LIFO Queue)
        path = queue.LifoQueue()

        # should print to true if the goal has been found
        DFS.dfs_util(p_node, visited, path)

        list_path = []
        for element in list(path.queue):
            list_path.append(element.get_id())

        # Update gameboard
        path_cost = 0
        while not path.empty():
            node = path.get()
            path_cost = path_cost + 1
            row, col = node.get_location()
            gameboard.maze_to_array[row][col] = '.'

        print("Path Taken: ", list_path)
        print("Path Cost:", path_cost)
        print("Number of Nodes Expanded:", len(visited))
        print("Maximum Fringe:", DFS.max_fringe_value, "\n")
