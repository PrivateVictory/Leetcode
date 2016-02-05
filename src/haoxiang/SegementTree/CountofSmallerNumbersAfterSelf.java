import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;

public class Solution {

    public  int[] sum;
    public  int[] left;
    public  int[] right;
    public List<Integer> countSmaller(int[] nums) {


        ArrayList<Integer> result = new ArrayList<Integer>();
        int root = 1;
        if(nums.length == 0) return result;
        List<Integer> tmp = new ArrayList<Integer>();
        for(int i =0;i<nums.length;i++){
            tmp.add(nums[i]);
        }
        Collections.sort(tmp);
        HashMap<Integer,Integer> map = new HashMap<Integer, Integer>();
        int k = 1;
        int step = 0;
        map.put(tmp.get(0),0);
        while(k<nums.length){
            if(!(tmp.get(k)>tmp.get(k-1))){
                map.put(tmp.get(k),step);
            }else{
                step++;
                map.put(tmp.get(k),step);
            }
            k++;
        }
        sum = new int[nums.length * 4];
        left  = new int[nums.length * 4];
        right  = new int[nums.length * 4];

        BulidTree(0,nums.length,1);
        for (int i = nums.length-1; i >= 0; i--) {
            result.add(Query(root, 0, map.get(nums[i])-1));
            Update(map.get(nums[i]),root);
        }
        Collections.reverse(result);
        return result;
    }

    public void BulidTree(int l, int r, int id ) {
        left[id] = l;
        right[id] = r;
        if (l == r) return;
        int mid = (l + r) >> 1;
        BulidTree(l, mid, id*2);
        BulidTree(mid + 1, r, id*2+1);
        sum[id] = sum[id * 2] + sum[id * 2 + 1];

    }

    public void Update(int pos,  int id ) {
        sum[id] += 1;
        if (left[id] == right[id]) {
            return;
        }
        int mid = (left[id] + right[id]) >> 1;
        if (pos <= mid) Update(pos, id*2);
        else Update(pos, id*2+1);

    }


    public int Query(int id,int l,int r) {
        if (l > r)
            return 0;
        if (l <= left[id] && right[id] <= r)
            return sum[id];
        int mid = left[id] + right[id] >> 1, result = 0;
        if (l <= mid)
            result += Query(id*2, l, r);
        if (r > mid)
            result += Query(id*2+1, l, r);
        return result;
    }

}
