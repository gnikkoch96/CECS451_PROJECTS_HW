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
                    root_parent = row[1].replace(" ", "")  # removes the whitespace

                    root_a = row[2].replace(" ", "")[0:row[2].find("=") - 1]  # removes "=0" part into a substring
                    root_value = row[2].replace(" ", "")[row[2].find("="): len(row[2])] # stores the value

                    self.tree.add_node(root_a, root_value, root_parent)  # child, parent
                else:
                    parent_node = row[1].replace(" ", "")[0:row[2].find("=") - 1]

                    child_node1 = row[2].replace(" ", "")[0:row[2].find("=") - 1]
                    cn1_value = row[2].replace(" ", "")[row[2].find("="): len(row[2])]

                    child_node2 = row[3].replace(" ", "")[0:row[2].find("=") - 1]
                    cn2_value = row[3].replace(" ", "")[row[3].find("="): len(row[3])]

                    child_node3 = row[4].replace(" ", "")[0:row[2].find("=") - 1]
                    cn3_value = row[4].replace(" ", "")[row[4].find("="): len(row[4])]

                    # add values
                    self.tree.add_node(child_node1, cn1_value, parent_node)
                    self.tree.add_node(child_node2, cn2_value, parent_node)
                    self.tree.add_node(child_node3, cn3_value, parent_node)

                line_count += 1
