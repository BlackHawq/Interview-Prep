#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
    public:
        vector<int> twoSum(vector<int>& nums, int target){
            unordered_map<int,int> seen;

            for (int i = 0; i < nums.size(); ++i) {
                int complement = target - nums[i];

                if (seen.find(complement)!= seen.end()) {
                    return {seen[complement], i};
                } else {
                    seen[nums[i]] = i;
                }
            }
            return {};
        }
};

int main() {
    Solution solution;
    vector<int> nums = {1,2,3,4,5};
    int target = 5;
    vector<int> result = solution.twoSum(nums, target);

    cout<< result[0] << " " << result[1] << endl;
    return 0;
}