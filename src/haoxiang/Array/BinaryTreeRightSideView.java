package haoxiang.Array;

import java.util.*;

/**
 * Created by haoxiang on 16/3/22.
 */
public class BinaryTreeRightSideView {
      public static  class TreeNode {
          int val;
          TreeNode left;
          TreeNode right;
          TreeNode(int x) { val = x; }
      }
    public List<Integer> rightSideView(TreeNode root) {

        List<Integer> res = new ArrayList<Integer>();
        Deque<TreeNode> q = new ArrayDeque<TreeNode>();
        if(root == null) return res;
        q.add(root);
        while(!q.isEmpty()){
            res.add(q.getLast().val);
            for(int i =0;i<q.size();++i){
                TreeNode tmp = q.getFirst();
                q.pollFirst();
                if(tmp.left!=null) q.addLast(tmp.left);
                if(tmp.right!=null) q.addLast(tmp.right);
            }

        }
        return res;


    }
}
