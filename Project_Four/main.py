
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

dfs = DFSNodeColor(g, size, g.get_popular_node())  # the most popular node will be chosen at the start (i.e. degree heuristics)
dfs.DFS_recursive()

# g.graph_summary()
# dfs = DFSRec(g, size, 2)
# dfs.DFS_recursive()
