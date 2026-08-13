class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        cols = len(matrix[0])
        # Base row of zeros for 1-based padding
        self.pref = [[0] * (cols + 1)]
        
        for row in matrix:
            # 1. Compute 1D row prefix sum using C-level accumulate
            acc_row = [0] + list(accumulate(row))
            # 2. Vector-add with the previous row
            prev_row = self.pref[-1]
            self.pref.append([a + b for a, b in zip(acc_row, prev_row)])

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        p = self.pref
        return p[r2 + 1][c2 + 1] - p[r1][c2 + 1] - p[r2 + 1][c1] + p[r1][c1]
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)