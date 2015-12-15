class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.empty()) return 0;
        int maxVal = 0;
        int minVal = prices[0];
        
        for (int i = 1; i < prices.size(); i++) {
            minVal = min(minVal, prices[i]);
            maxVal = max(maxVal, prices[i]-minVal);
        }
        return maxVal;
    }
};