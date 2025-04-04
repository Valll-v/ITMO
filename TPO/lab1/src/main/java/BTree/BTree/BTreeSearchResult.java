package BTree.BTree;

public class BTreeSearchResult {
	public Integer level;
	public Integer index;
	public BTreeNode node;

	public BTreeSearchResult(BTreeNode node, Integer level, Integer index) {
		this.node = node;
		this.level = level;
		this.index = index;
	}
}
