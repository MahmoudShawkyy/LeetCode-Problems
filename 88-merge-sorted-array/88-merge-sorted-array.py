class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp=[]
        for i in range(m):
            temp.append(nums1[i])
        for i in range(n):
            temp.append(nums2[i])
        temp.sort()
        nums1.clear()
        for i in temp:
            nums1.append(i)
        