class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        vector<int>answer;
        int n=nums2.size();
        vector<int>check(n,1);           
        for(int i=0;i<nums1.size();i++)
            for(int j=0;j<nums2.size();j++)
                if(nums1[i]==nums2[j]&&check[j])
                   {
                    answer.push_back(nums1[i]);
                    check[j]=0;
                    break;
                    
                   }
        return answer;
    }
};