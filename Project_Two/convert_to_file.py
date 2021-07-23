# -----------------------------------------------------------------------
#   Converts the Gameboard to a .txt file
#   (c) 2021 Rishika Baranawl and Nikko Chan
#
#   Date: 07/20/2021
#   Name(s): Rishika Baranwal and Nikko Chan
#   Student ID: 016064033 (Nikko), 026354235 (Rishika)
#   E-Mail: Nikko.Chan@student.csulb.edu, rishika.baranwal@student.csulb.edu
#   Version: 1.0.0
# -----------------------------------------------------------------------
import numpy as np

class Solution:
    @staticmethod
    def append_file(gameboard, filename, search_type):
        list = []
        list.append("--------------------" + search_type + "--------------------")
        for row in range(len(gameboard.maze_to_array)):
            str_row = ""
            for col in range(len(gameboard.maze_to_array[row])):
                str_row = str_row + gameboard.maze_to_array[row][col]
            list.append(str_row)

        Array = np.array(list)

        file = open(filename + ".txt", "a")

        # Saving the 2D array in a text file
        output_maze = ""
        for line in Array:
            file.write(line + "\n")
            output_maze += line + '\n'

        print(output_maze)



        file.close()

    @staticmethod
    # How to use: Solution.create_file(gameboard, filename) -> creates a .txt file
    def create_file(gameboard, filename, search_type):
        list = []
        list.append("--------------------" + search_type + "--------------------")
        for row in range(len(gameboard.maze_to_array)):
            str_row = ""
            for col in range(len(gameboard.maze_to_array[row])):
                str_row = str_row + gameboard.maze_to_array[row][col]
            list.append(str_row)

        Array = np.array(list)

        file = open(filename + ".txt", "w+")

        # Saving the 2D array in a text file
        output_maze = ""
        for line in Array:
            file.write(line + "\n")
            output_maze += line + '\n'

        print(output_maze)
        file.close()
