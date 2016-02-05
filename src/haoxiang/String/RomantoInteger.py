class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        numerals = [
        {'letter': 'M', 'value': 1000},
        {'letter': 'D', 'value': 500},
        {'letter': 'C', 'value': 100},
        {'letter': 'L', 'value': 50},
        {'letter': 'X', 'value': 10},
        {'letter': 'V', 'value': 5},
        {'letter': 'I', 'value': 1},
        ]
        index_by_letter = {}
        for index in xrange(len(numerals)):
            index_by_letter[numerals[index]['letter']] = index

        result = 0
        previous_value = None
        for letter in reversed(s):
            index = index_by_letter[letter]
            value = numerals[index]['value']
            if (previous_value is None) or (previous_value <= value):
                result += value
            else:
                result -= value
            previous_value = value

        return result
