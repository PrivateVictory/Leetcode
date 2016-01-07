class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        
        for (int i = n-2; i >= 0; i--)
            grid[m-1][i] += grid[m-1][i+1];
        for (int j = m-2; j >= 0; j--)
            grid[j][n-1] += grid[j+1][n-1];
        
        for (int j = m-2; j >= 0; j--)
            for (int i = n-2; i >= 0; i--)
                grid[j][i] += min(grid[j][i+1], grid[j+1][i]);
        return grid[0][0];
    }
};