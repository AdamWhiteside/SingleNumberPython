class Solution(object):
    def singleNumber(self, nums):
        dictionary = {}
        for i in range(len(nums)):
            if nums[i] not in dictionary.keys():
                dictionary[nums[i]] = nums[i]
            else:
                del dictionary[nums[i]]
        return dictionary.values()[0]