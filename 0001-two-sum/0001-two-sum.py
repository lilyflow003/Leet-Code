class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # outer loop go through each element
        for i in range(len(nums)):

            # inner loop go through next to elements
            for j in range(i+1, len(nums)):

                # check if two elements sum up of target 
                if nums[i] + nums[j] == target:
                 
                #  return the indices of elements 
                 return [i,j]
                
                # return empty list if two elements are not sum of target 
        return []