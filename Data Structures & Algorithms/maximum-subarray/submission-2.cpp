class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int sum = nums[0];
        int cur = 0;

        for ( int right = 0; right < nums.size(); right++ ) {
            cur += nums[right];
            sum = max(sum, cur);

            if ( cur < 0 ) {
                cur = 0;
            }
        }
        return sum;
    }
};
