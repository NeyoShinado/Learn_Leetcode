# Version0
# 按对角线筛选子方阵，方阵中查询函数不对
# Not Pass
'''
class Solution:
    def searchMatrix(self, matrix, target):
        # init
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        rbias = 0
        cbias = 0
        res = False

        if matrix[m-1][n-1] < target or matrix[0][0] > target:
            return False

        while not res and (rbias<=m-1 or cbias<=n-1):
            # min width height cmp
            l = min(m-rbias, n-cbias)

            # search sub-square
            res = searchSquare(l, rbias, cbias, matrix, target)
            if res == -1:
                return False

            # rb,cb update
            if m - rbias > n-cbias:
                rbias += l
            elif n-cbias > m-rbias:
                cbias += l
            else:
                rbias += l
                cbias += l
        
        return res

def searchSquare(l, rbias, cbias, matrix, target) -> bool:
    # l: length of square
    # rbias, cbias: start index of sub-square
    # diag search
    # output: bool type mean target in/not in subsquare
    #         -1 mean target not in matrix
    if matrix[rbias][cbias] > target or matrix[rbias+l-1][cbias+l-1] < target:
        return False
    x = rbias
    y = cbias
    while x <= rbias+l-1:
        if matrix[x][y] == target:
            return True
        elif matrix[x][y] < target:
            x += 1
            y += 1
            continue
        else:
            break
    # locate check
    if x <= rbias+l-1:
        for col in range(cbias, y+1):
            if matrix[x][col] == target:
                return True
        for row in range(rbias, x+1):
            if matrix[row][y] == target:
                return True
    else:
        return False
    return -1
'''


# Version1
# 二分搜索
'''
class Solution:
    def binary_search(self, matrix, target, start, vertical):
        lo = start
        hi = len(matrix[0])-1 if vertical else len(matrix)-1

        while hi >= lo:
            mid = (lo + hi) // 2
            if vertical: # searching a col
                if matrix[start][mid] < target:
                    lo = mid + 1
                elif matrix[start][mid] > target:
                    hi = mid - 1
                else:
                    return True
            else: # searching a row
                if matrix[mid][start] < target:
                    lo = mid + 1
                elif matrix[mid][start] > target:
                    hi = mid - 1
                else:
                    return True

            return False

    def searchMatrix(self, matrix, target):
        if not matrix:
            return False

        for i in range(min(len(matrix), len(matrix[0]))):
            vertical_found = self.binary_search(matrix, target, i, True)
            horizontal_found = self.binary_search(matrix, target, i, False)
            if vertical_found or horizontal_found:
                return True

        return False
'''


# Version3
# 排除法
# TC: O(M+N), SC: O(1)
class Solution:
    def searchMatrix(self, matrix, target):
        if len(matrix)==0 or len(matrix[0])==0:
            return False

        H = len(matrix)
        W = len(matrix[0])

        r = H - 1
        c = 0

        while c < W and r >= 0:
            if matrix[r][c] > target:
                r -= 1
            elif matrix[r][c] < target:
                c += 1
            else:
                return True

        return False