class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0: return 0

        i, j = 0, 1
        seen = { s[i]: 1}
        max_freq = 1
        max_seq = 1
        while j < len(s):
            if s[j] in seen:seen[s[j]] += 1
            else: seen[s[j]] = 1

            max_freq = max(max_freq, seen[s[j]])
            r = (j - i + 1) - max_freq
            if r <= k: 
                max_seq = max(max_seq, j - i + 1)
            else: 
                seen[s[i]] -= 1
                i += 1
            j += 1
        return max_seq
        
