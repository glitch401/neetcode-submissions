class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        # 1. Pre-allocate prefix grid
        self.p = [[0] * (n + 1) for _ in range(m + 1)]

        # Local alias speeds up variable lookup in Python loops
        p = self.p

        for r in range(m):
            row_sum = 0
            row = matrix[r]
            p_prev = p[r]
            p_curr = p[r + 1]

            for c in range(n):
                # Accumulate row value on the fly
                row_sum += row[c]
                # Pref[r+1][c+1] = Pref[r][c+1] + running_row_sum
                p_curr[c + 1] = p_prev[c + 1] + row_sum

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        p = self.p
        return p[r2 + 1][c2 + 1] - p[r1][c2 + 1] - p[r2 + 1][c1] + p[r1][c1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)