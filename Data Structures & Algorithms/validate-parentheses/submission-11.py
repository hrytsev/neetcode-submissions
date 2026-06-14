class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==1:
            return False
        bra={"]":"[","}":"{",")":"("}
        stack=[]
        for v in s:
            print(v,stack)
            if v not  in bra:
                stack.append(v)
            else:
                if stack and stack[-1]==bra[v]:
                    stack.pop()
                else:
                    return False


        return len(stack)==0