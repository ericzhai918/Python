#方法1：
def searchMatrix(self, matrix, target):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == target:
                return True
    return False

#方法2
    def searchMatrix(self, matrix, target):
        if not matrix or target is None:
            return False
        rows = len(matrix)
        cols = len(matrix[0])
        low = 0
        high = rows * cols - 1

        while (low <= high):
            mid = (low + high) / 2
            num = matrix[mid / cols][mid % cols]
            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1

        return False

#方法3
    def searchMatrix(self, matrix, target):
        if not matrix or target is None:
            return False
        rows, cols = len(matrix), len(matrix[0])
        i, j = 0, cols - 1
        while i < rows and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i = i + 1
            else:
                j = j - 1

        return False