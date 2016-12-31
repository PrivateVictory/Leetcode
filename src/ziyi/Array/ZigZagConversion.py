#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-31 05:32:38
# @Author  : AlexTang (1174779123@qq.com)
# @Link    : http://t1174779123.iteye.com
# @Description：ZigZag Conversion，字符串转换为之字形顺序
'''
    基本思路：对于m行结构，每行的结构分别为    (2m-2)*n
                                        (2m-2)*n+1          (2m-2)*n+(2m-2-1)
                                        (2m-2)*n+2        (2m-2)*n+(2m-2-2)
                                        (2m-2)*n+3    (2m-2)*n+(2m-2-3)
                                        ...             ...
                                        (2m-2)*n+m-2  (2m-2)*n+m
                                        (2m-2)*n+m-1
            所以，第i行的结构为： (2m-2)*n+i                        i=0,m-1
                                (2m-2)*n+i,(2m-2)*n+(2m-2-i)    0<i<m-1
            生成思路为：  1 求商和余数，根据数列得到每行的序号
                        2 根据序号顺序构造新的字符串

'''
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        result = ''
        l = len(s)
        if l == 0 or numRows == 1:
            return s
        cycle = 2*numRows - 2
        n = l / cycle
        print 'l:%d cycle:%d n:%d'%(l,cycle,n)
        for i in range(numRows):
            print 'the',i,'th loop:'
            for j in range(n+1):
                # 添加(2m-2)*n+i
                index_1 = cycle * j + i
                if index_1 < l:
                    result += s[index_1]
                    # print 'add index_1',index_1,' ',s[index_1]
                # 如果不是首末行，添加(2m-2)*n+(2m-2-i)
                if 0 < i < (numRows-1):
                    index_2 = cycle * j + cycle - i
                    if index_2 < l:
                        result += s[index_2]
                        # print 'add index_2',index_2,' ',s[index_2]
        return result

def main():
    s = Solution()
    print s.convert('PAYPALISHIRING',3)
    print s.convert('ABCDEFGHIJKLMNOPQRST',5)
if __name__ == '__main__':
    main()




