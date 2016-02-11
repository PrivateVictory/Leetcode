package haoxiang.HashTable;

import java.util.*;

/**
 * Created by haoxiang on 16/2/11.
 */
public class ThreeSum {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();

        for (int i = 0; i < nums.length; ++i) {

            HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
            int target = 0 - nums[i];
            for (int j = 0; j < nums.length; ++j) {
                int tmp = target - nums[j];
                if (map.containsKey(tmp)) {
                    List<Integer> list = new ArrayList<Integer>();
                    int min = Math.min(Math.min(nums[i],tmp),nums[j]);
                    int max = Math.max(Math.max(nums[i],tmp),nums[j]);
                    list.add(min);
                    if(min!=nums[i]&&max!=nums[i])list.add(nums[i]);
                    if(min!=nums[j]&&max!=nums[j])list.add(nums[j]);
                    if(min!=tmp&&max!=tmp)list.add(tmp);
                    list.add(max);
                    if(!res.contains(list))res.add(list);
                    break;

                } else {
                    map.put(nums[j], 1);
                }
            }

        }
        return res;

    }
}
