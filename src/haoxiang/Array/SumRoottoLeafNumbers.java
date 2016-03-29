package haoxiang.Array;

/**
 * Created by haoxiang on 16/3/25.
 */
public class SumRoottoLeafNumbers {
    public static class TreeNode {
            int val;
             TreeNode left;
             TreeNode right;
             TreeNode(int x) { val = x; }
         }

    private String sum = "";
    public int sumNumbers(TreeNode root) {
        findSum(root,"");
//        return sum;
        return Integer.parseInt(sum);
    }
    public void findSum(TreeNode root,String curr){
        if(root == null)return;
        if(root !=null && root.left == null && root.right == null) {
            curr+=Integer.toString(root.val);
            sum+=curr;
            return;
        }
        if(root != null && root.left !=null){
            curr+=Integer.toString(root.val);
            findSum(root.left,curr);
        }
        if(root!=null && root.right != null){
            curr+=Integer.toString(root.val);
            findSum(root.right,curr);
        }

    }
}
