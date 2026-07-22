class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        [ Hello, World ]
        > len1,len2,len3,lenN|HelloWorld
        """
        joined = ''.join(strs)
        lens = ','.join([str(len(s)) for s in strs])
        return lens + "|" + joined

    def decode(self, s: str) -> List[str]:
        str_lens, joined = s.split('|', 1)
        if len(str_lens) == 0: return []
        lens = [int(s) for s in str_lens.split(',')]
        strs = []
        for l in lens:
            strs.append(joined[0:l])
            joined = joined[l:]
        return strs
