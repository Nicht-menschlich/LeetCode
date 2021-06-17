# https://leetcode.com/problems/count-of-matches-in-tournament/
class Solution:
    def gamesPlayed(self, n: int) -> int:
        if n % 2 == 0:
            playersInAdvance = n / 2
            gamesAdd = n / 2
        else:
            playersInAdvance = (n - 1) / 2 + 1
            gamesAdd = (n - 1) / 2
        if n == 1:
            matches = gamesAdd
        else:
            matches = self.gamesPlayed(playersInAdvance) + gamesAdd
        return matches

    def numberOfMatches(self, n: int) -> int:
        return int(self.gamesPlayed(n))
