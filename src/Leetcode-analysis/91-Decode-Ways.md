# [91. Decode Ways](https://leetcode.com/problems/decode-ways/)

> A message containing letters from A-Z is being encoded to numbers using the following mapping:

	'A' -> 1
	'B' -> 2
	...
	'Z' -> 26

> Given an encoded message containing digits, determine the total number of ways to decode it.

> For example,Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

> The number of ways decoding "12" is 2.

这题主要是考察的是String的操作。然后可以使用动态规划的思想。

假设有个n个元素的数组，则这个数组(0到n-1)能够反编码的方式个数是0到n-2的子数组的反编码方式数与0到n-3的子数组的反编码方式数之和。依次类推。每次分割1个字符或者2个字符。

	public int numDecodings(String s) {
    	if(s==null || s.length()<=0) return 0;
    	//1-26。其实是对字符串数的一个分段。跟IP分割一样 每次取一个字符或者两个字符
    	int len = s.length();
    	int[] cache = new int[len];
    	if(s.charAt(0)!='0') cache[0] = 1;
    	else return 0;
    	if(s.length()==1) return cache[0];
    	//分割一个字符 不能为0
    	if(s.charAt(1)!='0') cache[1] = cache[0];
    	else cache[1] = 0;
    	//分割两个字符  注意前面不能从0开始
    	int tem = Integer.parseInt(s.substring(0, 2));
    	if(tem>0 && tem<=26 ) cache[1] += 1;
    	if(cache[1]==0) return 0;
    	for(int i=2;i<len;i++){
    		//分割一个字符 不能为0
    		if(s.charAt(i)!='0') cache[i] = cache[i-1];
    		else cache[i] = 0;
    		
    		//分割两个字符  注意前面不能从0开始
    		int temp = Integer.parseInt(s.substring(i-1, i+1));
    		if(temp>0 && temp<=26 && s.charAt(i-1)!='0') cache[i] += cache[i-2];
    		
    		if(cache[1]==0) return 0;
    	}
        return cache[len-1];
    }