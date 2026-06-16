class Solution:
    def lengthOfLongestSubstring(self,s):
        if s=="":
            return 0
        n=len(s)
        l=0
        length=0
        max_l=1
        win_set=set()
        while l+length<n:
            current=s[l+length]
            if current not in win_set:
                length+=1
                win_set.add(current)
            else:
                if current==s[l]:
                    l+=1
                else:
                    win_set=set()
                    l=l+length+1
                    length=0
            max_l=max(max_l,length)
        return max_l