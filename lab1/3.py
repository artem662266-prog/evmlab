class Solution:
    def lengthOfLongestSubstring(self, s):
        max_len = 0

        for i in range(len(s)):
            seen = set()
            length = 0
            for j in range(i, len(s)):
                if s[j] in seen:
                    break
                seen.add(s[j])
                length += 1
            max_len = max(max_len, length)

        return max_len
