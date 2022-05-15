class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& mat, int r, int c) {
        vector<int>temp,temp2;
        vector<vector<int>>answer;
        int n=mat.size(),m=mat[0].size();
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
                temp.push_back(mat[i][j]);
        int index=0;
        if(n*m!=r*c)
            return mat;
            
        for(int i=0;i<r,index<n*m;i++)
        {
            for(int j=0;j<c;j++)
            {
                temp2.push_back(temp[index]);
                index++;
            }
            
            answer.push_back(temp2);
            temp2.clear();
        }
        return answer;
    }
};