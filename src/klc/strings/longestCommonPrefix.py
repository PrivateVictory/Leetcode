

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
            
        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)

# Another solution, using something already implemented in python
import os

class Solution:
    def longestCommonPrefix(self, strs):
        return os.path.commonprefix(strs)

# pythonic approach

 def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        shortest = min(strs,key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest 
        
 # another pythonic
def longestCommonPrefix(self, strs):
    prefix = ''
    # * is the unpacking operator, essential here
    for z in zip(*strs):
        bag = set(z)
        if len(bag) == 1:
            prefix += bag.pop()
        else:
            break
    return prefix
