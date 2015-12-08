class Solution {
public:
	vector<vector<int>> generate(int numRows) {
		vector<vector<int>> triangle;

		for (int i = 0; i < numRows; i++) {
			vector<int> temp;
			for (int j = 0; j <= i; j++) {
				if (j == 0 || j == i)
					temp.push_back(1);
				else
					temp.push_back(triangle[i-1][j-1]+triangle[i-1][j]);
			}
			triangle.push_back(temp);
		}
		return triangle;
	}
};