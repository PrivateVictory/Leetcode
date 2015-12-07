class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> str;
    	int index;

    	for (int i = 0; i < nums.size(); i++) {
    		index = i;
    		while (i+1 < nums.size() && nums[i]+1 == nums[i+1])
    			i++;
    		if (index == i)
    			str.push_back(to_string(nums[index]));
    		else
    			str.push_back(to_string(nums[index]) + "->" + to_string(nums[i]));
    	}
    	return str;
    }
};