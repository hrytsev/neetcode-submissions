class Solution:
    def checkInclusion(self,s1, s2):
        if len(s1) > len(s2):
            return False

        s_counter = Counter(s1)
        window_counter = defaultdict(int)

        length = len(s1)

        for i in range(length):
            window_counter[s2[i]] += 1

        if window_counter == s_counter:
            return True

        l = 0

        while l + length < len(s2):
            current = s2[l + length]
            prev = s2[l]

            window_counter[current] += 1
            window_counter[prev] -= 1

            if window_counter[prev] == 0:
                del window_counter[prev]

            l += 1

            if window_counter == s_counter:
                return True

        return False