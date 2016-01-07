#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-01-06 21:11:37
# @Author  : Alex Tang (1174779123@qq.com)
# @Link    : http://t1174779123.iteye.com

'''
    description:
'''

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        THOUSANDS = ['','Thousand','Million','Billion']
        TEENS = ['Ten','Eleven','Twelve','Thirteen','Fourteen',\
                'Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
        TENS = ['','','Twenty','Thirty','Forty','Fifty',\
                'Sixty','Seventy','Eighty','Ninety']
        ONES = ['','One','Two','Three','Four','Five',\
                'Six','Seven','Eight','Nine']
        words = []
        place = 0
        # zero
        if num == 0:
            return 'Zero'
        while num:
            # meet thousand
            if place % 3 == 0:
                r_thousand = num % 1000
                r_hundred = num % 100
                num /= 100
                place += 2

                # add thousand
                if r_thousand and place / 3:
                    words.append(THOUSANDS[place / 3])
                # add decade and unit
                if r_hundred:
                    num_ten = r_hundred / 10
                    num_one = r_hundred % 10
                    if num_ten == 0:
                        words.append(ONES[num_one])
                    elif num_ten == 1:
                        words.append(TEENS[num_one])
                    elif num_ten > 1:
                        words.append(ONES[num_one])
                        words.append(TENS[num_ten])
            # meet hundred
            elif place % 3 == 2:
                num_hundred = num % 10
                num /= 10
                place += 1
                # add hundred
                if num_hundred:
                    words.append('Hundred')
                    words.append(ONES[num_hundred])
        return ' '.join([x for x in reversed(words) if x])

def main():
    s = Solution()

    print s.numberToWords(0)
    print s.numberToWords(123)
    print s.numberToWords(1234)
    print s.numberToWords(12345678)
    print s.numberToWords(100000)

if __name__ == '__main__':
    main()

            







            


