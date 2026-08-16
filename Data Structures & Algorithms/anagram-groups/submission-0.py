class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {} #create hashmap
        result = [] #list return

        for s in strs:
            sorted_s = tuple(sorted(s)) #sorted method returns list(mutable) alphabetical order, tuple makes it immutable list
            if sorted_s not in anagram_map:
                anagram_map[sorted_s] = [] #initialize key
            anagram_map[sorted_s].append(s) #add key to hashmap
        for group in anagram_map.values():
            result.append(group)
        return result
    
        print(anagram_map)
