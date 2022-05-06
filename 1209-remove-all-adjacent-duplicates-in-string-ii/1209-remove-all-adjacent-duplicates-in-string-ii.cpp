class Solution {
public:
    string removeDuplicates(string s, int k) {
        vector<int>freq(s.length(),1);
        stack<int>st;
        string str;
        st.push(0);
        for(int i=1;i<s.length();i++)
        {
            if(!st.empty())
                if(s[st.top()]==s[i])
                    freq[i]=freq[st.top()]+1;
            st.push(i);
            if(freq[i]==k)
                for(int i=0;i<k;i++)
                    st.pop();
            
            
            
            
            
        }
        
        while(!st.empty())
        {
            str+=s[st.top()];
            st.pop();
        }
        reverse(str.begin(),str.end());
        return str;
    }
};