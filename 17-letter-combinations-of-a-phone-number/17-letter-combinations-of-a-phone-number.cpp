class Solution {
public:
    vector<string> letterCombinations(string digits) {
       vector<string> v={"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        vector<string>ans;
        if(!digits.size())
            return ans;
        ans.push_back("");
        for(int i=0;i<digits.size();i++)
        {
            vector<string>temp;
            string str=v[digits[i]-'0'];
            for(int j=0;j<ans.size();j++)
                for(int k=0;k<str.length();k++)
                    temp.push_back(ans[j]+str[k]);
            swap(ans,temp);
        }
        return ans;
    
    }
};