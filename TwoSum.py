from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            hashmap ={}
            for i in range(len(nums)):
                complement = target - nums[i]
                if complement in hashmap:
                    return [i,hashmap[complement]]
                hashmap[nums[i]] = i

# test case 1
solution = Solution()
nums1 = [2, 7, 11, 15]
target1 = 9
print(solution.twoSum(nums1, target1)) 