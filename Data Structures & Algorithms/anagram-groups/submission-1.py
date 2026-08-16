class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        an_map = defaultdict(list)
        result = []

        for s in strs:
            sorted_s = tuple(sorted(s))
            an_map[sorted_s].append(s)

        for group in an_map.values():
            result.append(group)
        return result
