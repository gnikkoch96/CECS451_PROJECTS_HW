import graph

# Main
if __name__ == '__main__':
    g = graph.Graph()

    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('s')

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