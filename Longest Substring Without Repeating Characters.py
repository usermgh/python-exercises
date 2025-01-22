class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = set()
        left = 0
        max_length = 0
        for i in range(len(s)):
            while s[i] in result:
                result.remove(s[left])
                left += 1
           
            result.add(s[i])

            max_length = max(max_length, i - left + 1)
        return max_length

x = Solution()
result = x.lengthOfLongestSubstring("pwwkew")
print(result)