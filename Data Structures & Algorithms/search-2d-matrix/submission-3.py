class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        rowl, rowr = 0, m - 1

        while rowl <= rowr:
            mid = (rowl + rowr) // 2

            if matrix[mid][n - 1] < target:
                rowl = mid + 1
            elif matrix[mid][0] > target:
                rowr = mid - 1
            else:
                row = mid
                break
        else:
            return False

        l, r = 0, n - 1

        while l <= r:
            mid = (l + r) // 2

            if matrix[row][mid] < target:
                l = mid + 1
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                return True

        return False