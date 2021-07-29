# -----------------------------------------------------------------------
#   Perform Minimax or Alpha-Beta Pruning on a Tree
#   (c) 2021 Rishika Baranawl and Nikko Chan
#
#   Date: 08/04/2021
#   Name(s): Rishika Baranwal and Nikko Chan
#   Student ID: 016064033 (Nikko), 026354235 (Rishika)
#   E-Mail: Nikko.Chan@student.csulb.edu, rishika.baranwal@student.csulb.edu
#   Version: 1.0.0
# -----------------------------------------------------------------------


from convert_dataset_to_tree import DataTree

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # dataset_path = "dataset\\tree1.txt"
    dataset_path = "dataset\\practice_set.txt"
    dt = DataTree(dataset_path)

    root_node = dt.tree.root

    user_input = int(input("Which algorithm do you want to perform?\n1.Minimax\n2.Alpha-Beta Pruning\n3.Exit\nChoice:"))

    if user_input == 1: # perform minimax (w/out pruning)
        # for depth, you have to subtract by one because of computer indexing
        dt.tree.minimax(root_node, 2, False)

        # print out all the nodes along with their values
        for node_key in dt.tree.get_nodes():
            node = dt.tree.node_dict[node_key]
            print(node.get_id(), "[", node.get_value(), "]")

    elif user_input == 2: # perform alpha-beta pruning
        # for depth, you have to subtract by one because of computer indexing
        dt.tree.minimax(root_node, 2, True)

        # print out all the nodes along with their values and their pruned status
        for node_key in dt.tree.get_nodes():
            node = dt.tree.node_dict[node_key]
            print(node.get_id(), "[", node.get_value(), "], Pruned Status: ", node.pruned)
    else: # exit the program
        print("Exited Program...")
