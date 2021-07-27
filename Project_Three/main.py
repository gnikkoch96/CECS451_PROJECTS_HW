

from convert_dataset_to_tree import DataTree

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dataset_path = "dataset\\tree1.txt"
    dt = DataTree(dataset_path)

    root_node = dt.tree.root

    # for depth, you have to subtract by one because of computer indexing
    dt.tree.minimax(root_node, 2, False)

