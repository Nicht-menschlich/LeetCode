from typing import List


class Solution:
    def isTwoBitCharacter(self, bits: List[int], i: int) -> bool:
        if bits[i] == 1:
            return True
        return False
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i < len(bits):
            if i == len(bits)-2:
                print(not self.isTwoBitCharacter(bits, i))
                return not self.isTwoBitCharacter(bits, i)
            elif i == len(bits)-1:
                return True
            else:
                if self.isTwoBitCharacter(bits, i):
                    i += 2
                else:
                    i += 1
