class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]] #i.e. costs[0][0] is paint the 0th house red. 
        :rtype: int
        """
        #initial costs of last house painted R, G, or B respectively
        if(len(costs)==0):
            return 0
        n=len(costs)
        lastR = costs[0][0]
        lastG = costs[0][1]
        lastB = costs[0][2]
        
        for i in range(1, n):
            curR = min(lastG, lastB) + costs[i][0]
            curG = min(lastR, lastB) + costs[i][1]
            curB = min(lastR, lastG) + costs[i][2]
            
            lastR=curR
            lastG=curG
            lastB=curB
        
        return min(lastR, lastB, lastG)
            
