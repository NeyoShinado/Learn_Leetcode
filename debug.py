# Version0
class Solution:
    def searchMatrix(self, matrix, target):
        # init
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        rbias = 0
        cbias = 0
        res = False

        if matrix[m - 1][n - 1] < target or matrix[0][0] > target:
            return False

        while not res and (rbias <= m - 1 or cbias <= n - 1):
            # min width height cmp
            l = min(m - rbias, n - cbias)

            # search sub-square
            res = searchSquare(l, rbias, cbias, matrix, target)
            if res == -1:
                return False

            # rb,cb update
            if m - rbias > n - cbias:
                rbias += l
            elif n - cbias > m - rbias:
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
    if matrix[rbias][cbias] > target or matrix[rbias + l - 1][cbias + l - 1] < target:
        return False
    x = rbias
    y = cbias
    while x <= rbias + l - 1:
        if matrix[x][y] == target:
            return True
        elif matrix[x][y] < target:
            x += 1
            y += 1
            continue
        else:
            break
    # locate check
    if x <= rbias + l - 1:
        for col in range(cbias, y + 1):
            if matrix[x][col] == target:
                return True
        for row in range(rbias, x + 1):
            if matrix[row][y] == target:
                return True
    else:
        return False
    return -1


# Version1
# 二分搜索


if __name__ == "__main__":
    #matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
    target = 15
    t = Solution()
    res = t.searchMatrix(matrix, target)

