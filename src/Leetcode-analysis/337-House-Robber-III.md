# [337. House Robber III](https://leetcode.com/problems/house-robber-iii/)

可以使用深度优先遍历算法，层层递归下去。而对于每一层来说，该层可以是被偷或者是被偷。当被偷的时候，显然他的下一层就不能被偷了。当没有被偷的时候，其下一层是可以被偷的。而不管这一层是判断如何，到下一层时候，又是一个完整的子结构，思考过程类似。

	public int rob(TreeNode root) {
    	if(root==null) return 0;
    	if(root.left==null && root.right==null) return root.val;
    	//二叉树的递归
    	//偷该户
    	int rob = root.val;
    	//不偷该户
    	int noRob = 0;
    	if(root.left!=null){
    		//相连的不偷，以此又是一个完整的子结构
    		rob += rob(root.left.left) + rob(root.left.right);
    		noRob += rob(root.left);
    	}
    	if(root.right!=null){
    		rob += rob(root.right.left) + rob(root.right.right);
    		noRob += rob(root.right);
    	}
    	return Math.max(rob, noRob);
    }
