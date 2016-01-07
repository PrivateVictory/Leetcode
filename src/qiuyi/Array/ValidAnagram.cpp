// Solution 1
class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;
        unordered_multiset<char> st(t.cbegin(), t.cend());
        
        for (auto i : s) {
            auto pos = st.find(i);
            if (pos != st.end())
                st.erase(pos);
            else
                return false;
        }
        return true;
    }
};

// Solution 2
class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;
        int n = s.size();
        unordered_map<char, int> count;
        
        for (int i = 0; i < n; i++) {
            count[s[i]]++;
            count[t[i]]--;
        }
        for (auto i : count)
            if (i.second != 0)
                return false;
        
        return true;
    }
};

// Solution 3
class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;
        int n = s.size();
        const int charnum = 26;
        vector<int> count(charnum, 0);
        
        for (int i = 0; i < n; i++) {
            count[s[i]-'a']++;
            count[t[i]-'a']--;
        }
        for (int i = 0; i < charnum; i++)
            if (count[i] != 0)
                return false;
        
        return true;
    }
};
