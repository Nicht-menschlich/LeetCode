class Solution:
    def isPalindrome(self, s : str):
        if len(s) %2 == 0:
            for i in range(int(len(s)/2)):
                if list(s)[i] == list(s)[len(s)-i-1]:
                    continue
                return False
            return True
        else:
            for i in range(int((len(s)-1)/2)):
                if list(s)[i] == list(s)[len(s)-i-1]:
                    continue
                return False
            return True
    def longestPalindrome(self, s: str) -> str:
        if self.isPalindrome(s):
            return s
        longest = ""
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if j-i > len(longest):
                    if self.isPalindrome(s[i:j]):
                        longest = s[i:j]

        return longest

