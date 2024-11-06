def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    word = s.split()
    cont = 0

    for i in word[len(word) -1]:
        cont += 1
            
    return cont


print(lengthOfLastWord("Hello World"))