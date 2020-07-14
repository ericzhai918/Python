import unittest

class Solution:
    def findMoreThanHalfNumIn2d(self, numbers):
        if numbers == []:
            return 0
        val, cnt = None, 0
        for num in numbers:
            if cnt == 0:
                val, cnt = num, 1
            else:
                if val == num:
                    cnt += 1
                else:
                    cnt -= 1
        return val if numbers.count(val) * 2 > len(numbers) else 0

class TestFindMoreThanHalfNumIn2d(unittest.TestCase):
    def test_null_array(self):
        s = Solution()
        numbers = []
        value = s.findMoreThanHalfNumIn2d(numbers)
        self.assertEqual(value, 0)

    def test_just_1_num(self):
        s = Solution()
        numbers = [3]
        value = s.findMoreThanHalfNumIn2d(numbers)
        self.assertEqual(value, 3)

    def test_all_same_num(self):
        s = Solution()
        numbers = [1,1,1,1,1]
        value = s.findMoreThanHalfNumIn2d(numbers)
        self.assertEqual(value,1)

    def test_no_same_num(self):
        s = Solution()
        numbers = [1,2,3,4,5]
        value = s.findMoreThanHalfNumIn2d(numbers)
        self.assertEqual(value,0)

    def test_some_same_num(self):
        s = Solution()
        numbers = [1,2,3,2,2,2,5,4,2]
        value = s.findMoreThanHalfNumIn2d(numbers)
        self.assertEqual(value, 2)

if __name__ == '__main__':
    unittest.main()