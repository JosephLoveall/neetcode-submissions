class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq =  [[] for _ in range(len(nums) + 1)] # creates an array of frequencies
        
        for i in nums:
            count[i] = count.get(i, 0) + 1 #gets count

        for n, c in count.items(): # gives each dictionary entry as a pair (n is key, c is value)
            freq[c].append(n) # go to the bucket at index c and add n to it

        result = []  #list where we will put most frequent elements

        for i in range(len(freq) - 1, 0 , -1): # <--- grabs results from the highest index which also is highest frequency
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result