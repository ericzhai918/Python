import unittest


class Solution:
    def printClockwiseMatrix(self, matrix):
        if not matrix:
            return []

        m = len(matrix)
        n = len(matrix[0])
        answer = []
        # 统计数组中元素的个数
        number = 1
        i = j = 0

        # 定义四个边界
        upper_i = 0
        lower_i = m - 1
        left_j = 0
        right_j = n - 1

        # 定义两个指针，默认情况为指针向右
        right_pointer = 1
        down_pointer = 0

        while number <= m * n:
            answer.append(matrix[i][j])

            if right_pointer == 1:
                if j < right_j:
                    j = j + 1
                else:
                    right_pointer = 0
                    down_pointer = 1
                    upper_i = upper_i + 1
                    i = i + 1

            elif down_pointer == 1:
                if i < lower_i:
                    i = i + 1
                else:
                    down_pointer = 0
                    right_pointer = -1
                    right_j = right_j - 1
                    j = j - 1

            elif right_pointer == -1:
                if j > left_j:
                    j = j - 1
                else:
                    right_pointer = 0
                    down_pointer = -1
                    lower_i = lower_i - 1
                    i = i - 1

            elif down_pointer == -1:
                if i > upper_i:
                    i = i - 1
                else:
                    down_pointer = 0
                    right_pointer = 1
                    left_j = left_j + 1
                    j = j + 1
            number = number + 1

        return answer


class TestPrintClockwiseMatrix(unittest.TestCase):
    def test_null_matrix(self):
        s = Solution()
        matrix = []
        answer = []
        self.assertEqual(s.printClockwiseMatrix(matrix), answer)

    def test_2x2_matrix(self):
        s = Solution()
        matrix = [[1, 2], [ 3, 4]]
        answer = [1, 2, 4, 3]
        self.assertEqual(s.printClockwiseMatrix(matrix), answer)

    def test_2x3_matrix(self):
        s = Solution()
        matrix = [[1, 2, 3], [4, 5, 6]]
        answer = [1, 2, 3, 6, 5, 4]
        self.assertEqual(s.printClockwiseMatrix(matrix), answer)

    def test_4x4_matrix(self):
        s = Solution()
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        answer = [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
        self.assertEqual(s.printClockwiseMatrix(matrix), answer)


if __name__ == '__main__':
    unittest.main()
