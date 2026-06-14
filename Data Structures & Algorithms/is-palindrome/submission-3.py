class Solution:
    def isPalindrome(self, s: str) -> bool:
        acceptable=lambda x:x.isalpha() or x in [str(i) for i in range(0,10)]
        chars=[c.lower() for c in s if acceptable(c) and c!=" "]
        l,r=0,len(chars)-1
        while l<r:
            left=chars[l]
            right=chars[r]
            print(left,right)
            if left!=right:
                return False
            l+=1
            r-=1
        return True