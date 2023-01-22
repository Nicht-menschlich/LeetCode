#https://leetcode.com/problems/string-to-integer-atoi/
import re


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        match = re.search(r'^[+-]?\d+', s)
        if not match:
            return 0
        num_str = match.group()

        num = int(num_str)
        #print(num)

        if num > (2**31)-1:
            #print(1)
            return (2**31)-1
        elif num < (-2**31):
            #print(2)
            return (-2**31)
        #print(3)
        return num


