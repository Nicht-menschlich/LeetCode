#https://leetcode.com/problems/add-digits/
class Solution:
    def addDigits(self, num: int) -> int:
        while True:
            string = str(num)
            if len(string) == 1:
                return int(string)
            num = 0
            for i in list(string):
                num += int(i)