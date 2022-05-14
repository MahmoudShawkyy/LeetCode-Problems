class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int answer=0,profit=0,temp=INT_MAX;
        for(int i=0;i<prices.size();i++)
        {
            if(prices[i]<temp)
                temp=prices[i];
            profit=prices[i]-temp;
            if(profit>answer)
                answer=profit;
    }
        return answer;
        
        
    }
};