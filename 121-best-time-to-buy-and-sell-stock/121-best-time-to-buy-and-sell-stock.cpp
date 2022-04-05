class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxi=0,mini=100000;
        for(int i=0;i<prices.size();i++)
        {
            mini=min(mini,prices[i]);
            maxi=max(maxi,prices[i]-mini);
        }
        return maxi;
        
        
        
    }
};