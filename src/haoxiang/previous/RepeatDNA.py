__author__ = 'lenovo'

class Solution:
    def findRepeatedDnaSequences(self, s):
        list = set([])
        lens = len(s)
        for i in range(0,len(s)-1):
            if (i+10)<=lens:
                temp_s = s[i:i+10]
                if temp_s in s[i+1:lens] :
                    list.add(temp_s)
        print list
    def findRepeatedDnaSequences_others_way(self, s):
        repeatSeq = set()
        addedSeq = set()
        result = []
        answer = []
        charToBin = {'A' : 0b00, 'T' : 0b01, 'G' : 0b10, 'C' : 0b11}
        mask = 0xfffff
        current = 0
        for i in range(len(s)):
            #create bit
            x = charToBin[s[i]]
            current |= x
            if i >= 9:
                if current in repeatSeq:
                    if current not in addedSeq:
                        addedSeq.add(current)
                        result.append(i - 9)
                else:
                    repeatSeq.add(current)
            #shift
            current <<= 2
            #mask
            current &= mask
        for i in result:
            answer.append(s[i : i + 10])
        return answer

s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
test = Solution()
test.findRepeatedDnaSequences(s)