import unittest
from typing import List

'''
Approach:

- define dp[i] as True when a word in wordDict ends exactly at index i,
  and that there is another word that ends before this word
  - base case: when this is the first word segment in string s
- at every index i, look through all possible words that end exactly at i

'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        l = len(s)
        dp = [False] * l
        for i in range(l):
            for j in range(i, -1, -1):
                word = s[j:i+1]
                if word in words:
                    if j == 0:
                        dp[i] = True
                    elif dp[j-1]:
                        dp[i] = True
        return dp[l-1]

class UnitTests(unittest.TestCase):

    def test_public_1(self):
        self.assertEqual(Solution().wordBreak("leetcode", ["leet","code"]), True)

    def test_public_2(self):
        self.assertEqual(Solution().wordBreak("applepenapple", ["apple","pen"]), True)

    def test_public_3(self):
        self.assertEqual(Solution().wordBreak("catsandog", ["cats","dog","sand","and","cat"]), False)

if __name__ == '__main__':
    unittest.main()
