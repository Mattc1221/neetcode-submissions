class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # S: O(Nlog(N)) M: O(N + M)
        # return sorted(s) == sorted(t)
        if len(s) != len(t): return False
        smap, tmap = {}, {}
        for i in range(len(s)):
            smap[s[i]] = 1  if s[i] not in smap else smap[s[i]] + 1
            tmap[t[i]] = 1  if t[i] not in tmap else tmap[t[i]] + 1
        return smap == tmap

        

