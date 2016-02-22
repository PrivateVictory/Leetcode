package haoxiang.Array;

import java.util.Arrays;

/**
 * Created by haoxiang on 16/2/20.
 */
public class MedianFinder {
    private int [] res = new int [1000];
    private int len = 0;

    public void addNum(int num) {
        len++;
        res[len-1] = num;
        Arrays.sort(res);
    }

    public double findMedian() {
        int mid;
        double result;
        if(len%2==0){
            mid = len/2;
            result = res[mid];
        }else{
            mid = len/2;
            result =( res[mid]+res[mid-1])/2;
        }
        return result;
    }
}
