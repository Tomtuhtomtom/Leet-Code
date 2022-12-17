
class Solution:
    def __init__(self):
        pass

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        num_count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            num_count[n] = 1 + num_count.get(n, 0)
        for n, c in num_count.items():
            freq[c].append(n)

        most_nums = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                most_nums.append(n)
                if len(most_nums) == k:
                    return most_nums

result = Solution()
print(result.topKFrequent(nums = [1,1,1,2,2,3], k = 2))