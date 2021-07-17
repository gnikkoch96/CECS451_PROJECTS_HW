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

# Creates the Gameboard (Using a 2D Array)
gb = gameboard.GameBoard()
print(gb.getStart())
print(gb.getGoal())

# Creates the Graph of the Gameboard
g = graph.Graph()

# create the nodes by adding an edge to them where the node is the node_counter
# for i in gb.maze_to_array:
#     for j in i:
#         if(j != %):
#             g.
