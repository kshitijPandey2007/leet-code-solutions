class Solution:
    def twoSum(self, nums, target):
        num_map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_map:
                return [num_map[complement], i]
            num_map[nums[i]] = i
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    sol = Solution()
    result = sol.twoSum(nums, target)
    print("Indices of the two numbers:", result)
