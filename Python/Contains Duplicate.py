class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        myset = set(nums)

        if len(nums) != len(myset):
            print("true")
            return True
            
        else:
            print("false")
            return False
c = Solution()
c.containsDuplicate([1,2,3,4,1])