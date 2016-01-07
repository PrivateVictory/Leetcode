class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();
        vector<vector<int>> cache(m, vector<int>(n, 0));

        for (int j = n-1; j >= 0; j--)
            if (obstacleGrid[m-1][j] != 1)
                cache[m-1][j] = 1;
            else
                break;
        for (int i = m-1; i >= 0; i--)
            if (obstacleGrid[i][n-1] != 1)
                cache[i][n-1] = 1;
            else
                break;
        for (int i = m-2; i >= 0; i--)
            for (int j = n-2; j >= 0; j--)
                if (obstacleGrid[i][j] != 1)
                    cache[i][j] = cache[i+1][j] + cache[i][j+1];
                else
                    continue;
        return cache[0][0];
    }
};