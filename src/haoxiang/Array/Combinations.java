package haoxiang.Array;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by haoxiang on 16/2/26.
 */
public class Combinations {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        List<Integer> num = new ArrayList<Integer>();
        DFS(num,n,k,res,1);
        return res;
    }
    public void DFS(List<Integer> cur,int n,int k,List<List<Integer>> res,int step){
        if(cur.size() == k) {
            res.add(new ArrayList<Integer>(cur));
            return;
        }
        if (cur.size() > k) {
            return;
        }
//        Math.pow(1,2);
        for(int i = step;i<=n;i++){
            cur.add(i);
            DFS(cur,n,k,res,i+1);
            cur.remove(cur.size()-1);
        }
    }
}
