def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        romanNumerals = []

        for i in s:
            romanNumerals.append(i)
        
        for i in range(len(romanNumerals)):
            if(i < len(romanNumerals) -1 and romanNumerals[i] == "I" and romanNumerals[i+1] in "VX"):
                sum -= 1
            elif(i < len(romanNumerals) -1 and romanNumerals[i] == "X" and romanNumerals[i+1] in "LC"):
                sum -= 10
            elif(i < len(romanNumerals) -1 and romanNumerals[i] == "C" and romanNumerals[i+1] in "DM"):
                sum -= 100
            else:
                if(romanNumerals[i] == "I"):
                    sum += 1
                if(romanNumerals[i] == "V"):
                    sum += 5
                if(romanNumerals[i] == "X"):
                    sum += 10
                if(romanNumerals[i] == "L"):
                    sum += 50
                if(romanNumerals[i] == "C"):
                    sum += 100
                if(romanNumerals[i] == "D"):
                    sum += 500
                if(romanNumerals[i] == "M"):
                    sum += 1000
        return sum

print(romanToInt("XI"))