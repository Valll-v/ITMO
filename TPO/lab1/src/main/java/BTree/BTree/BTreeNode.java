package BTree.BTree;

import java.util.ArrayList;

public class BTreeNode {
    public ArrayList<Integer> values;
    public ArrayList<BTreeNode> children;

    public BTreeNode() {
        this.values = new ArrayList<>();
        this.children = new ArrayList<>();
    }
}
