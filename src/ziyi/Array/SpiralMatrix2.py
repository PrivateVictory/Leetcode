#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-15 08:15:09
# @Author  : Alex Tang (1174779123@qq.com)
# @Link    : http://t1174779123.iteye.com

'''
	description:
'''

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        self.step_count = 0
        self.matrix = [[0]*n for i in range(n)]
        self.direction = 'r'
        self.position = [0,-1]
        self.up_side, self.down_side, self.left_side, self.right_side = -1, n, -1, n
        while self.step_count < n * n:
        	self.move_and_gen()
        	self.update_direction()
        return self.matrix
    
    def move_and_gen(self):
    	#move
    	if self.direction == 'r':
    		self.position[1] += 1
    	elif self.direction == 'l':
    		self.position[1] -= 1
    	elif self.direction == 'd':
    		self.position[0] += 1
    	elif self.direction == 'u':
    		self.position[0] -= 1
    	#generate
    	self.step_count += 1
    	self.matrix [self.position[0]][self.position[1]] = self.step_count
    #change direction and side at conners
    def update_direction(self):
    	if self.direction == 'r' and self.position[1] == self.right_side - 1:
    		self.direction = 'd'
    		self.up_side += 1
    	elif self.direction == 'd' and self.position[0] == self.down_side - 1:
    		self.direction = 'l'
    		self.right_side -= 1
    	elif self.direction == 'l' and self.position[1] == self.left_side + 1:
    		self.direction = 'u'
    		self.down_side -= 1
    	elif self.direction == 'u' and self.position[0] == self.up_side + 1:
    		self.direction = 'r'
    		self.left_side += 1

def print_matrix(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix)):
			print matrix[i][j],'\t',
		print ''
	print ''
def main():
	s = Solution()
	print_matrix(s.generateMatrix(3))
	print_matrix(s.generateMatrix(4))
	print_matrix(s.generateMatrix(5))
if __name__ == '__main__':
	main()
