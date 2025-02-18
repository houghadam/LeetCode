class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        shortest = len(strs[0])
        num_words = len(strs)
        prefix = ""
        for s in strs:
            if len(s) < shortest:
                shortest = len(s)
        for i in range(shortest):
            temp_prefix = strs[0][i]
            count = 0
            for s in strs:
                if s[i] == temp_prefix:
                    count += 1
            if count == num_words:
                prefix += temp_prefix
            else:
                return prefix
        return prefix


solution = Solution()
result = solution.longestCommonPrefix(strs=["cir", "car"])
print(result)
