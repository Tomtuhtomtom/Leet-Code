import collections

class Solution:
    def __init__(self):
        pass

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_groups = collections.defaultdict(list)
        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter) - ord("a")] += 1
            anagram_groups[tuple(count)].append(word)
        return anagram_groups.values()


result = Solution()
print(result.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))


