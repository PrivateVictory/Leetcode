package com.cyw.leetcode;

import java.util.ArrayList;

/**
 * https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
 * @author cyw
 *
 */
public class LowestCommonAncestorOfABinarySearchTreeProbblem235 {

	public static void main(String[] args) {

	}
	/**
	 * 1、遍历分别到达p、q的路径，求出两路径的最初相交的结点HashMap、排序
	 * @param root
	 * @param p
	 * @param q
	 * @return
	 */
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(root==null || p==null || q==null) return null;
        ArrayList<TreeNode> list1 = new ArrayList<TreeNode>();
        ArrayList<TreeNode> list2 = new ArrayList<TreeNode>();
        if(!findNode(list1, root, p)) return root;
        if(!findNode(list2, root, q)) return root;
        for(TreeNode tr1 : list1){
        	for(TreeNode tr2:list2){
        		if(tr1==tr2) return tr1;
        	}
        }
        return root;
    }
    
    /**
     * 递归遍历，得到root到p的路径
     * @param list
     * @param root
     * @param p
     * @return
     */
    public boolean findNode(ArrayList<TreeNode> list, TreeNode root, TreeNode p){
    	if(list==null || root==null || p==null) return false;
    	if(root==p) {
    		list.add(root);
    		return true;
    	}
    	boolean flag = false;
    	if(root.left!=null && findNode(list, root.left, p)){
    		flag = true;
			list.add(root);
    	}
    	if(root.right!=null && findNode(list, root.right, p)){
    		flag = true;
    		list.add(root);
    	}
    	return flag;
    }
    public class TreeNode {
	     int val;
	     TreeNode left;
	     TreeNode right;
	     TreeNode(int x) { val = x; }
    }
}
