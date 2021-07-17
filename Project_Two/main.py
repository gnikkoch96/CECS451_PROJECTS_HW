import graph

# Main
if __name__ == '__main__':
    g = graph.Graph()

    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('s')

<<<<<<< Updated upstream
    g.add_edge('a', 'b', 1)
    g.add_edge('a', 'c', 2)
    g.add_edge('b', 'd', 4)
    g.add_edge('c', 'a', 3)
    g.add_edge('c', 'b', 9)
    g.add_edge('c', 'd', 2)
    g.add_edge('d', 's', 7)
    g.add_edge('d', 'b', 6)
    g.add_edge('s', 'a', 10)
    g.add_edge('s', 'c', 5)
    g.graph_summery();
=======
# create vertex and add edges to all "_", ".", and "P"
for row in range(len(gb.maze_to_array)):
    for column in range(len(gb.maze_to_array[row])):
        if gb.maze_to_array[row][column] != '%':
            # check up
            if (row - 1) >= 0:
                if gb.maze_to_array[row - 1][column] != '%':
                    g.add_edge(gb.maze_to_array[row][column], gb.maze_to_array[row - 1][column])

            #check down
            if (row + 1) < len(gb.maze_to_array):
                if gb.maze_to_array[row + 1][column] != '%':
                    g.add_edge(gb.maze_to_array[row][column], gb.maze_to_array[row + 1][column])

            #check left
            if (column - 1) >= 0:
                if gb.maze_to_array[row][column - 1] != '%':
                    g.add_edge(gb.maze_to_array[row][column], gb.maze_to_array[row + 1][column - 1])

            #check right
            if (column + 1) < len(gb.maze_to_array[row]):
                if gb.maze_to_array[row][column + 1] != '%':
                    g.add_edge(gb.maze_to_array[row][column], gb.maze_to_array[row][column + 1])

g.graph_summery()
>>>>>>> Stashed changes
