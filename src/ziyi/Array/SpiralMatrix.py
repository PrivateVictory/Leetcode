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
        if len(matrix) == 0:
            return []
        self.matrix = matrix
        self.m, self.n = len(matrix), len(matrix[0])
        self.result = []

        self.step_count = 0
        self.position = [0,-1]
        self.direction = 'r'
        self.up_side, self.down_side, self.left_side, self.right_side = -1, self.m, -1, self.n
        while self.step_count < self.m * self.n:
            self.move_and_step()
            self.update_direction()
        return self.result
    
    def move_and_step(self):
        #move
        if self.direction == 'r':
            self.position[1] += 1
        elif self.direction == 'd':
            self.position[0] += 1
        elif self.direction == 'l':
            self.position[1] -= 1
        elif self.direction == 'u':
            self.position[0] -= 1
        #step
        self.result.append(self.matrix[self.position[0]][self.position[1]])
        self.step_count += 1

    # change direction and side at conners
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


