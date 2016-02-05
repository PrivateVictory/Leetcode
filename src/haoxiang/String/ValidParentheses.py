class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        map = {
            ")":"(",
            "}":"{",
            "]":"["
            }
        start = ["(","{","["]
        end = [")","}","]"]
        stack = []
        flag = True
        for i in s:
            if i in start:
                stack.append(i)
            elif len(stack) != 0:
                tmp = stack.pop()
                if map[i] == tmp:
                    continue
                else:
                    return False
            elif len(stack) == 0:
                return False

        return True if len(stack) == 0 else False
                    
