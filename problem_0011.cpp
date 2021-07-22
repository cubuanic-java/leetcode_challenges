class Solution {
public:
    int maxArea(vector<int>& height) 
    {
        // leetcode specific hack
        ios::sync_with_stdio(false);
        cin.tie(NULL);
        
        int left = 0;
        int N = height.size();
        int right = N-1;
        int best_area = 0;
        int curr_area = 0;
        
        for (int i=0; i < N; i++) 
        {
            if(height[left] < height[right]) {
                curr_area = (right - left) * height[left++];
            } else {
                curr_area = (right - left) * height[right--];
            }
            
            if (best_area < curr_area) best_area = curr_area;
        }
        return best_area;
    }
};