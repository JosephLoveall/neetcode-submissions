class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = dict()
        for c in s:
            x[c] = x.get(c, 0) + 1
        for c in t:
           x[c] = x.get(c, 0) - 1
    
        for v in x.values():
            if v != 0 :
                return False

        return True



