class Solution:
    def __init__(self):
        pass

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_hash = {}
        for n, num in enumerate(nums):
            if target - num in num_hash:
                return [num_hash[target - num], n]
            else:
                num_hash[num] = n



result = Solution()
print(result.twoSum(nums = [2, 7, 11, 15], target = 9))