class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        rows, cols = len(matrix), len(matrix[0])
        count = rows * cols
        left, right, top, bot = 0, cols - 1, 0, rows - 1
        output = []
        # invariant: left, right, top and bot are always valid indices
        while len(output) < count:
            # traverse one layer (i.e. the outermost layer)
            ptr = left
            while ptr <= right and len(output) < count:
                val = matrix[top][ptr]
                output.append(val)
                ptr += 1
            
            ptr = top + 1
            while ptr <= bot and len(output) < count:
                val = matrix[ptr][right]
                output.append(val)
                ptr += 1

            ptr = right - 1
            while ptr >= left and len(output) < count:
                val = matrix[bot][ptr]
                output.append(val)
                ptr -= 1
            
            ptr = bot - 1
            while ptr >= top + 1 and len(output) < count:
                val = matrix[ptr][left]
                output.append(val)
                ptr -= 1
            
            # remove the layer
            left += 1
            right -= 1
            top += 1
            bot -= 1
        return output