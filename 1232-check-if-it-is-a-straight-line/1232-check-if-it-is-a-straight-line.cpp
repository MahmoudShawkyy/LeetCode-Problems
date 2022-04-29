class Solution {
public:
    bool checkStraightLine(vector<vector<int>>& coordinates) {
        int n=coordinates.size();
        int dx=coordinates[n-1][0]-coordinates[0][0];
        int dy=coordinates[n-1][1]-coordinates[0][1];
        for(int i=1;i<coordinates.size();i++)
           {
            int dxx=coordinates[i][0]-coordinates[0][0];
            int dyy=coordinates[i][1]-coordinates[0][1];
            if(dx*dyy!=dy*dxx) return false;
            
            }
        return true;
                
            
    }
};