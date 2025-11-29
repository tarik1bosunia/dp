
# ============= Recursion =============
# def fibonacci(n):
#     """Return the nth Fibonacci number."""
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1

#     return fibonacci(n - 1) + fibonacci(n - 2)


# n = 3
# print(fibonacci(n))



# ============= Memoization =============
# def fibonacci(n, dp):
#     """Return the nth Fibonacci number."""
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
    
#     if dp[n] != -1:
#         return dp[n]

#     dp[n] = fibonacci(n - 1, dp) + fibonacci(n - 2, dp)
#     return dp[n]


# n = 3
# print(fibonacci(n, [-1] * (n + 1)))


# ============= Tabulation =============

# def fibonacci(n, dp):
#     """Return the nth Fibonacci number."""
#     dp[0] = 0
#     dp[1] = 1
    
#     for i in range(2, n+1):
#         dp[i] = dp[i - 1] + dp[i - 2]
        
#     return dp[n]

# n = 4
# print(fibonacci(n, [-1] * (n + 1)))


# ============= Space Optimization =============

def fibonacci(n, dp):
    """Return the nth Fibonacci number."""
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, n+1):
        dp[0], dp[1] = dp[1], dp[0] + dp[1] 
        
    return dp[1]

n = 4
print(fibonacci(n, [-1] * (2)))