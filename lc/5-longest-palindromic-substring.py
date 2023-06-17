class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        if l == 1:
            return s

        # define dp[i][j] = True when the substring from i to j (both inclusive)
        # is a palindrome
        dp = [[False] * l for _ in range(l)]

        # single char is a palindrome
        for i in range(l):
            dp[i][i] = True

        res_ptr = 0
        res_len = 0

        for right in range(l):
            for left in range(right, -1, -1):
                # edge case: same character at same position
                if left == right:
                    if res_len < 1:
                        res_ptr = left
                        res_len = 1

                elif s[left] != s[right]:
                    continue
                # base case: when we find "xx"
                # we found a longer palindromic substring
                elif right - left == 1:
                    if res_len < 2:
                        res_ptr = left
                        res_len = 2
                    dp[left][right] = True

                # when we find "x___x" where "___" is a palindrome
                elif dp[left + 1][right - 1]:
                    # we found a longer palindromic substring
                    if (right - left + 1) > res_len:
                        res_ptr = left
                        res_len = right - left + 1
                    # memoize: remember that s[left:right+1] is a palindrome
                    dp[left][right] = True

        return s[res_ptr:res_ptr+res_len]

'''
edge cases:
"ac"
"aaaa"

consider:
    for right in range(l):
        for left in range(right, -1, -1):
        --> use this iteration method when building from bottom up (usually DP questions)
            --> this method ensures that at every index i, all the possible substrings up to this point has been covered / considered (and therefore updated into our memo table)
        --> because the second method below may miss some of the subproblems
            
            VS

    for left in range(l):
        for right in range(left, l):
        --> this method fails for the test case "aaaa" because when we consider left = 0 and right = 3, the subproblem "aa" where left = 1 and right = 2
            has not been considered up to this point (and so the memo table has not been updated for this subproblem)
'''