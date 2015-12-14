class Solution {
public:
    vector<vector<int>> combinationSum3(int k, int n) {
        vector<vector<int>> ret;
        vector<int> t;
        dfs(ret, t, k, n, 1);
        return ret;
    }
    
    void dfs(vector<vector<int>>& ret, vector<int>& t, int k, int n, int index) {
        if (n == 0 && k == 0) {
            ret.push_back(t);
            return;
        }
        if (n < 0 || k <= 0)
            return;
        
        for (int i = index; i <= 9; i++) {
            t.push_back(i);
            dfs(ret, t, k-1, n-i, i+1);
            t.pop_back();
        }
    }
};