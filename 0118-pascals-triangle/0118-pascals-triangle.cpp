class Solution {
public:
    vector<int> fun(int n){
        vector<int> temp(n);  // because we have use indexing soooo giving size is compulsory
       long long  int a=1;   // always remember factorial type question requies long long 
        temp[0]=1;
        for(int j=1;j<n;j++){
            a=a*(n-j);
            a=a/j;
            temp[j]=a;
        }
            return temp;
    }
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> ans;
        vector<int> mid;
        for(int i=1;i<=numRows;i++){
           mid=fun(i);
            ans.push_back(mid);
        }
        return ans;
    }
    
};