package BTree;

import java.util.ArrayList;
import java.util.Arrays;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestInstance;
import org.junit.jupiter.api.TestInstance.Lifecycle;
import BTree.BTree.BTree;
import BTree.BTree.BTreeNode;
import BTree.BTree.BTreeSearchResult;


@TestInstance(Lifecycle.PER_CLASS)
class BTreeTest {

	private BTree btree;
	
	@BeforeAll
	public void setUp() {
		this.btree = new BTree();
		this.btree.root = new BTreeNode();
	}
	
	@BeforeEach
	public void clear() {
		this.btree.root = new BTreeNode();
	}

    @Test
    void testInsertValue() {
    	ArrayList<Integer> list;
    	
    	list = new ArrayList<Integer>(Arrays.asList(2));
        this.btree.insert(2);
        Assertions.assertEquals(list, this.btree.root.values);
        
        list = new ArrayList<Integer>(Arrays.asList(1, 2));
        this.btree.insert(1);
        Assertions.assertEquals(list, this.btree.root.values);
        
        list = new ArrayList<Integer>(Arrays.asList(1, 2, 3));
        this.btree.insert(3);
        Assertions.assertEquals(list, this.btree.root.values);
        
        list = new ArrayList<Integer>(Arrays.asList(1, 2, 2, 3));
        this.btree.insert(2);
        Assertions.assertEquals(list, this.btree.root.values);
    }
    
    @Test
    void testSplitChild() {
    	ArrayList<Integer> list;
    	
    	list = new ArrayList<Integer>(Arrays.asList(1, 2, 3, 4, 5, 6));
        this.btree.root.values = list;
        this.btree.insert(3);
        
        Assertions.assertEquals(new ArrayList<Integer>(Arrays.asList(3)), this.btree.root.values);
        Assertions.assertEquals(new ArrayList<Integer>(Arrays.asList(1, 2, 3)), this.btree.root.children.get(0).values);
        Assertions.assertEquals(new ArrayList<Integer>(Arrays.asList(4, 5, 6)), this.btree.root.children.get(1).values);
    }
    
    @Test
    void testInsertChild() {
    	ArrayList<Integer> list;
    	
    	list = new ArrayList<Integer>(Arrays.asList(1, 2, 3, 4, 5, 6));
        this.btree.root.values = list;
        this.btree.insert(3);
        this.btree.insert(5);
        this.btree.insert(8);
        this.btree.insert(0);
        
        Assertions.assertEquals(new ArrayList<Integer>(Arrays.asList(4, 5, 5, 6, 8)), this.btree.root.children.get(1).values);
        Assertions.assertEquals(new ArrayList<Integer>(Arrays.asList(0, 1, 2, 3)), this.btree.root.children.get(0).values);
    }
    
    @Test
    void testSearch() {
    	ArrayList<Integer> list;
    	
    	list = new ArrayList<Integer>(Arrays.asList(1, 2, 3, 4, 5, 6));
        this.btree.root.values = list;
        this.btree.insert(3);
        
        BTreeSearchResult rootResult = new BTreeSearchResult(this.btree.root, 0, 1);
        BTreeSearchResult childResult = new BTreeSearchResult(this.btree.root.children.get(0), 1, 2);
        
        Assertions.assertEquals(rootResult.node, this.btree.search(3).node);
        Assertions.assertEquals(rootResult.index, this.btree.search(3).index);
        Assertions.assertEquals(rootResult.level, this.btree.search(3).level);
        
        Assertions.assertEquals(childResult.node, this.btree.search(2).node);
        Assertions.assertEquals(childResult.index, this.btree.search(2).index);
        Assertions.assertEquals(childResult.level, this.btree.search(2).level);
        
        Assertions.assertNull(this.btree.search(11));
    }
}
