class Solution:
    def dailyTemperatures(self,temperatures):
        n=len(temperatures)
        res=[0]* n
        stack=[]
        for i,t in enumerate(temperatures):
            if not stack or t<=temperatures[stack[-1]]:
                stack.append(i)
            while stack and temperatures[stack[-1]]<t:
                index=stack.pop()
                res[index]=i-index
            stack.append(i)
        return res