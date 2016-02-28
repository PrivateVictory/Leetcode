package haoxiang.Array;

import java.util.HashMap;

/**
 * Created by haoxiang on 16/2/25.
 */
public class MaximumProductofWordLengths {

    public int maxProduct(String[] words) {
        int res = 0;
        int [] num ;
        for(int i =0;i<words.length;++i){
            num = new int [26];
            for(int j =0;j<words[i].length();j++){
                int tmp = words[i].charAt(j) - 'a';
                num[tmp]++;
            }
            for(int k = i;k<words.length;k++){
                boolean flag = true;
                for (int m = 0;m<words[k].length();m++){
                    int tmp = words[k].charAt(m) - 'a';
                    if(num[tmp] != 0){
                        flag = false;
                        break;
                    }
                }
                if(flag) res = Math.max(res,words[i].length()*words[k].length());
            }
        }

        return res;
    }
}
