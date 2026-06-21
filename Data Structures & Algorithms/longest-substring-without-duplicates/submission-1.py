class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        seenset = set()
        maxlen = 0

        while r < len(s):
            if s[r] not in seenset:
                seenset.add(s[r])
                currlen = r - l + 1
                maxlen = max(currlen, maxlen)
                r += 1
            else:
                seenset.remove(s[l])
                l += 1

        return maxlen