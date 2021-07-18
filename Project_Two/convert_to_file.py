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
    def create_file(gameboard):
        list = []
        for row in range(len(gameboard.maze_to_array)):
            str_row = ""
            for col in range(len(gameboard.maze_to_array[row])):
                str_row = str_row + gameboard.maze_to_array[row][col]
            list.append(str_row)

        print(list)

        Array = np.array(list)

        # Displaying the array
        print('Array:\n', Array)
        file = open("file2.txt", "w+")

        # Saving the 2D array in a text file
        for line in Array:
            file.write(line + "\n")

        file.close()

        # Displaying the contents of the text file
        file = open("file2.txt", "r")
        content = file.read()

        print("\nContent in file2.txt:\n", content)
        file.close()
