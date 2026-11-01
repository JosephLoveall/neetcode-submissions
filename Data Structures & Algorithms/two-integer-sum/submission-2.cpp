class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> tracker; // create the hash, index i , index j 
        
        for(int i = 0; i < nums.size(); i++){ // iterate through the array
            int needed = target - nums[i]; // find the number that would add to our target
            if(tracker.count(needed) >  0){ // see if that number is one we have in our hash
             vector<int> result = {tracker[needed], i}; //store the two indexes then return
             return result;
            }
            tracker[nums[i]] = i; // add to our list 
        }
    }
};
