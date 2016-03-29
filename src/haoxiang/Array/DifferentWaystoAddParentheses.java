package haoxiang.Array;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by haoxiang on 16/3/22.
 */
public class DifferentWaystoAddParentheses {

    public List<Integer> diffWaysToCompute(String input) {

        List<String> stringRes = new ArrayList<String>();
        char [] str = input.toCharArray();
        List<Integer> left = new ArrayList<Integer>();
        List<Integer> right = new ArrayList<Integer>();
        List<Integer> res = new ArrayList<Integer>();

        for(int i =0;i<input.length();++i){
            if(Character.isDigit(str[i])) continue;
            left = diffWaysToCompute(input.substring(0,i));
            right = diffWaysToCompute(input.substring(i+1,input.length()-i-1));
            for(int j = 0; j < left.size(); ++j)
                     for( int k =0; k < right.size(); ++k)
                        res.add(compute(left.get(j), right.get(k), input.charAt(i)));
        }
        return res;

    }
    public int compute(int a ,int b,char op){
        switch (op){
            case '+':return a+b;
            case '-':return a-b;
            case '*':return a*b;
        }
        return 0;
    }
}
