

from convert_dataset_to_tree import DataTree

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dataset_path = "dataset\\tree1.txt"
    tree = DataTree(dataset_path)
    tree.tree.dfs_traversal()
