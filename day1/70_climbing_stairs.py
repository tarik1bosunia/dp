# ============ Recursion ==================
# class Solution:
#     def climbStairs(self, n: int) -> int:
        
#         if n <= 1:
#             return 1
        
#         return self.climbStairs(n - 1) + self.climbStairs(n - 2)
    


# sol = Solution()
# n = 2
# print(sol.climbStairs(n))


# ============ Memoization ==================
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         dp = [-1] * (n + 1)
        
#         return self.helper(n, dp)
    
#     def helper(self, n, dp):
#         if n <= 1:
#             return 1
        
#         if dp[n] != -1:
#             return dp[n]
        
#         dp[n] = self.helper(n - 1, dp) + self.helper(n - 2, dp)
#         return dp[n]


# sol = Solution()
# n = 2
# print(sol.climbStairs(n))





# ============ Tabulation ==================
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         dp = [-1] * (n + 1)
        
#         return self.helper(n, dp)
    
#     def helper(self, n, dp):
#         dp[0] = 1
#         dp[1] = 1
        
#         for i in range(2, n + 1):
#             dp[i] = dp[i - 1] + dp[i - 2]
            
#         return dp[n]


# sol = Solution()
# n = 2
# print(sol.climbStairs(n))




# ============ Tabulation ==================
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1] * 2
        
        for i in range(2, n + 1):
            dp[1], dp[0] = dp[1] + dp[0], dp[1]
            
        return dp[1]

sol = Solution()
n = 2
print(sol.climbStairs(n))
        