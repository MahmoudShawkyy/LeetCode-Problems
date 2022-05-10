class Solution {
    
        vector<vector<int>>answer;
        vector<int>combination;
    
    void solve(int n,int k,int num,int sum,vector<int>combination)
   {
            if(k==0)
            {
                if(sum==n)
                 answer.push_back(combination);
                return;
            }
            for(int i=num;i<=9;i++)
            {
                combination.push_back(i);
                solve(n,k-1,i+1,sum+i,combination);
                combination.pop_back();
            }
    }
    public:
    vector<vector<int>> combinationSum3(int k, int n) {

        
        solve(n,k,1,0,combination);
        return answer;
    }
};