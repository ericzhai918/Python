import unittest

class Solution:
    def jumpFloor(self,num):
        a = 1
        b = 1
        for i in range(num):
            a,b = b, a+b
        return a

    def jumpFloorII(self,num):
        return pow(2,num-1)


class TestJumpSteps(unittest.TestCase):

    def test_1_step(self):
        solu = Solution()
        step = solu.jumpFloor(1)
        self.assertEqual(step,1)

    def test_2_step(self):
        solu = Solution()
        step = solu.jumpFloor(2)
        self.assertEqual(step,2)

    def test_3_step(self):
        solu = Solution()
        step = solu.jumpFloor(3)
        self.assertEqual(step,3)

    def test_4_step(self):
        solu = Solution()
        step = solu.jumpFloor(4)
        self.assertEqual(step, 5)

    def test_5_step(self):
        solu = Solution()
        step = solu.jumpFloor(5)
        self.assertEqual(step,8)

class TestJumpStepsII(unittest.TestCase):

    def test_1_step(self):
        solu = Solution()
        step = solu.jumpFloorII(1)
        self.assertEqual(step, 1)

    def test_2_step(self):
        solu = Solution()
        step = solu.jumpFloorII(2)
        self.assertEqual(step, 2)

    def test_3_step(self):
        solu = Solution()
        step = solu.jumpFloorII(3)
        self.assertEqual(step, 4)

    def test_4_step(self):
        solu = Solution()
        step = solu.jumpFloorII(4)
        self.assertEqual(step, 8)

    def test_5_step(self):
        solu = Solution()
        step = solu.jumpFloorII(5)
        self.assertEqual(step, 16)

if __name__ == '__main__':
    unittest.main()