class Solution {
public:
    vector<int> sortedSquares(vector<int>& A) {
        vector<int> res(A.size());      
        int l = 0;
        int r = A.size() - 1;
        
        for (int i = r; i >= 0; i--) {          
            if (abs(A[l]) > abs(A[r])) {
                res[i] = A[l] * A[l++];
            } else {
                res[i] = A[r] * A[r--];
            }
        }
        
        return res;
    }
};