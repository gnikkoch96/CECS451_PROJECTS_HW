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
    dataset_path = "dataset\\tree2.txt"
    # dataset_path = "dataset\\practice_set.txt"
    dt = DataTree(dataset_path)
    depth = 4  # place the depth value here (remember that tree1 and tree2 have different depths i.e. put 2 for tree1 and 4 for tree 2)
    root_node = dt.tree.root

    user_input = 0
    while user_input < 3:
        user_input = int(input("\nWhich algorithm do you want to perform?\n1.Minimax\n2.Alpha-Beta Pruning\n3.Exit\nChoice: "))

        if user_input == 1: # perform minimax (w/out pruning)
            # for depth, you have to subtract by one because of computer indexing
            dt.tree.minimax(root_node, depth, False)

            # print out all the nodes along with their values
            for node_key in dt.tree.get_nodes():
                node = dt.tree.node_dict[node_key]
                print(node.get_id(), "[", node.get_value(), "]")

        elif user_input == 2: # perform alpha-beta pruning
            # for depth, you have to subtract by one because of computer indexing
            dt.tree.minimax(root_node, depth, True)

            # print out all the nodes along with their values and their pruned status
            for node_key in dt.tree.get_nodes():
                node = dt.tree.node_dict[node_key]
                print(node.get_id(), "(", node.value, "), [", node.alpha, ',', node.beta, "], Pruned Status: ", node.pruned)
        else: # exit the program
            print("Exited Program...")
