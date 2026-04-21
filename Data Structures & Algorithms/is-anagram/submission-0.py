class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ints = {}
        intt = {}
        for i in range(len(s)):
            if s[i] not in ints:
                ints[s[i]] = 1
            else:
                ints[s[i]] += 1
        for i in range(len(t)):
            if t[i] not in intt:
                intt[t[i]] = 1
            else:
                intt[t[i]] += 1
        if ints == intt:
            return True
        else:
            return False                     
        