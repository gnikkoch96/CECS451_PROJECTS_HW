# -----------------------------------------------------------------------
#   Creates the Maze as a 2D Data Structure
#   (c) 2021 Rishika Baranawl and Nikko Chan
#
#   Date: 07/20/2021
#   Name(s): Rishika Baranwal and Nikko Chan
#   Student ID: 016064033 (Nikko), 026354235 (Rishika)
#   E-Mail: Nikko.Chan@student.csulb.edu, rishika.baranwal@student.csulb.edu
#   Version: 1.0.0
# -----------------------------------------------------------------------

# GameBoard class is used to convert the layout file into a 2D array
class GameBoard(object):
    def __init__(self):
        # User chooses which maze they want to do
        self.mazeFile = None
        self.maze_array = None
        self.load_map()
        self.maze_to_array = self.create_2d_array()
        self.store_maze_2D()
        print(self.maze_to_array)
        self.mazeFile.close()

    # loads the map of the user's choice
    def load_map(self):
        userInputMaze = int(input("Choose Layout: \n1.Small Maze\n2.Medium Maze\n3.Big Maze\nChoice: "))
        if userInputMaze == 1:
            self.mazeFile = open("mazes\\smallMaze.lay", "r")
        elif userInputMaze == 2:
            self.mazeFile = open("mazes\\mediumMaze.lay", "r")
        else:
            self.mazeFile = open("mazes\\bigMaze.lay", "r")

    # stores the maze in a 2D data structure
    def store_maze_2D(self):
        count_row = 0
        count_col = 0
        self.mazeFile.seek(0) # reset the file read after
        for line in self.mazeFile.readlines():
            for char in line:
                if count_col < len(self.maze_to_array[count_row]):
                    self.maze_to_array[count_row][count_col] = char # store the char at location [count_row][count_col]
                    count_col = count_col + 1
            count_row = count_row + 1
            count_col = 0

    # returns a 2d array of count_row x count_col
    def create_2d_array(self):
        count_row = 0
        count_col = 0
        self.mazeFile.seek(0) # reset the file read after
        for i in self.mazeFile.readlines():
            count_row = count_row + 1
            count_col = 0
            for j in i:
                count_col = count_col + 1
        print(count_row, " x ", count_col)
        return [[0 for col in range(count_col)] for row in range(count_row)]

    # gets the Location of the Starting Node
    def getStart(self):
        pass

    # gets the Location of the Goal Node
    def getGoal(self):
        pass

