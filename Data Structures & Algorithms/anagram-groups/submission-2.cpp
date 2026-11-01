class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> result; // result list of groups
        unordered_map<string, vector<string>> groupings; // hash (key, value) --> (sorted(string), group of strings)
        //sort the string alphabetically add as key and add the origional string to the associated alphabetic order
        for(string s : strs){
            string sorted = s; // copy the string
            sort(sorted.begin(), sorted.end()); // sort the copy
            groupings[sorted].push_back(s); //insert the copy as key, insert string as value
        }
        //auto& , means that the compiler will figure out the data type '&' means to reference the origional hash
        for(auto& group : groupings){ //iterate through the hash
            result.push_back(group.second); // for each group, take the value, which is the list of strings, and add to result
        }
        return result;
    }
    
};
