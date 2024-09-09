def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """

    cont = 0
    i = 0
    firstOccur = -1

    if len(needle) > len(haystack):
        return -1
    
    while i < len(haystack) and cont < len(needle):
        if(i + len(needle)) > len(haystack) and cont == 0:
            return -1
        
        if haystack[i] == needle[cont] and cont == 0:
           firstOccur = i
           cont += 1

        elif haystack[i] == needle[cont]:
            cont += 1
            
        else:
            i = i - cont
            cont = 0
            firstOccur = -1

        i += 1
        

    return firstOccur

print(strStr("Mississippi", "issipi"))