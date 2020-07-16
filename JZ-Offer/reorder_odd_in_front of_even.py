import unittest


class Solution:
    def reorderArray(self, array):
        size = len(array)
        left = 0
        right = size - 1
        while left < size:
            if array[right] % 2 == 1:
                temp = array[right]
                for i in range(right - 1, -1, -1):
                    array[i + 1] = array[i]
                array[0] = temp
            else:
                right = right - 1
            left = left + 1
        return array


class TestReorderArray(unittest.TestCase):
    def test_ascending_array(self):
        array = [1, 2, 3, 4, 5, 6]
        s = Solution()
        self.assertEqual(s.reorderArray([1, 2, 3, 4, 5, 6]), [1, 3, 5, 2, 4, 6])

    def test_descending_array(self):
        array = [1, 2, 3, 4, 5, 6]
        s = Solution()
        self.assertEqual(s.reorderArray([6, 5, 4, 3, 2, 1]), [5, 3, 1, 6, 4, 2])

    def test_disorder_array(self):
        array = [1, 2, 3, 4, 5, 6]
        s = Solution()
        self.assertEqual(s.reorderArray([6, 1, 4, 5, 2, 3]), [1, 5, 3, 6, 4, 2])


if __name__ == '__main__':
    unittest.main()
