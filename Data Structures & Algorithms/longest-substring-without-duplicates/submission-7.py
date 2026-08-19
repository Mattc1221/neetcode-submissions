class Solution:
    def lastSeenAtDict(self, s: str) -> int:
        if len(s) == 0: return 0

        max_len = 1
        i, j = 0, 1
        last = { s[i]: 0 }

        while j < len(s):
            if s[j] in last and last[s[j]] >= i:
                i = last[s[j]] + 1
            last[s[j]] = j
            j += 1
            max_len = max(max_len, j - i)
        return max_len


    def shrinkingSoln(self, s: str) -> int:
        if len(s) <= 1: return len(s)

        max_len = 1
        i, j = 0, 1
        seen = { s[0] }
        while j < len(s):
            if s[j] not in seen:
                seen.add(s[j])
                j += 1
                max_len = max(len(seen), max_len)
            else:
                seen.remove(s[i])
                i += 1
        return max_len

    def lengthOfLongestSubstring(self, s: str) -> int:
        return self.lastSeenAtDict(s)

