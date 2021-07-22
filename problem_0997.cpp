// Runtime: 16 ms, faster than 99.71% of C++ 
// online submissions for Squares of a Sorted Array.

class Solution {
public:
    vector<int> sortedSquares(vector<int>& A) 
    {
        // Leetcode specific optimization
        ios::sync_with_stdio(false);
        cin.tie(NULL);

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