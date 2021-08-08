
from Graph.Graph import Graph
from pathlib import Path

from SearchAlgorithms.DFSNodeColor import DFSNodeColor
from SearchAlgorithms.DFSRec import DFSRec

# Converting maze to graph

output_folder = Path("Output/")
data_folder = Path("Data/TextData/")

# contains the whole path to map.txt
data = data_folder / "map.txt"

g = Graph(data)
g.graph_build()
size = g.graph_length()

# solve the graph color puzzle
dfs = DFSNodeColor(g, size, g.get_popular_node())  # the most popular node will be chosen at the start (i.e. degree heuristics)
# dfs = DFSNodeColor(g, size, g.get_popular_node())  # the most popular node will be chosen at the start (i.e. degree heuristics)
dfs.DFS_recursive()

# print out the dfs path along with their color
# dfs_output = DFSRec(g, size, g.get_popular_node())
# dfs_output.DFS_recursive()

