class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for i in nums1:
            for j in nums2:
                if i==j:
                    ans.append(i)
                    nums2.remove(j)
                    break
        return ans
                    
        