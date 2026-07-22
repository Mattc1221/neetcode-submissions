class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        [ Hello, World ]
        > len1,len2,len3,lenN|HelloWorld

        n = len strs
        C: O(n)
        M: O(1)
        """
        joined = ''.join(strs)
        lens = ','.join([str(len(s)) for s in strs])
        return lens + "|" + joined

    def decode(self, s: str) -> List[str]:
        """
        C: 
        M: 
        """
        str_lens, joined = s.split('|', 1)
        if len(str_lens) == 0: return []
        lens = [int(s) for s in str_lens.split(',')]
        strs = []
        i = 0
        for l in lens:

            strs.append(joined[i:i+l])
            i += l
            # strs.append(joined[0:l])
            # joined = joined[l:]
        return strs
