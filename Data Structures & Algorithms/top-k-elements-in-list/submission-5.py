class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        intme = {}
        freq = [[] for _ in range(len(nums)+1)]

        for i in nums:
            if i not in intme:
                intme[i] = 1
            else:
                intme[i] += 1

        for n, c in intme.items(): 
            freq[c].append(n)

        res = []

        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res