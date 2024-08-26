def twoSum(self, nums, target):
        index = []
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if(nums[i] + nums[j] == target and i != j):
                    index.append(i)
                    index.append(j)
                    return index