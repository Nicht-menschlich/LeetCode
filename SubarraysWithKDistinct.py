class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        arrays = []
        for i in range(len(A)):
            subArray = []
            subCount = 0
            for c in range(i, len(A)):
                curNum = A[c]
                if curNum not in subArray:
                    subCount += 1
                if subCount <= K:
                    subArray += [curNum]
                if subArray not in arrays:
                    arrays += [str(subArray)]
        return len(arrays)