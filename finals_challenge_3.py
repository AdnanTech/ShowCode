from solution import Solution
import unittest

class Solution:

    def kill_switch(self, input):
        # sort array into 2 groups where each group is equal
        
        arr_length = len(input)
        
        # workout sum of all numbers in array
        sum = 0
        for i in input:
            sum += i
        
        # check if all numbers add to an odd number
        if (sum % 2 == 0):
            return True        
        
        if (sum % 2 != 0):
            return False
            
        
        return subset_checking(input, arr_length, sum // 2)
        
    def subset_checking(input, arr_length, sum):
        # Base Cases
        if sum == 0:
            return True
        if n == 0 and sum != 0:
            return False
 
        # recursive method
        # if last element is > sum, ignore
        if input[arr_length - 1] > sum:
            return subset_checking(input, arr_length, sum)
            
        return subset_checking(input, arr_length - 1, sum) or subset_checking(input, arr_length - 1, sum - input[arr_length - 1])
        
        
class SolutionTests(unittest.TestCase):

    
    def test1(self):
        solution = Solution()
        self.assertEqual(solution.kill_switch([ 1, 3, 3, 4, 5 ]), True)

    def test2(self):
        solution = Solution()
        self.assertEqual(solution.kill_switch([ 2, 4, 5, 6 ]), False)

if __name__ == '__main__':
    unittest.main()