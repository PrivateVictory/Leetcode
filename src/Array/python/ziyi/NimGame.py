#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return bool(n%4)

    def test_one(self,n):
    	print 'input n:',n,'canWinNim :',self.canWinNim(n)
    def test(self):
    	self.test_one(1)
    	self.test_one(4)
    	self.test_one(5)
    	self.test_one(7)
    	self.test_one(10)
    	self.test_one(12)

def main():
	s = Solution()
	s.test()
if __name__ == '__main__':
	main()

