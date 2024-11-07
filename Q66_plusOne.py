def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    
    return plusOneAux(digits, len(digits) -1)

def plusOneAux(digits, rightIndex):
    if(digits[rightIndex] < 9): 
        digits[rightIndex] = digits[rightIndex] + 1
        return digits
    else:
        digits[rightIndex] = 0
        if(rightIndex == 0):
            digits.insert(0,1)
        else:
            rightIndex -= 1
            plusOneAux(digits, rightIndex) 
    return digits

digits = [1, 9, 9, 9]
print(digits)
print(plusOne(digits))