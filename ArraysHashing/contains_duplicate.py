
class Solution:
    def __init__(self):
        pass

    def containsDuplicate(self, nums: list[int]) -> bool:
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        return False

# class Solution:
#     def containsDuplicate(self, nums: list[int]) -> bool:
#         if len(nums) != len(set(nums)):
#             return True

result = Solution()
print(result.containsDuplicate(nums = [1,2,3,1]))