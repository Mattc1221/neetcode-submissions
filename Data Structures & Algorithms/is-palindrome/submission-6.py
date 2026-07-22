import re
class Solution:
    def isAN(self, c: str) -> bool:
        char = ord(c)
        return (char >= ord('a') and char <= ord('z')) or (char >= ord('A') and char <= ord('Z')) or (char >= ord('0') and char <= ord('9'))


    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i, j = 0, len(s) -1
        while i < j:
            if not self.isAN(s[i]):
                i = i + 1
                continue
            if not self.isAN(s[j]):
                j = j - 1
                continue
            if s[i] != s[j]:
                return False
            i = i + 1
            j = j - 1
        return True
            

