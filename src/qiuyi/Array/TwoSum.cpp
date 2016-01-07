// Solution 1 in O(NlgN)
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ret;
        int sum;

        for (int j = nums.size()-1; j > 0; j--) {
            sum = nums[j];
            for (int i = 0; i < j; i++) {
                sum += nums[i];
                if (sum == target) {
                    ret.push_back(i+1);
                    ret.push_back(j+1);
                    break;
                }
                else                    
                    sum -= nums[i];
            }
        }
        return ret;
    }
};

// Solution 2 in O(N)
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ret;
        unordered_map<int, int> mapping;
        
        for (int i = 0; i < nums.size(); i++)
            mapping[nums[i]] = i;
        for (int i = 0; i < nums.size(); i++) {
            int gap = target - nums[i];
           if (mapping.find(gap) != mapping.end() && mapping[gap] > i) {
               ret.push_back(i+1);
               ret.push_back(mapping[gap]+1);
               break;
           }
        }
        return ret;
    }
};