// Solution 1 in DP
class Solution {
public:
    int uniquePaths(int m, int n) {
        if (m == 1 && n == 1) return 1;
        vector<vector<int>> cache(m, vector<int>(n, 0));
        
        for (int j = n-2; j >= 0; j--)
            cache[m-1][j] = 1;
        for (int i = m-2; i >= 0; i--)
            cache[i][n-1] = 1;
        for (int i = m-2; i >= 0; i--)
            for (int j = n-2; j >= 0; j--)
                cache[i][j] = cache[i+1][j] + cache[i][j+1];
        return cache[0][0];
    }
};

// Solution 2 in Math
class Solution {
public:
    int uniquePaths(int m, int n) {
        if (m == 1 && n == 1) return 1;
        long long ret = 1;
        
        for (int i = n; i < m+n-1; i++)
            ret = ret * i/(i-n+1);
        return (int)ret;
    }
};