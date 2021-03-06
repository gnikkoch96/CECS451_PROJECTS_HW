# -----------------------------------------------------------------------
#   Project 2: Maze Search
#   Description: Choosing a maze, we must utilize A*, BFS, and DFS to find the path from starting node to goal node
#   (c) 2021 Rishika Baranwal and Nikko Chan
#
#   Date: 07/20/2021
#   Name(s): Rishika Baranwal and Nikko Chan
#   Student ID: 016064033 (Nikko), 026354235 (Rishika)
#   E-Mail: Nikko.Chan@student.csulb.edu, rishika.baranwal@student.csulb.edu
#   Version: 1.0.0
# -----------------------------------------------------------------------
import graph
import gameboard
from bfs import BFS
from convert_to_file import Solution

# Functions
from dfs import DFS


# Creates the Graph of the Gameboard
def create_graph():
    gr = graph.Graph()

    # create a vertex for all chars on the maze using the num_vertices as the id for each vertex
    for row in range(len(gb.maze_to_array)):
        for column in range(len(gb.maze_to_array[row])):
            gr.add_vertex(gr.num_vertices, gb.maze_to_array[row][column], row, column)

    # create vertex and add edges to all "_", ".", and "P"
    for node_id in gr.get_vertices():
        current_node = gr.vert_dict[node_id].get_node()
        if current_node != '%':

            # check up
            validate_value = node_id - gb.get_col_count()
            if validate_value >= 0:
                up_node_id = validate_value
                up_node = gr.vert_dict[up_node_id].get_node()
                if up_node != '%':
                    gr.add_edge(node_id, up_node_id)

            # check right
            validate_value = node_id + 1
            if validate_value < gb.get_row_count() * gb.get_col_count():
                right_node_id = validate_value
                right_node = gr.vert_dict[right_node_id].get_node()
                if right_node != '%':
                    gr.add_edge(node_id, right_node_id)

            # check down
            validate_value = node_id + gb.get_col_count()
            if validate_value < gb.get_row_count() * gb.get_col_count():
                down_node_id = validate_value
                down_node = gr.vert_dict[down_node_id].get_node()
                if down_node != '%':
                    gr.add_edge(node_id, down_node_id)

            # check left
            validate_value = node_id - 1
            if validate_value >= 0:
                left_node_id = validate_value
                left_node = gr.vert_dict[left_node_id].get_node()
                if left_node != '%':
                    gr.add_edge(node_id, left_node_id)
    return gr

# Main

# Gameboard class is used to convert the maze file into a 2d array
gb = gameboard.GameBoard()

# Creates the graph
g = create_graph()

# Perform DFS on the Maze
print("Performing Depth-First Search---------------------")
DFS.depth_first(g, gb)
Solution.create_file(gb, gb.mazeName, "Depth-First Search")

# Perform BFS on the Maze
gb.reset_map() # resets the gameboard
print("Performing Breadth-First Search-------------------")
BFS.bfs(g, gb)
Solution.append_file(gb, gb.mazeName, "Breadth-First Search")





