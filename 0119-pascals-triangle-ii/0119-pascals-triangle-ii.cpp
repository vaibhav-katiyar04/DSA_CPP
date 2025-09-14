class Solution {
public:
    //two ways
    //use optimize n-1 C r-1  .....run only number of r times O(n*r)
    // optimize way finding formula O(n)
    vector<int> getRow(int rowIndex) {
        vector<int> ans(rowIndex+1);
        long long int a=1;
        ans[0]=1;
        for(int i=1;i<=rowIndex;i++){
            a=a*(rowIndex+1-i);
            a=a/i;
            ans[i]=a;
        }
       return ans;
    }
};