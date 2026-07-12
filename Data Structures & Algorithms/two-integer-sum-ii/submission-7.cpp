class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        
        int l = 0;
        int r = numbers.size() - 1;
        
        while (l < r) {
            int total = numbers[l] + numbers[r];
            
            if (target == total) {
                return {l+1, r+1};
            }
            else if (target > total) {
                l++;
            }
            else {
                r--;
            }
        }
    }
};
