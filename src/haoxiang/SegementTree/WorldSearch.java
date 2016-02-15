package haoxiang.SegementTree;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Created by haoxiang on 16/2/6.
 */
public class WorldSearch {

//    public void dfs(Trie trie, Set<String> set, int i, int j, char[][] board, String word, boolean[][] visited){
//        if(i<0 || j<0 || i>board.length-1 || j> board[0].length-1 || visited[i][j]) return;
//
//        //get the current stream of the word
//        word += board[i][j];
//
//        //for a particular path we take in the graph, we make sure we dont revisit them in the following recurrences
//        visited[i][j] = true;
//
//        //search the trie for the word
//        SearchResult result = trie.search(word);
//
//        //if considering the word as a prefix fails, then there is no use to proceed, so we terminate
//        if(result == SearchResult.NOT_FOUND){
//            //reset visited to false
//            visited[i][j] = false;
//            return;
//        }//if the word itself was found, then add it to the set
//        else if(result == SearchResult.WORD_FOUND) set.add(word);
//
//        //now perform DFS
//        dfs(trie, set, i-1, j, board, word, visited);
//        dfs(trie, set, i+1, j, board, word, visited);
//        dfs(trie, set, i, j-1, board, word, visited);
//        dfs(trie, set, i, j+1, board, word, visited);
//
//        //reset visited to false
//        visited[i][j] = false;
//    }


    public List<String> findWords(char[][] board, String[] words) {
        List<String> res = new ArrayList<String>();
        if(board.length == 0 || words.length == 0 || board[0].length == 0) return res;
        Trie trie = new Trie();

        for(int i =0;i<words.length;i++){
            trie.insert(words[i]);
        }


        return res;

    }

}

class Trie{
    TrieNode root = null;
    public  Trie(){
        this.root = new TrieNode();

    }
    public boolean search(String word){
        TrieNode node = root;
        for(int i =0;i<word.length();i++){
            if(!node.chiden.containsKey(word.charAt(i))) return false;
            else node.chiden.get(word.charAt(i));
        }
        return true;

    }
    public void insert(String word){

        TrieNode node = root;
        for(int i =0;i<word.length();i++){
            char ch = word.charAt(i);
            if(!node.chiden.containsKey(ch)) node.add(ch);
            else{
                node = node.chiden.get(ch);
            }

        }
    }

}
class TrieNode{
    Map<Character,TrieNode> chiden = new HashMap<Character, TrieNode>();
    boolean isEnd;
    String value;
    public TrieNode(String value){
        this.value = value;

    }
    public TrieNode(){}
    public void add(char c){
        this.chiden.put(c,new TrieNode(value));
    }

}