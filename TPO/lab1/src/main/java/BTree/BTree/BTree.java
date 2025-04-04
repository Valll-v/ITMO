package BTree.BTree;

import java.util.ArrayList;

public class BTree {
	
	public BTreeNode root;

	public BTree() {
		this.root = new BTreeNode();
	}
	
	private ArrayList<Integer> insertIntoList(Integer value, ArrayList<Integer> list) {
		for (int i = 0; i < list.size(); i++) {
			if (value <= list.get(i)) {
				ArrayList<Integer> newList = new ArrayList<Integer>();
				for (int t = 0; t < i; t++) {
					newList.add(list.get(t));
				}
				newList.add(value);
				for (int t = i; t < list.size(); t++) {
					newList.add(list.get(t));
				}
				return newList;
			}
		}
		list.add(value);
		return list;
	}
	
	public void insert(int value) {
		this.root = this.insertFull(value, this.root);
	}
	
	private BTreeNode insertFull(int value, BTreeNode current) {
		if (!current.children.isEmpty()) {
			for (int i = 0; i < current.values.size(); i++) {
				if (current.values.get(i) > value) {
					BTreeNode child = this.insertFull(value, current.children.get(i));
					current.children.set(i, child);
					return current;
				}
			}
			BTreeNode child = this.insertFull(value, current.children.get(current.children.size() - 1));
			current.children.set(current.children.size() - 1, child);
			return current;
		} else {
			current.values = this.insertIntoList(value, current.values);
			if (current.values.size() == 7) {
				ArrayList<Integer> newValues = new ArrayList<Integer>();
				newValues.add(current.values.get(3));
				BTreeNode newChild1 = new BTreeNode();
				BTreeNode newChild2 = new BTreeNode();
				for (int i = 0; i < 3; i++) {
					newChild1.values.add(current.values.get(i));
				}
				for (int i = 4; i < 7; i++) {
					newChild2.values.add(current.values.get(i));
				}
				current.children.add(newChild1);
				current.children.add(newChild2);
				current.values = newValues;
			}
		}
		return current;
	}
	
	public BTreeSearchResult search(int value) {
		return this.searchFull(value, root, 1);
	}
	
	private BTreeSearchResult searchFull(int value, BTreeNode current, int level) {
		for (int i = 0; i < current.values.size(); i++) {
			if (value == current.values.get(i)) {
				return new BTreeSearchResult(current, i, level);
			}
			if (value < current.values.get(i)) {
				if (current.children.size() > i) {
					return this.searchFull(value, current.children.get(i), level + 1);
				} else {
					return null;
				}
			}
		}
		if (!current.children.isEmpty()) {
			return this.searchFull(value, current.children.get(current.children.size() - 1), level + 1);
		}
		return null;
	}
}