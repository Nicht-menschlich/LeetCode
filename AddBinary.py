class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        finalBin = ""
        length = len(a)
        if len(b) > length:
            length = len(b)
        aList = list(a)
        bList = list(b)
        current, nxt = "", False
        print(length)
        for i in range(length):
            curNext = nxt
            iA, iB = "0", "0"
            if i < len(aList):
                iA = aList[len(aList)-i-1]
            if i < len(bList):
                iB = bList[len(bList)-i-1]
            current, nxt = self.checkBin(iA, iB, curNext)
            finalBin = current + "" + finalBin
            print(iA + iB)
            print(current)
            print(finalBin)
        if nxt:
            finalBin = "1" + finalBin
        print(nxt)
        return finalBin

    def checkBin(self, first, second, nxt):
        if first == "1" and second == "1":
            if nxt:
                return "1", True
            return "0", True
        elif first == "0" and second == "0":
            if nxt:
                return "1", False
            return "0", False
        if nxt:
            return "0", True
        return "1", False