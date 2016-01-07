class Solution {
public:
	int missingNumber(vector<int>& nums) {
		int sum1 = 0;
		int sum2 = 0;

		for (auto i = 0; i < nums.size(); i++)
			sum1 += i;
		for (auto num : nums) {
			sum2 += num;
		}

		return sum1 - sum2;
	}
};