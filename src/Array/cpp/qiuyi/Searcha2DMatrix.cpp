class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if (matrix.empty()) return false;
        int n = matrix[0].size();
        int i = 0;
        int j = matrix.size() -1;
        
        while (i <= j) {
            int mid = (i+j)/2;
            int flag = bi_search(matrix[mid], 0, n, target);
            if (flag == 1) return true;
            if (flag == 0) return false;
            if (flag == -1) j = mid-1;
            if (flag == 2) i = mid+1;
        }
        return false;
    }
    
    int bi_search(vector<int>& v, int i, int j, int target) {
        int mid = (i+j)/2;
        if (i>j && i>=v.size()) // right out
            return 2;   
        else if (i>j && j<0) // left  out
            return -1;
        else if (i > j)     // not found
            return 0;
        if (v[mid] == target)
            return 1;
        else if (v[mid] < target)
            return bi_search(v, mid+1, j, target);
        else if (v[mid] > target)
            return bi_search(v, i, mid-1, target);
        // return 1 found, -1 less, 2 biger, 0 not found
    }
};