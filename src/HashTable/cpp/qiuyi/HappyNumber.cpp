class Solution {
public:
    bool isHappy(int n) {
        unordered_set<int> cache;
        int sum = 0;
        
        while (true) {
            if (n == 0) {
                if (sum == 1) return true;
                n = sum;
                auto pos = cache.find(sum);
                if (pos != cache.end())
                    return false;
                else
                    cache.insert(sum);
                sum = 0;
            }
            int num = n % 10;
            sum += num * num;
            n = n / 10;
        }
    }
};