__author__ = 'lenovo'
class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        left = 0
        right = len(A) - 1
        while left <= right:
            if A[left] == elem:
                A[left], A[right] = A[right], A[left]
                right -= 1
            else:
                left += 1
        return left