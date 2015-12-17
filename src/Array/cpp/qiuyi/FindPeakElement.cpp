class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int m = nums.size();
        int i=0, j=m;

        while (i <= j) {
            int mid = (j-i)/2+i;
            if (mid == 0 && nums[mid] > -1 && nums[mid] > nums[mid+1])
                return mid;
            else if (mid == m-1 && nums[mid] > nums[mid-1])
                return mid;
            if (nums[mid]<nums[mid-1])
                j = mid - 1;
            else if (nums[mid]<nums[mid+1])
                i = mid + 1;
            else
                return mid;
        }
    }
};