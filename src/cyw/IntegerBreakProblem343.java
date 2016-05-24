package com.cyw.test;

public class IntegerBreakProblem343 {
    public int integerBreak(int n) {
        if (n == 2 || n == 3) {
            return n - 1;
        }
        int base = 1;
        while (n > 4) {
            base *= 3;
            n -= 3;
        }
        return base * n;
    }
}
