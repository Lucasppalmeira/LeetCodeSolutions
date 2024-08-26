def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        output = ""
        strs = sorted(strs)
        initial = strs[0]
        final = strs[-1]

        for i in range(min(len(initial), len(final))):
            if(initial[i] != final[i]):
                return output
            output += initial[i]
            
        return output