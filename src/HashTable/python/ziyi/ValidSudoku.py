#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-17 15:55:16
# @Author  : Alex Tang (1174779123@qq.com)
# @Link    : t1174779123.iteye.com

"""
	description:
"""

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        list_row = [0]*9
        list_col = [0]*9
        list_squ = [0]*9
        #find if each row/column/square not repeat
        for i in range(9):
        	for j in range(9):
        		#row
        		if not board[i][j] == '.':
        			temp = int(board[i][j])-1
        			if not list_row[temp] == 0:
        				print 'row: i = ',i,'j = ',j,'num = ',temp+1,'list_row = ',list_row
        				return False
        			else:
        				 list_row[temp] = 1
        		#col
        		if not board[j][i] == '.':
        			temp = int(board[j][i])-1
        			if not list_col[temp] == 0:
        				print 'col: i = ',i,'j = ',j,'num = ',temp+1,'list_col = ',list_col
        				return False
        			else:
        				list_col[temp] = 1
        		#square
        		if not board[(i/3)*3+j/3][(i%3)*3+j%3] == '.':
        			temp = int(board[(i/3)*3+j/3][(i%3)*3+j%3])-1
        			if not list_squ[temp] == 0:
        				print 'squ: i = ',i,'j = ',j,'num = ',temp+1,'list_squ = ',list_squ
        				return False
        			else:
        				list_squ[temp] = 1
        	# print 'i = ',i,'list_row:',list_row
        	# print 'i = ',i,'list_col:',list_col
        	# print 'i = ',i,'list_squ:',list_squ
        	# print ''
        	#reset num list
        	list_row = [0]*9
        	list_col = [0]*9
        	list_squ = [0]*9
        return True

def main():
	s = Solution()
	a = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
	print_sudoku(a)
	print s.isValidSudoku(a)
	b = [".87654328","2........","3........","4........","5........","6........","7........","8........","9........"]
	print_sudoku(b)
	print s.isValidSudoku(b)
	c = ["..5.....6","....14...",".........",".....92..","5....2...",".......3.","...54....","3.....42.","...27.6.."]
	print_sudoku(c)
	print s.isValidSudoku(c)
	d = [".........","......3..","...18....","...7.....","....1.97.",".........","...36.1..",".........",".......2."]
	print_sudoku(d)
	print s.isValidSudoku(d)
def print_sudoku(board):
	for i in range(9):
		print board[i]

if __name__ == '__main__':
	main()

