package haoxiang.Array;

/**
 * Created by haoxiang on 16/2/25.
 */
public class FindtheDuplicateNumber {
    public int findDuplicate(int[] nums) {
        int [] num = new int [nums.length];
        int res = 0;
        for(int i =0;i<nums.length;i++){
            num[nums[i]]++;
        }
        for(int j =0;j<num.length;j++){
            if(num[j]>1){
                res = num[j];
                break;
            }
        }
        return res;
    }
}
