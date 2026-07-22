import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i, j = 0, len(s) - 1
        pattern = r"[A-Za-z0-9]"
        while i < j:
            if not re.search(pattern, s[i]):
                i = i + 1
                continue
            if not re.search(pattern, s[j]):
                j = j - 1
                continue
            if s[i] == s[j]:
                i = i + 1
                j = j - 1
                continue
            return False
        return True
