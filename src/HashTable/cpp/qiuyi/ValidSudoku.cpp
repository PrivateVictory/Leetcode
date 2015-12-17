class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int count_r[9][9] = {0};
        int count_c[9][9] = {0};
        int count_s[9][9] = {0};
        int m = board.size();
        int n = board[0].size();
        
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++) {
                if (board[i][j] == '.') continue;
                if (++count_r[i][board[i][j]-'1'] > 1) return false;
                if (++count_c[j][board[i][j]-'1'] > 1) return false;
                if (++count_s[i/3 * 3 + j/3][board[i][j]-'1'] > 1) return false;
            }
        return true;
    }
};