##Restore IP Addresses
这题的意思是说给一串的数字，可以在其中加上"."，问有几种可能生成的字符串是符合IP地址的规范。一看是遍历字符串然后排列组合的，直接dfs。每个ip的子数组有三种可能，1，2，3位数。注意要判断下生成的数字是不是有效的，还要注意不能以0开头（第一次没注意到这个case）。直接上代码：

```public class Solution {
    public List<String> restoreIpAddresses(String s) {
        List<String> res = new ArrayList<String>();
        if(s.length()>12)return res;
        dfs(s,"",0,res);
        return res;
        
    }
    public void dfs(String s,String tmp,int index,List<String> res){
        if(index == 3){
            if(isValid(s)){
                res.add(tmp+s);
                return;
            }
        }
        for(int i =1;i<4&&i<s.length();++i){
            String substr = s.substring(0,i);
            if(isValid(substr)){
                dfs(s.substring(i),tmp+substr+".",index+1,res);
            }
        }
    }
    public boolean isValid(String s){  
        if (s.charAt(0)=='0') return s.equals("0");  
        int num = Integer.parseInt(s);  
        return num<=255 && num>0;  
    }  
    
}
```