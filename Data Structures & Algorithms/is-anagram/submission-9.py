class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # S: O(n log(n) + m log(m)) M: O(n + m)
        # return sorted(s) == sorted(t)

        # S: O(m + n) M: O(1)
        # NOTE: remember - memory in this case is bound by the corpus of different input characters (i.e. 26 -> O(1)). Always clarify the input conditions
        # if len(s) != len(t): return False
        # smap, tmap = {}, {}
        # for i in range(len(s)):
        #     smap[s[i]] = 1  if s[i] not in smap else smap[s[i]] + 1
        #     tmap[t[i]] = 1  if t[i] not in tmap else tmap[t[i]] + 1
        # return smap == tmap

        # S: O(m + n) M: O(1)
        # NOTE: Struggled on this to map letters to 0 to 25. Did not know the ord function was available.
        if len(s) != len(t): return False
        counters = [0] * 26
        a = ord("a")
        for i in range(len(t)):
            s_char, t_char = ord(s[i]) - a, ord(t[i]) - a
            counters[s_char] = counters[s_char] - 1
            counters[t_char] = counters[t_char] + 1

        for count in counters:
            if count != 0:
                return False
        return True
