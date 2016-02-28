package haoxiang.Array;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by haoxiang on 16/2/25.
 */
public class Permutations {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        Perm(nums,0,res);
        return res;
    }
    public void Perm(int [] num,int start,List<List<Integer>> res){
        if(start == num.length-1) {
            List<Integer> tmpNum = new ArrayList<Integer>();
            for(int j = 0;j<num.length;j++){
                tmpNum.add(num[j]);
            }
            res.add(tmpNum);
        }
        for(int i = start;i<num.length;i++){
            int [] newNum = swap(num,i,start);
            Perm(newNum, start + 1,res);
            swap(num,start,i);
        }
    }
    public int [] swap(int []num,int i,int j){
        int tmp = num[i];
        num[i] = num[j];
        num[j] = tmp;
        return num;
    }
}