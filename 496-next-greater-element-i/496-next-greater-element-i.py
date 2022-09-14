class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer=[]
        for n1 in nums1:
            check=True
            i=nums2.index(n1)
            for j in range(i,len(nums2)):
                if nums2[j]>n1:
                    answer.append(nums2[j])
                    check=False
                    break
            if check :
                answer.append(-1)
        return answer
        