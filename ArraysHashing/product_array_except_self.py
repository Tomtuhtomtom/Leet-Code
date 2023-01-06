import math

nums = [1,2,3,4]

class Solution:
    def __init__(self):
        pass

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        answer = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]
        return answer


result = Solution()
print(result.productExceptSelf(nums))

