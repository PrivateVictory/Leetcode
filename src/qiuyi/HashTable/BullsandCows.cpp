class Solution {
public:
    string getHint(string secret, string guess) {
        int bulls = 0, cows = 0;
        int n = secret.size();
        int s_map[10] = {0};
        int g_map[10] = {0};

        for (int i = 0; i < n; i++) {
            char s = secret[i];
            char g = guess[i];
            if (g == s)
                bulls++;
            else {
                (s_map[g-'0']>0) ? s_map[g-'0']--,cows++ : g_map[g-'0']++;
                (g_map[s-'0']>0) ? g_map[s-'0']--,cows++ : s_map[s-'0']++;
            }
        }
        
        
        return to_string(bulls) + "A" + to_string(cows) + "B";
    }
};