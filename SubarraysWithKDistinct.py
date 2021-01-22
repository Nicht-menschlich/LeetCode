#https://leetcode.com/problems/subarrays-with-k-different-integers/
class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        #this code does work but leetcode has an exceeded time limit
        counter = 0
        for i in range(len(A)):
            subArray = []
            subCount = 0
            for c in range(i, len(A)):
                curNum = A[c]
                if curNum not in subArray:
                    subCount += 1
                if subCount <= K:
                    subArray += [curNum]
                else:
                    break
                if subCount == K:
                    print(subArray)
                    counter += 1
        return counter