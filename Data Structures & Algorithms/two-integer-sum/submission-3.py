class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        diff_list = [target-x for x in nums]

        for ind, difference in enumerate(diff_list):
            if difference in nums and ind != nums.index(difference):
                return sorted([ind, nums.index(difference)])

        return []