class Solution {
public:
	int minSubArrayLen(int s, vector<int>& nums) {
		int r,l,sum;
		int ret = nums.size()+1;

		r = l = sum = 0;
		while (r < nums.size()) {
			sum += nums[r++];
			while (sum >= s) {
				ret = min(ret, r-l);
				sum -= nums[l++];
			}
		}
		return ret <= nums.size() ? ret : 0;
	}
};