// Solution 1
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() == 0) return 0;

		int index = 0;
		for (int i = 1; i < nums.size(); i++)
			if (nums[index] != nums[i])
				nums[++index] = nums[i];
		return index + 1;
    }
};

// Solution 2
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        return distance(nums.begin(), unique(nums.begin(),nums.end()));
    }
};

// Solution 3
class Solution {
public:
	int removeDuplicates(vector<int>& nums) {
		return removeduplicates(nums.begin(), nums.end(), nums.begin()) - nums.begin();
	}

private:
	template< typename InIt, typename OtIt>
	OtIt removeduplicates(InIt first, InIt last, OtIt output) {
		while (first != last) {
			*output++ = *first;
			first = upper_bound(first, last, *first);
		}
	    return output;
	}
};