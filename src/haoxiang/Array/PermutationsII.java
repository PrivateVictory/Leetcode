package haoxiang.Array;

import java.util.*;

/**
 * Created by haoxiang on 16/2/26.
 */
public class PermutationsII {
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        Set<List<Integer>> set = new HashSet<List<Integer>>();
        Perm(nums, 0, set);
        Iterator<List<Integer>> it = set.iterator();
        while (it.hasNext()) {
            List<Integer> item = it.next();
            res.add(item);
        }
        return res;
    }

    public void Perm(int[] num, int start, Set<List<Integer>> res) {
        if (start == num.length - 1) {
            List<Integer> tmpNum = new ArrayList<Integer>();
            for (int j = 0; j < num.length; j++) {
                tmpNum.add(num[j]);
            }

            res.add(tmpNum);
        }
        for (int i = start; i < num.length; i++) {
            int[] newNum = swap(num, i, start);
            Perm(newNum, start + 1, res);
            swap(num, start, i);
        }
    }

    public int[] swap(int[] num, int i, int j) {
        int tmp = num[i];
        num[i] = num[j];
        num[j] = tmp;
        return num;
    }
}
