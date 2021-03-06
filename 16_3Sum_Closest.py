"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return target
        nums = sorted(nums)
        res = nums[0] + nums[1] + nums[-1]
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if abs(sum - target) < abs(res - target):
                    res = sum
                if sum < target:
                    l += 1
                else:
                    r -= 1
        return res

if __name__ == '__main__':
    l = [0, 0, 0]
    t = 1
    print(Solution().threeSumClosest(l, t))
