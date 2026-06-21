class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        window_count = [0] * 26

        for i in range(len(s1)):
            s1_idx = ord(s1[i]) - ord('a')
            s2_idx = ord(s2[i]) - ord('a')
            s1_count[s1_idx] += 1
            window_count[s2_idx] += 1

        if s1_count == window_count:
            return True
            

        l = 0
        r = len(s1)
        while r < len(s2):
            right_index = ord(s2[r]) - ord('a')
            window_count[right_index] +=1

            left_index = ord(s2[l]) - ord('a')
            window_count[left_index] -=1

            l+=1
            r+=1

            if s1_count == window_count:
                return True
        return False

            
        