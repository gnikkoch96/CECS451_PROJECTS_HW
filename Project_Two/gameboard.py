# GameBoard class is used to convert the layout file into a 2D array
class GameBoard(object):
    def __init__(self):
        # User chooses which maze they want to do
        self.pathToMaze = None
        userInputMaze = int(input("Choose Layout: \n1.Small Maze\n2.Medium Maze\n3.Big Maze\nChoice: "))
        print(self.userInputMaze == 1)
        if self.userInputMaze == 1:
            self.pathToMaze = open("mazes\\smallMaze.lay", "r")
        elif self.userInputMaze == 2:
            self.pathToMaze = open("mazes\\mediumMaze.lay", "r")
        else:
            self.pathToMaze = open("mazes\\bigMaze.lay", "r")

        self.gameBoard2DArray = self.convertMazeto2D()

    def convertMazeto2D(self):
        
        return 2


    # Gets the Location of the Starting Node
    def getStart(self):
        pass

    # Gets the Location of the Goal Node
    def getGoal(self):
        pass

