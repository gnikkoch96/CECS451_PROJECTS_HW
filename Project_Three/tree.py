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
    def add_node(self, node_id, node_value, parent_id):
        # if there are no nodes currently, then that means it is the root node
        if self.num_node == 0:
            parent = None
            new_v = Node(node_id, node_value, parent)
            self.root = new_v
        else:
            parent = self.node_dict[parent_id]
            new_v = Node(node_id, node_value, parent)
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

    # is_prune is used to tell if we want to prune or not (used in the last part)
    def minimax(self, current_node, depth, is_prune):
        # start with max first
        if is_prune:
            self.max_value_prune(current_node, float('-inf'), float('inf'), depth)
        else:
            self.max_value(current_node, depth)

    def max_value(self, current_node, depth):
        if depth == 0:
            return current_node

        maxEval = float('-inf')  # stores a negative infinity (anything is greater than negative infinity)

        for child in current_node.get_children_nodes():
            child_node = self.node_dict[child]

            e = self.min_value(child_node, depth - 1)
            print(child_node.get_id())
            print('Type e:', type(e))
            print("E:", e)
            maxEval = max(maxEval, e.get_value())


        print("Max Eval: ", maxEval)
        return maxEval

    def min_value(self, current_node, depth):
        if depth == 0:
            return current_node

        minEval = float('inf')  # stores a positive infinity (anything is less than positive infinity)

        for child in current_node.get_children_nodes():
            child_node = self.node_dict[child]

            e = self.max_value(child_node, depth - 1)
            print(child_node.get_id())
            print('Type e:', type(e))
            print("E:", e)
            minEval = min(minEval, e.get_value())

        print("Min Eval: ", minEval)
        return minEval

    # prune version of the max and min value functions
    def max_value_prune(self, current_node, a, b, depth):
        if depth == 0:
            return current_node

        for child in current_node.get_children_nodes():
            child_node = current_node.child_dict[child]
            a = max(a, self.min_value(child_node, a, b, depth - 1))
            print(a)
            if a >= b:  # this is the cutoff point
                return a
        return a

    def min_value_prune(self, current_node, a, b, depth):
        if depth == 0:
            return current_node

        for child in current_node.get_children_nodes():
            child_node = current_node.child_dict[child]
            b = min(b, self.max_value(child_node, a, b, depth - 1))
            print(b)
            if b <= a:
                return b
        return b

    def dfs_util(self, root):
        for item in root.get_children_nodes():
            node = self.node_dict[item]
            if not node.visited:
                node.visited = True
                self.dfs_util(node)

        print(root.get_id())  # prints the node once it reaches the end
        return

    # depth-first search traversal
    def dfs_traversal(self):
        self.dfs_util(self.root)


class Node:

    # parent_id is null if it is the root node
    # node_value represents the value of the node from the dataset
    def __init__(self, node_id, node_value, parent):
        self.id = node_id
        self.parent = parent
        self.value = float(node_value)
        self.visited = False  # is used to prevent looping
        self.child_dict = {}  # stores a dictionary of all the children of this node (aka successors)

    def add_child(self, child_id, child_node):
        self.child_dict[child_id] = child_node

    def get_children_nodes(self):
        return self.child_dict.keys()

    def get_parent(self):
        return self.parent

    def get_value(self):
        return self.value

    def get_id(self):
        return self.id
