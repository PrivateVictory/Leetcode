#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-14 23:51:54
# @Author  : Alex Tang (1174779123@qq.com)
# @Link    : http://t1174779123.iteye.com

'''
    description:
'''

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        self.matrix = matrix
        if matrix == []:
            return []
        else:
            m, n = len(matrix), len(matrix[0])
        self.step_count = 0
        self.result = []
        #positions
        self.cur_pos = [0,-1]
        #directions
        self.UP, self.DOWN, self.LEFT, self.RIGHT = 1, 2, 3, 4
        self.cur_direction = self.RIGHT
        #sides
        self.up_side, self.down_side, self.left_side, self.right_side = -1, m, -1, n
        #stop loop when pass m*n steps 
        while not self.step_count == m * n:
            #a loop
            self.move()
            self.update_direction()
        return self.result
    #move method             
    def move(self):
        if self.cur_direction == self.RIGHT:
            self.cur_pos[1] += 1
        elif self.cur_direction == self.DOWN:
            self.cur_pos[0] += 1
        elif self.cur_direction == self.LEFT:
            self.cur_pos[1] -= 1
        elif self.cur_direction == self.UP:
            self.cur_pos[0] -= 1
        self.step_count += 1
        self.result.append(self.matrix[self.cur_pos[0]][self.cur_pos[1]])
    #judge if change direction
    def update_direction(self):
        if (self.cur_direction == self.RIGHT and self.cur_pos[1] == self.right_side - 1) or\
            (self.cur_direction == self.DOWN and self.cur_pos[0] == self.down_side - 1) or\
            (self.cur_direction == self.LEFT and self.cur_pos[1] == self.left_side + 1) or\
            (self.cur_direction == self.UP and self.cur_pos[0] == self.up_side + 1) :
            self.turnRight()
    #turn right method
    def turnRight(self):
        if self.cur_direction == self.UP:
            self.cur_direction = self.RIGHT
            self.left_side += 1
        elif self.cur_direction == self.RIGHT:
            self.cur_direction = self.DOWN
            self.up_side += 1
        elif self.cur_direction == self.DOWN:
            self.cur_direction = self.LEFT
            self.right_side -= 1
        elif self.cur_direction == self.LEFT:
            self.cur_direction = self.UP
            self.down_side -= 1
        
def main():
    s = Solution()
    print s.spiralOrder([])
    a = [[1,2,3],[4,5,6],[7,8,9]]
    print_matrix(a)
    print s.spiralOrder(a)
    b = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    print_matrix(b)
    print s.spiralOrder(b)
    c = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
    print_matrix(c)
    print s.spiralOrder(c)

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print matrix[i][j],'\t',
        print ''

if __name__ == '__main__':
    main()


