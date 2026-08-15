class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()

        for i, num in enumerate(nums): #tracks number and indice
            needed = target - num

            if needed in seen:
                return [seen.get(needed), i]

            seen[num] = i #sees number and tracks indice
            