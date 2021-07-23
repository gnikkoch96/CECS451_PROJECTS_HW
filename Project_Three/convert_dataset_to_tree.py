# -----------------------------------------------------------------------
#   Handles the creation of the tree based on the passed dataset
#   (c) 2021 Rishika Baranawl and Nikko Chan
#
#   Date: 08/02/2021
#   Name(s): Rishika Baranwal and Nikko Chan
#   Student ID: 016064033 (Nikko), 026354235 (Rishika)
#   E-Mail: Nikko.Chan@student.csulb.edu, rishika.baranwal@student.csulb.edu
#   Version: 1.0.0
# -----------------------------------------------------------------------

from tree import Tree
from tree import Node
import csv # comma separated value

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
                # columns are read as row[i] where i is the ith column while row represents the line from the dataset
                if line_count == 0: # initialize the root (because it has different column counts)
                    # print("Label:", row[0])
                    # print("Parent:", row[1])
                    # print("Children", row[2])
                    # removes the whitespace
                    self.tree.add_node(row[2].replace(" ", ""), row[1].replace(" ", "")) # child, parent
                else:
                    # print("Label:", row[0])
                    # print("Parent:", row[1])
                    # print("Children #1:", row[2])
                    # print("Children #2:", row[3])
                    # print("Children #3:", row[4])
                    self.tree.add_node(row[2].replace(" ", ""), row[1])
                    self.tree.add_node(row[3].replace(" ", ""), row[1])
                    self.tree.add_node(row[4].replace(" ", ""), row[1])



