class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(word, index, visited, board, row, col):
            visited.add((row, col))
            if index == len(word) - 1 and board[row][col] == word[index]:
                return True
            elif board[row][col] != word[index]:
                visited.remove((row, col))
                return False
            else:
                r, c = len(board), len(board[0])
                if r == 1 and c == 1:
                    return index == len(word) - 1
                if row != 0 and (row - 1, col) not in visited and dfs(word, index + 1, visited, board, row - 1, col):
                    return True
                if row != r - 1 and (row + 1, col) not in visited and dfs(word, index + 1, visited, board, row + 1, col):
                    return True
                if col != 0 and (row, col - 1) not in visited and dfs(word, index + 1, visited, board, row, col - 1):
                    return True
                if col != c - 1 and (row, col + 1) not in visited and dfs(word, index + 1, visited, board, row, col + 1):
                    return True
                visited.remove((row, col))
                return False
        r, c = len(board), len(board[0])
        for i in range(r):
            for j in range(c):
                if dfs(word, 0, set(), board, i, j):
                    return True
        return False
