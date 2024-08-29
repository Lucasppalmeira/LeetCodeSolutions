def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums2 = []
        cont = 0

        for i in range(len(nums)):
            if(nums[i] not in nums2):
                nums2.append(nums[i])
                cont += 1
                print(nums[i])
    
        for i in range(len(nums2)):
            nums[i] = nums2[i]
        
        return cont