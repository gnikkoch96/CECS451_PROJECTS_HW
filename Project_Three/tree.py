# -----------------------------------------------------------------------
#   Tree and Node Class
#   (c) 2021 Rishika Baranawl and Nikko Chan
#
#   Date: 08/02/2021
#   Name(s): Rishika Baranwal and Nikko Chan
#   Student ID: 016064033 (Nikko), 026354235 (Rishika)
#   E-Mail: Nikko.Chan@student.csulb.edu, rishika.baranwal@student.csulb.edu
#   Version: 1.0.0
# -----------------------------------------------------------------------

class Tree:
    def __init__(self):
        self.node_dict = {}
        self.num_node = 0
        self.root = None

    # adds a node while connecting current node (node_id) to a parent (parent_id)
    def add_node(self, node_id, parent_id):
        # if there are no nodes currently, then that means it is the root node
        if self.num_node == 0:
            parent = None
            new_v = Node(node_id, parent)
            self.root = new_v
        else:
            parent = self.node_dict[parent_id]
            new_v = Node(node_id, parent)
            parent.add_child(node_id, new_v)

        self.node_dict[node_id] = new_v
        self.num_node += 1

    def get_node(self, node_id):
        if node_id in self.node_dict:
            return self.node_dict[node_id]
        else:
            return None

    def get_nodes(self):
        return self.node_dict.keys()

    # is_prune is used to tell if we want to prune or not
    def minimax(self, state, depth, is_prune):
        # start with max first
        self.max_value(state, float('-inf'), float('+inf'), depth, is_prune)
        

    def max_value(self, state, a, b, depth, is_prune):
        if depth == 0:
            return state

        for child in state.get_children_nodes():
            a = max(a, self.min_value(child, a, b, depth - 1, is_prune))
            if a >= b:  # this is the cutoff point
                return a

        pass

    def min_value(self, state, alpha, beta, depth, is_prune):
        pass

    def dfs_util(self, root):
        for item in root.get_children_node():
            node = self.node_dict[item]
            if not node.visited:
                node.visited = True
                self.dfs_util(node)

        print(root.get_id()) # prints the node once it reaches the end
        return

    # depth-first search traversal
    def dfs_traversal(self):
        self.dfs_util(self.root)


class Node:

    # parent_id is null if it is the root node
    def __init__(self, node_id, parent):
        self.id = node_id
        self.parent = parent
        self.visited = False  # is used to prevent looping
        self.child_dict = {}  # stores a dictionary of all the children of this node (aka successors)

    def add_child(self, child_id, child_node):
        self.child_dict[child_id] = child_node

    def get_children_node(self):
        return self.child_dict.keys()

    def get_parent(self):
        return self.parent

    def get_id(self):
        return self.id
