def isPalindrome(str):
    strLen = len(str)
    i = 0 
    j = strLen-1
    while i<j:
        if str[i] != str[j]:
            return False
        i+=1
        j-=1
    return True

str = "malayalam"
if isPalindrome(str):
    print('palindrome!')
else:
    print("nope")