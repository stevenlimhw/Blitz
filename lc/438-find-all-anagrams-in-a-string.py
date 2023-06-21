from typing import List


class Solution:
    # non-constant sliding window approach
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []

        map = {}
        for i in range(len(p)):
            c = p[i]
            if c in map:
                map[c] += 1
            else:
                map[c] = 1
        
        l = 0
        r = 0
        letters = {}

        # invariant: letters contain those within l and r (both inclusive)
        while r < len(s):
            c = s[r]
            if c not in map:
                r += 1
                l = r
                letters = {}
                continue

            if c in letters:
                c_count = letters[c]
                if c_count + 1 > map[c]:
                    # find the earliest c and remove it
                    while s[l] != c:
                        if letters[s[l]] == 1:
                            letters.pop(s[l])
                        else:
                            letters[s[l]] -= 1
                        l += 1
                    # guarantee: s[ref] = c
                    l += 1
                else:
                    letters[c] += 1
            # if c not in letters
            else:
                letters[c] = 1
            
            if r - l + 1 == len(p):
                res.append(l)
            
            r += 1
        return res
            

