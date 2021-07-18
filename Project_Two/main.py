# -----------------------------------------------------------------------
#   Project 2: Maze Search
#   Description: Choosing a maze, we must utilize A*, BFS, and DFS to find the path from starting node to goal node
#   (c) 2021 Rishika Baranawl and Nikko Chan
#
#   Date: 07/20/2021
#   Name(s): Rishika Baranwal and Nikko Chan
#   Student ID: 016064033 (Nikko), 026354235 (Rishika)
#   E-Mail: Nikko.Chan@student.csulb.edu, rishika.baranwal@student.csulb.edu
#   Version: 1.0.0
# -----------------------------------------------------------------------
import graph
import gameboard
import csv


# Creates the Gameboard (Using a 2D Array)
gb = gameboard.GameBoard()
# row_p, col_p = gb.getStart()
# print(row_p, col_p)

# row_g, col_g = gb.getGoal()
# print(row_g, col_g)

# Creates the Graph of the Gameboard
g = graph.Graph()

# create a vertex for all chars on the maze
for row in range(len(gb.maze_to_array)):
    for column in range(len(gb.maze_to_array[row])):
        g.add_vertex(g.num_vertices, gb.maze_to_array[row][column])

# create vertex and add edges to all "_", ".", and "P"
for node_id in g.get_vertices():
    # Nikko: we can use modulus to see what column it is at so if we wanted to look up from 219 we would do 219%22 = 21
    # print(g.vert_dict[node_id].get_node())
    # print(g.vert_dict[node_id - (node_id % 22)].get_node())

    current_node = g.vert_dict[node_id].get_node()
    if current_node != '%':
        print("valid current node: ", current_node)
        print("valid current node_id: ", node_id)

        # check up
        # validate_value = node_id - (node_id % gb.get_col_count())
        validate_value = node_id - gb.get_col_count()
        print("validate value: ", validate_value)
        if validate_value >= 0:
            up_node_id = validate_value
            up_node = g.vert_dict[up_node_id].get_node()
            # print("id", up_node_id)
            # print("node:", up_node)
            if up_node != '%':
                g.add_edge(node_id, up_node_id)

g.graph_summery()