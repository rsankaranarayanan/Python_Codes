# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]
 

# Constraints:

# 1 <= n <= 8

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        S = []
        def backtrack( left = 0, right = 0):
            if left == right == n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(left+1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(left, right+1)
                S.pop()
        backtrack()
        return ans
        
