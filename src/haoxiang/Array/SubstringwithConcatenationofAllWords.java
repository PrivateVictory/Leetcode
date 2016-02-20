package haoxiang.Array;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

/**
 * Created by haoxiang on 16/2/19.
 */
public class SubstringwithConcatenationofAllWords {

    public List<Integer> findSubstring(String s, String[] words) {
        int wordLen = words[0].length();
        int sLen = s.length();
        int wordsLen = words.length;
        List<Integer> res = new ArrayList<Integer>();
        HashMap<String, Integer> map = new HashMap<String, Integer>();

        int sum = 0;
        for (int k = 0; k < wordsLen; k++) {
            map.put(words[k], k + 1);
            sum += map.get(words[k]);
        }
        for (int i = 0; i < wordLen; ++i) {
            int t = i;
            int[] value = new int[sLen / wordsLen];
            int[] sumValue = new int[sLen / wordsLen];
            int tp = i;
            int n = 0;
            if (map.get(s.substring(tp, tp + wordLen)) != null) {
                value[0] = map.get(s.substring(tp, tp + wordLen));
            } else {
                value[0] = 0;
            }
            sumValue[0] = value[0];
            for (int m = 1; m < wordsLen; m++) {
                if (map.get(s.substring(tp, tp + wordLen)) != null) {
                    value[m] = map.get(s.substring(tp, tp + wordLen));
                } else {
                    value[m] = 0;
                }
                sumValue[m] = sumValue[m - 1] + value[m];
                tp += wordLen;
            }
            for(int m = 1; m < wordsLen; m++){
                System.out.println(sumValue[m]);
            }
            for (t = i; t < sLen; t += wordLen) {
                n++;
                if (t + wordLen < sLen && map.containsKey(s.substring(t, t + wordLen))) {
                    int tmpSum = sumValue[n + wordsLen] - sumValue[n];
                    if (tmpSum == sum) res.add(t);
                }
            }

        }

        return res;
    }
}
