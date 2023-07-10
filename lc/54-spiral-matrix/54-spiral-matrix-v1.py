from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = set()

        res = []
        ptr_r = 0
        ptr_c = 0

        min_r = 0
        min_c = 0
        max_r = len(matrix) - 1
        max_c = len(matrix[0]) - 1

        if max_r == 0 and max_c == 0:
            res.append(matrix[0][0])
            return res

        dir = "right"

        bound_r = max_r
        bound_c = max_c

        isFirst_r = True
        isFirst_c = True

        while True:
            # stop when we go out of bound
            if ptr_r > max_r or ptr_r < 0 or ptr_c > max_c or ptr_c < 0:
                break

            # stop when we reach last element
            if ((ptr_r, ptr_c) in visited):
                print("HERE")
                break

            # at vertices
            if (dir == "right" or dir == "left") and ptr_c == bound_c:
                # change direction
                if dir == "right":
                    dir = "down"
                    if isFirst_r:
                        bound_r = max_r
                        isFirst_r = False
                    else:
                        bound_r = max_r - 1
                        max_r -= 1
                elif dir == "left":
                    dir = "up"
                    bound_r = min_r + 1
                    min_r += 1
            elif (dir == "down" or "up") and ptr_r == bound_r:
                if dir == "down":
                    dir = "left"
                    if isFirst_c:
                        bound_c = min_c
                        isFirst_c = False
                    else:
                        bound_c = min_c + 1
                        min_c += 1
                elif dir == "up":
                    # now we go right
                    dir = "right"
                    bound_c = max_c - 1
                    max_c -= 1

            cur = matrix[ptr_r][ptr_c]
            res.append(cur)
            visited.add((ptr_r, ptr_c))
            print(visited)
            print(dir)
            if dir == "right":
                ptr_c += 1
            elif dir == "down":
                ptr_r += 1
            elif dir == "left":
                ptr_c -= 1
            elif dir == "up":
                ptr_r -= 1
        return res
