# -----------------------------------------------------------------------
#   Handles the creation of the tree based on the passed dataset
#   (c) 2021 Rishika Baranawl and Nikko Chan
#
#   Date: 08/04/2021
#   Name(s): Rishika Baranwal and Nikko Chan
#   Student ID: 016064033 (Nikko), 026354235 (Rishika)
#   E-Mail: Nikko.Chan@student.csulb.edu, rishika.baranwal@student.csulb.edu
#   Version: 1.0.0
# -----------------------------------------------------------------------

from tree import Tree
from tree import Node
import csv  # comma separated value


class DataTree:
    # dataset is a file of the dataset (csv format)
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        self.tree = None
        self.parse_dataset()

    def parse_dataset(self):
        self.tree = Tree()

        with open(self.dataset_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            line_count = 0
            for row in csv_reader:
                # NN: columns are read as row[i]
                if line_count == 0:  # initialize the root
                    root_parent = " "
                    # root_parent = row[1].replace(" ", "")  # removes the whitespace

                    adj_child_value = row[2].replace(" ", "")
                    root_node = adj_child_value[0:adj_child_value.find("=")]  # removes "=0" part into a substring
                    root_value = adj_child_value[adj_child_value.find("=") + 1: len(adj_child_value)]  # stores the value

                    self.tree.add_node(root_node, root_value, root_parent)  # child, parent
                else:  # parse everything else
                    adj_parent_value = row[1].replace(" ", "")
                    parent_node = adj_parent_value

                    for col in range(2, len(row)):
                        adj_child_value = row[col].replace(" ", "")

                        child_node = adj_child_value[0:adj_child_value.find("=")]
                        cn_value = adj_child_value[adj_child_value.find("=") + 1: len(row[col])]

                        # add values to the tree
                        self.tree.add_node(child_node, cn_value, parent_node)

                line_count += 1
