from typing import List, Tuple, Set

class Solution:
    # backtracking approach
    def dfs(self, board: List[List[str]], src: Tuple[int, int], word: str, visited: Set[Tuple[int, int]]) -> bool:
        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]        
        rows = len(board)
        cols = len(board[0])

        if not word:
            return True

        for dir in dirs:
            next_r = src[0] + dir[0]
            next_c = src[1] + dir[1]
            if next_r < 0 or next_r >= rows or next_c < 0 or next_c >= cols:
                continue
            
            next_pos = (next_r, next_c)
            if next_pos in visited:
                continue

            next_char = board[next_r][next_c]
            if next_char == word[0]:
                # make a decision to use next_pos
                visited.add(next_pos)
                isFound = self.dfs(board, next_pos, word[1:], visited)
                # if decision is correct, we use next_pos
                if isFound:
                    return True
                # if decision is wrong, do not use next_pos and remember to backtrack!
                visited.remove(next_pos)
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        positions = {}

        for i in range(rows):
            for j in range(cols):
                c = board[i][j]
                if c in positions:
                    positions[c].append((i, j))
                else:
                    positions[c] = [(i, j)]
        
        # edge case check
        if word[0] in positions:
            word_positions = positions[word[0]]
        else:
            return False

        for word_pos in word_positions:
            isFound = self.dfs(board, word_pos, word[1:], set([word_pos]))
            if isFound:
                return True
        return False
  