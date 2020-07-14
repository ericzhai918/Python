import unittest


class Solution:
    def searchMatrix(self, array, target):
        if not array or target is None:
            return False
        rows, cols = len(array), len(array[0])
        i, j = 0, cols - 1
        while i < rows and j >= 0:
            if array[i][j] == target:
                return True
            elif array[i][j] < target:
                i = i + 1
            else:
                j = j - 1
        return False


class TestSearchMatrix(unittest.TestCase):
    def test_increment_with_rows(self):
        s = Solution()
        array = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
        target = 7
        flag = s.searchMatrix(array, target)
        self.assertTrue(flag)

    def test_increment_with_every_rows(self):
        s = Solution()
        array = [[1, 3, 5, 7], [10, 11, 16, 20], [21, 23, 29, 33]]
        target = 11
        flag = s.searchMatrix(array, target)
        self.assertTrue(flag)


if __name__ == '__main__':
    unittest.main()
