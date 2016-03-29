package haoxiang.DP;

import java.util.Stack;

/**
 * Created by haoxiang on 16/3/10.
 */
public class LongestValidParentheses {
    public int longestValidParentheses(String s) {

        int result = 0;
        int sum = 0;
        int [] res = new int [s.length()];
        Stack<Character> charStack = new Stack<Character>();
        Stack<Integer> intStack = new Stack<Integer>();
        for(int i =0;i<s.length();++i){
            if(s.charAt(i)=='('){
                charStack.push('(');
                intStack.push(i);
            }else {
                if(!charStack.empty()){
                    res[i] =1;
                    res[intStack.pop()] =1;
                    charStack.pop();
                }else{
                    sum = 0;
                }
            }
        }
        for(int j = 0;j<s.length();++j){
            if(res[j] == 1){
                sum++;
                result = Math.max(sum,result);
            }else {
                sum = 0;
            }

        }

        return result;
    }
}
