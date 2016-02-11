package haoxiang.HashTable;

import java.util.HashMap;

/**
 * Created by haoxiang on 16/2/11.
 */
public class TwoSum {

    public int[] twoSum(int[] nums, int target) {
        //2,7,11,15  9
        int [] res = new int [2];
        HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();
        for(int i =0;i<nums.length;++i){
            if(map.containsKey(nums[i])){
                res[0] = map.get(nums[i]);
                res[1] = i+1;
            }else{
                map.put(nums[i],i+1);
            }

        }
            return res;
    }
}
