class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        mx=len(students)
        stds=deque(students)
        meals=deque(sandwiches)
        cnt=0
        while cnt!=mx:
            if stds[0]!=meals[0]:
                x=stds.popleft()
                stds.append(x)
                cnt+=1
            else:
                stds.popleft()
                meals.popleft()
                mx=len(stds)
                cnt=0
        return len(stds)