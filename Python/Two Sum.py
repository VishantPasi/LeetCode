class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0,len(nums)-1):
            for j in range(1,len(nums)):
                if (nums[i] + nums[j]) == target:
                    print("true")
                    
                    print(i,j)
                    return True
                else:
                    
                    print("False")
                    print(i,j)
                    return False
                    
c = Solution()
c.twoSum([2,7,11,15],18)