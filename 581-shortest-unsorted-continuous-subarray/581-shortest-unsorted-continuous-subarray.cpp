class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        vector<int>sorted;
        int answer,a=0,b=0;
        if(is_sorted(nums.begin(),nums.end()))
            return 0;
        for(int i=0;i<nums.size();i++)
            sorted.push_back(nums[i]);
        sort(sorted.begin(),sorted.end());
        for(int i=0;i<nums.size();i++)
            if(nums[i]!=sorted[i])
            {
                a=i+1;
                break;
            }
        for(int i=nums.size()-1;i>=0;i--)
            if(nums[i]!=sorted[i])
            {
                b=i+1;
                break;
            }
        
        answer=b-a+1;
        return answer;
        
    }
};
