class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
       set<vector<int>>st;
        vector<vector<int>>answer;
        vector<int>temp=nums;
        do{
            next_permutation(temp.begin(),temp.end());
            st.insert(temp);
          }while(temp!=nums);
           for(auto it:st)
            {answer.push_back(it);}
        return answer;
    }
};