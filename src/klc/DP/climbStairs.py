"""
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Note: Given n will be a positive integer.
I started by asking what the answer will be for n=0, n=1, and n=2. The key is to see that at each step i,
the total number of ways to get to step i depends on the total number of ways to get to step "i-2" and step "i-1" respectively.
In other words, steps(i)= steps(i-1)+steps(i-2). This is the recurrence relation and then it's standard DP afterwards. 
Time and space complexity both O(n).
"""
class Solution(object):
    def climbStairs(self,n):
        if(n==0):
            return 0
        elif(n==1):
            return 1
        steps=[0]*(n+1)
        steps[1]=1
        steps[2]=2
        for i in range(3,n+1):
            steps[i]= steps[i-1]+steps[i-2]
        return steps[n]
