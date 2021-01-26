class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        counter1, counter2, state = 0, 0, False
        while len(merged) < len(nums1) + len(nums2):
            if not state:


