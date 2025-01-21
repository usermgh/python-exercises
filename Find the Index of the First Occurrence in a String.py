class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        array = list(haystack)
        find = list(needle)
        return haystack.find(needle)

x = Solution()
result = x.strStr('leetcode','leeto')
print(result)        