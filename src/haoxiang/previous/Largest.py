__author__ = 'haoxiang'

def largestNumber( nums):
    map = {}
    for i in range(len(nums)):
        key = str(nums[i])
        map[key[0]] = str(nums)
    dict= sorted(map.iteritems(), key=lambda d:d[0])
    for j in dict:
        str = str(''.join(j))
    print(str)

test = [1,6,67,90]
largestNumber(test)