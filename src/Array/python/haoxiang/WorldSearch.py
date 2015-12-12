class Solution(object):
    def __init__(self):
        self.row=0
        self.line=0
        self.step=0
        self.result=[]
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.line = len(board)
        self.row = len(board[0])
        self.step = len(word)

        for i in range(self.line):
            for j in range(self.row):
                if board[i][j] == word[0]:
                    res = self.findNext(i,j,board,word,0)
                    self.result.append(res)
        if self.result.__contains__(True):
            print "True"
            return True
        else:
            print "False"
            return False

    def findNext(self,i,j,board,word,index):
        if i<0 or j<0 or i>=self.line or j>=self.row or board[i][j]!=word[index]:
            return False
        elif index==self.step-1:
            return True
        else:
            temp=board[i][j]
            board[i][j]=0
            if self.findNext(i,j+1,board,word,index+1):
                return True
            if self.findNext(i-1,j,board,word,index+1):
                return True
            if self.findNext(i,j-1,board,word,index+1):
                return True
            if self.findNext(i+1,j,board,word,index+1):
                return True
            board[i][j]=temp
            return False
Test = Solution()
test =[
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
]
test2 = ["aa"
         "aaa"]
Test.exist(test,"ABC")