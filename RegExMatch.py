#https://leetcode.com/problems/regular-expression-matching/submissions/
import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        match = re.match(p, s)
        if not match:
            return False
        return match.group() == s