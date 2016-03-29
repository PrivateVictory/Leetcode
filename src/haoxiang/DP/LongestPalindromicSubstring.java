package haoxiang.DP;

/**
 * Created by haoxiang on 16/3/14.
 */
public class LongestPalindromicSubstring {

    public String longestPalindrome(String s) {
        char [] sc = s.toCharArray();
        char [] sn = new char[s.length()];
        String res = "";
        int len = s.length();
        for(int i =0;i<s.length();++i){
            sn[len-i-1] = sc[i];
        }
        int[][]c = new int[sc.length+1][sn.length+1];
        int maxlen = 0;
        int maxindex = 0;
        for(int i =1;i<=sc.length;i++){
            for(int j=1;j<=sn.length;j++){
                if(sc[i-1] == sn[j-1]){
                    c[i][j] = c[i-1][j-1]+1;
                    if(c[i][j] > maxlen)
                    {
                        maxlen = c[i][j];
                        maxindex = i + 1 - maxlen;
                    }
                }
            }
        }
        for(int j =maxindex;j<=maxlen;j++){
            res+=sc[j];
        }

        return res;

    }
}
