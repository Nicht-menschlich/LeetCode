#https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        strList = list(s)
        maxLen = 0
        for i in range(len(s)):
            subStr = ""
            for c in range(i, len(s)):
                curChar = strList[c]
                if curChar not in subStr:
                    subStr += curChar
                else:
                    break
            if len(subStr) > maxLen:
                maxLen = len(subStr)
        return maxLen
