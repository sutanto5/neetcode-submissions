class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::map<int, int> m = {};

        for (int i =0; i < nums.size(); i++) {
            if(m.find(nums[i]) != m.end()){
                return 1;
            }
            else {
                m.insert({nums[i], 1});
            }
        }
        return 0;
    }
};