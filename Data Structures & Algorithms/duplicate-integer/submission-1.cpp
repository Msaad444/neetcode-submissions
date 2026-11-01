#include <unordered_set>

using namespace std;

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> myset;
        
        for(int i: nums){
            if(myset.count(i)){
                return true;
            }
            myset.insert(i);
    }
        return false;
    }
};