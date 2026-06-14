class Solution:
    def dailyTemperatures(self,temperatures):
        n=len(temperatures)
        res=[0]
        stack=[(temperatures[-1],n-1)]
        for i in range(n-2,-1,-1):
            t=temperatures[i]
            index=i
            while stack and stack[-1][0]<=t:
                stack.pop()
            res.append(stack[-1][1]-index if stack else 0)
            stack.append((t,index))
        return list(reversed(res))