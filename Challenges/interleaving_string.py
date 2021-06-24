"""
The problem description is vague
Idea is: try all possible interleave versions and see if s3 is uberhaupt in that set

"""
from functools import lru_cache


class Solution:
    first_run = True
    
    @lru_cache()
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # early cutoff
        if self.first_run and (len(s1) + len(s2) != len(s3)):
            self.first_run = False
            return False

        # we ran out of characters withtout any issue, return True
        if not len(s1) and not len(s2) and not len(s3): return True

        # try one from s1 if s1 has char and it is a possible interleave
        if len(s1) and s1[0] == s3[0]:
            res = self.isInterleave(s1[1:], s2, s3[1:])
            if res: return True
        
        # try one from s2 if it is a possible interleave
        if len(s2) and s2[0] == s3[0]:
            res = self.isInterleave(s1, s2[1:], s3[1:])
            if res: return True
        
        return False


s1 = "test"
s2 = "testtest"
s3 = "tttttesttest"

s = Solution()
print(s.isInterleave(s1, s2, s3))