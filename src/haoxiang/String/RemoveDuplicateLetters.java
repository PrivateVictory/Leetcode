package haoxiang.String;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Stack;

/**
 * Created by haoxiang on 16/2/15.
 */
public class RemoveDuplicateLetters {

    public String removeDuplicateLetters(String s) {

        String res = "";
        char[] ch = s.toCharArray();
        char[] num = new char[26];
        boolean[] visited = new boolean[26];
        for (char c : ch) {
            num[c - 'a']++;
        }
        Stack<Character> st = new Stack<Character>();
        for (char c : ch) {
            int index = c - 'a';
            num[index]--;
//            if(visited[index]) continue;
            if(st.contains(c))continue;
            while (!st.isEmpty() && c < st.peek() && num[st.peek() - 'a'] != 0) {
                visited[st.pop()-'a'] = false;
            }
            st.push(c);
            visited[index] = true;
        }
        StringBuilder sb = new StringBuilder();
        while(!st.isEmpty()){
            sb.insert(0,st.pop());
        }
        return sb.toString();

    }

}
