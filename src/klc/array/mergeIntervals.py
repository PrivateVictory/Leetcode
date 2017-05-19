'''
Problem: Given a collection of intervals, modify the collection such that 
overlapping intervals are merged. Return the new collection. 
Approach: First, sort the intervals by start index. Iterate through the collection
and check if interval i's start index is <= the last interval's end. If it is, update the ending 
of the collection. Otherwise, the interval is not overlapping and we add it without modification. Runs in O(n) time.
'''
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
# 
class Solution(object):
    def merge(self, intervals):
        merged = []
        for interval in sorted(intervals, key=lambda interval: interval.start):
            if merged and interval.start <= merged[-1].end:
                merged[-1].end = max(merged[-1].end, interval.end)
            else:
                merged += interval,
        return merged
