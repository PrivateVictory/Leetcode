class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        for (int i = digits.size()-1; i >= 0; i--) {
            digits[i] +=1;
            if (digits[i] > 9)
                digits[i] = 0;
            else
                break;
        }
        if (digits[0] == 0)
            digits.insert(digits.begin(), 1);
        
        return digits;
    }
};