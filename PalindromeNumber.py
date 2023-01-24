#https://leetcode.com/problems/palindrome-number/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_str = str(x)
        length = len(num_str)
        half = int(length/2)
        for i in range(half):
            if num_str[i] != num_str[length-i-1]:
                return False
        return True




