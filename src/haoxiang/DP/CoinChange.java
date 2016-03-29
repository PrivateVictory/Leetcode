package haoxiang.DP;

import java.util.Arrays;

/**
 * Created by haoxiang on 16/3/11.
 */
public class CoinChange {
    public int coinChange(int[] coins, int amount) {

        int res = 0;
        int sum = 0;
        Arrays.sort(coins);
        int len = coins.length-1;
        int start = 0;
        while(start>=len){
//            res+=coins[len];
            if(res==amount)return sum;

            if(res>amount){
                res-=coins[start];
                start++;
                res+=coins[start];
            }else {
                res+=coins[start];
                sum++;
            }
        }
        if(res==amount)return sum;
        else return -1;
    }
}
