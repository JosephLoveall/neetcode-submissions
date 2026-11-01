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

/*solution summarry report :
First create a result variable, and hashmap -- determine hash's key values.
Iterate through the origional array.
To find like strings, make a copy of the current string your on.
Sort that copy alphabetically, sort(sorted.begin(), sorted.end()), then add to hash as key.
Then whatever the string was will be the value to that key. 
Now that we have our hash we must iterate through it and append the values into the return array of arrays.
We use a range loop, using "auto&" as the datatype identifier for this , and we choose the value portion of the hashmap when we add it to the array we are returning.
Return array.
*/
