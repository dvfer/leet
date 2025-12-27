import sys
import ast 
from utils.timeit import measure_time 

class Solution():
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
    @measure_time
    def twoSum(self):
        for (idx, x) in enumerate(self.nums):
            for (idy, y) in enumerate(self.nums):
                if idx == idy: continue
                if x + y == self.target: return [idx, idy]
    @measure_time
    def twoSums2(self):
        dic = {}
        for (idx, x) in enumerate(self.nums):
            difference = self.target - x
            if difference in dic:
                return [dic[difference], idx]
            dic[x] = idx

    def __str__(self):
        return f"solution 1: {self.twoSum()}\nsolution 2: {self.twoSums2()}"

if __name__ == "__main__":
    print(f"All arguments: {sys.argv}")

    if len(sys.argv) == 3:
        try:
            nums_input = ast.literal_eval(sys.argv[1])
            
            target_input = int(sys.argv[2])

            print(Solution(nums_input, target_input))
            
        except ValueError:
            print("Error: Target must be an integer.")
        except SyntaxError:
            print("Error: Nums must be a valid list format like '[1,2,3]'.")
    else:
        print("Bad arguments.")
        print("Usage example: python script.py '[2,7,11,15]' 9")
        print("Running default setting")
        nums = list(range(5000))
        target = 9990 # 4995 + 4995 is the last pair usually
        
        print(Solution(nums, target))