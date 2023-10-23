from collections import deque
class Solution:
    def reverse(self, x: int) -> int:
        s=deque()
        dup=0
        out=""
        res=0
        if x>0:
            dup=x
        if x<0:
            dup=-1*x
        for i in str(dup):
            s.append(int(i))
        while(s):
            out+=str(s.pop())
        if x<0:
            res=-1*int(out)
        if x>0:
            res=int(out)
        if res >=-1*pow(2,31) and res<=pow(2,31)-1:
            return res
        else:
            return 0

