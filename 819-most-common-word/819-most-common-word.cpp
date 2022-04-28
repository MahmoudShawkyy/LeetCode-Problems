class Solution {
public:
    string mostCommonWord(string paragraph, vector<string>& banned) {
        vector<string>words;
        string str="";
        for(int i=0;i<paragraph.length();i++)
        {
            if(isalpha(paragraph[i]))
                str+=tolower(paragraph[i]);
            else
            {
             if(str!="")
                words.push_back(str);
                str="";
            }
            
        }
        if(isalpha(paragraph[paragraph.length()-1]))
        {
             words.push_back(str);
        }
        
        vector<string>valid;
        for(int i=0;i<words.size();i++)
            if(find(banned.begin(),banned.end(),words[i])==banned.end())
                valid.push_back(words[i]);

             
         map<string,int>freq;
         sort(valid.begin(),valid.end());
         int counter=-1;
         string answer;
         for(int i=0;i<valid.size();i++)
             freq[valid[i]]++;
        
          for(auto i:freq)
          {
              if(i.second>counter)
              {
                  counter=i.second;
                  answer=i.first;
              }
          }
        
        
        return answer;
};
    
};