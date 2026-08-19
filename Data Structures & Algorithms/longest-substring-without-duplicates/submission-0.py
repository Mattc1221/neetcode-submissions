class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1: return len(s)

        max_len = 1
        i, j = 0, 1
        seen = { s[0] }
        while j < len(s):
            if s[j] not in seen:
                seen.add(s[j])
                j += 1
            else:
                seen.remove(s[i])
                i += 1
            max_len = max(len(seen), max_len)
        return max_len

