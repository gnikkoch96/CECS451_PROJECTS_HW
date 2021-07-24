

from convert_dataset_to_tree import DataTree

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dataset_path = "dataset\\tree1.txt"
    dt = DataTree(dataset_path)
    print(dt.tree.node_dict)
    # tree.tree.dfs_traversal()
