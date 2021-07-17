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
# print(gb.getStart())
# print(gb.getGoal())

# Creates the Graph of the Gameboard
g = graph.Graph()

# # create vertex and add edges to all "_", ".", and "P"
# for row in range(len(gb.maze_to_array)):
#     for column in range(len(gb.maze_to_array[row])):
#         if gb.maze_to_array[row][column] != '%':
#             # check up
#             if (row - 1) >= 0:
#                 if gb.maze_to_array[row - 1][column] != '%':
#
#             #check down
#
#             #check left
#
#             #check right
