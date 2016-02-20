package haoxiang.Array;

import java.util.HashMap;

/**
 * Created by haoxiang on 16/2/16.
 */
public class HappyNumber {

    HashMap<Integer, Integer> res = new HashMap<Integer, Integer>();

    public boolean isHappy(int n) {
        if (n == 1) return true;
        if (res.containsKey(n)) return false;
        res.put(n, 1);
        int sum = 0;
        int m = n;
        while (m != 0) {
            int tmp = m % 10;
            sum += tmp * tmp;
            m /= 10;
        }

        return isHappy(sum);
    }
}
