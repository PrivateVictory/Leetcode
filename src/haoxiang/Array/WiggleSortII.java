package haoxiang.Array;

import java.util.Arrays;

/**
 * Created by haoxiang on 16/2/20.
 */
public class WiggleSortII {

    public void wiggleSort(int[] nums) {
        Arrays.sort(nums);
        int[] res = new int[nums.length];
        int mid = nums.length/2;
        if (nums.length % 2 != 0)
            mid++;
        int start = mid - 1;
        int end = nums.length - 1;
        for (int i = 0; i < nums.length; i++) {
            if (i % 2 == 0) {
                res[i] = nums[start];
                start--;
            } else {
                res[i] = nums[end];
                end--;
            }
        }
        for (int i = 0; i < nums.length; i++) {
            nums[i] = res[i];
        }
    }
}
