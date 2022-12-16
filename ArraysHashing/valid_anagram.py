class Solution:
    def __inti__(self):
        pass

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_letters = {}
        t_letters = {}

        for i in range(len(s)):
            s_letters[s[i]] = 1 + s_letters.get(s[i], 0)
            t_letters[t[i]] = 1 + t_letters.get(t[i], 0)
        for c in s_letters:
            if s_letters[c] != t_letters.get(c, 0):
                return False

        # return sorted(s) == sorted(t)
        # return Counter(s) == Counter(t)

result = Solution()
print(result.isAnagram(s = "a", t = "b"))
