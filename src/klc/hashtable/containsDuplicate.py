"""
Given an array of integers, find if the array contains any duplicates. 
Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.

There are several ways to do this. 1) We can check each element against every other element which 
takes O(n^2) time because we need two nested loops. 2) Can sort the input and check whether consecutive elements
are identical, O(n lgn). 3) Use a hash map (dictionary) 
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #can actually be shortened to return len(nums)!= len(set(nums))
        if(len(nums)<=1):
            return False
        if (len(nums)==len(set(nums))):
            return False
        else:
            return True
            
#Using a dictionary            
class Solution(object):
    def containsDuplicate(self, nums):
        d = {}
        for i,v in enumerate(nums):
            if v not in d: #add each pair to dictionary, if v already in dictionary, then there is a duplicate
                d[v] = i
            else: 
                return True
        return False
        
  #dictionary solution      
 class Solution(object):
    def containsDuplicate1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = {}
        for i in nums:
            if i in d:
                return True
            else:
                d[i] = 1
        return False

 

                
