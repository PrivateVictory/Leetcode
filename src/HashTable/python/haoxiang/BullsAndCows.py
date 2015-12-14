#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def getHint(self, secret, guess):
        aNum = 0
        bNum = 0
        sec = {}
        secret = list(secret)
        guess = list(guess)
        for i in range(len(secret)):
            if sec.has_key(secret[i]):
                sec[secret[i]].append(i)
            else:
                sec[secret[i]] = [i]
        for k in range(len(guess)):
            if sec.has_key(guess[k]):
                print sec[guess[k]]
                if len(sec[guess[k]])>0:
                    if k in sec[guess[k]]:
                        aNum+=1
                        sec[guess[k]].remove(k)
                        guess[k] = "#"
                    # else:
                    #     bNum+=1
                    #     # sec[guess[k]].pop()
        for j in range(len(guess)):
            if sec.has_key(guess[j]):
                if len(sec[guess[j]])>0:
                    if j not in sec[guess[j]]:
                        bNum+=1
                        sec[guess[j]].pop()

        return str(aNum)+"A"+str(bNum)+"B"


Test = Solution()
print Test.getHint("1122","1222")