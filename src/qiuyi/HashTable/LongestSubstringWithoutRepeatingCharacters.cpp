class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int> cache(256, -1);
        
        int len = 0;
        for (int r = 0, l = -1; r < s.size(); r++) {
            if (cache[s[r]] > l)
                l = cache[s[r]];
            cache[s[r]] = r;
            len = max(len, r-l);
        }
        return len;
    }
};