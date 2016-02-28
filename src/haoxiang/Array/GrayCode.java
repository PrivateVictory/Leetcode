package haoxiang.Array;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by haoxiang on 16/2/25.
 */
public class GrayCode {

    public List<Integer> grayCode(int n) {

        List<Integer> res = new ArrayList<Integer>();
        res.add(0);
        for (int i = 0; i <n; ++i) {
            int size = res.size();
            int tmp = 1 << i;
            for (int j = size; j > 0; j--) {
                res.add(tmp + res.get(j));
            }
        }
        return res;
    }
}
