package haoxiang.Array;

import java.util.HashMap;

/**
 * Created by haoxiang on 16/2/22.
 */
public class ExcelSheetColumnNumber {

    public int titleToNumber(String s) {
        int res = 0;
        int step = 0;
        for (int i = s.length() - 1; i >= 0; i--) {
            int n = (int) s.charAt(i) - 64;
            res += n * Math.pow(26, step);
            step++;
        }

        return res;

    }
}
