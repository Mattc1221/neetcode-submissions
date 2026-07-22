class Solution:
    def _solution1(self, strs: List[str]) -> List[List[str]]:
        # Sorting - same letters, same word when sorted
        # { sort(str1): [str1], sort(str2) }
        # [ str1, str2, str3 ]
        # M: O(n) C: O(n m log (m) )

        m = dict()
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in m:
                # GOTCHA this function edits the value.
                m[sorted_s].append(s)            
            else:
                m[sorted_s] = [s]
        return list(m.values())
    
    def hash(self, s: str) -> str:
        count = [0] * 26
        for c in s:
            pos = ord(c) - ord('a')
            count[pos] += 1
        return tuple(count)

    def _solution2(self, strs: List[str]) -> List[List[str]]:
        # Sorting - same letters, same word when sorted
        # { sort(str1): [str1], sort(str2) }
        # [ str1, str2, str3 ]
        # M: O(n) C: O(n m log (m) )
        # [ a, ..., z ]
        # [ 1, 5, ..., ] -> abbbbb
        # "Z E B R A"
        #    i 
        # insert_location = ord(str[i]) - ord("a")
        # [  1  1  0  0  1  0  0  0  0  0  0  0  0  0  0  0  0  1  0  0  0  0  0  0  0  1 ]
        # [  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z ]
        # M: O(n) C: O(n)
        # GOTCHA - LISTS ARE NOT HASHABLE

        m = dict()
        for s in strs:
            sorted_s = self.hash(s)
            if sorted_s in m:
                # GOTCHA this function edits the value.
                m[sorted_s].append(s)            
            else:
                m[sorted_s] = [s]
        return list(m.values())

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return self._solution2(strs)

