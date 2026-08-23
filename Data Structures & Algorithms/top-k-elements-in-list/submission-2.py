class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        array = [[] for  _ in range(len(nums) + 1)] #create a list of empty lists (one for each index from 0 to len(nums))
        result = []

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        for n, c in freq.items():
            array[c].append(n)
        
        n = len(array) - 1
        while k != 0:
            listIWant= array[n]
            if len(listIWant) != 0:
                for i in listIWant:
                    result.append(i)
                    k = k - 1
            n = n - 1
        return result