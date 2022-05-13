class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int>::iterator it;
        vector<int>answer;
        for(int i=0;i<nums.size();i++)
        {
            it=find(nums.begin(),nums.end(),target-nums[i]);
            if(it!=nums.end()&&it-nums.begin()!=i)
            {
                answer.push_back(i);
                answer.push_back(it-nums.begin());
                return answer;
            }
                
        }
        return answer;
    }
};