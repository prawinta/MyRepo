
def IsPalindrome(inpstr):     
    count = len(inpstr)     
    palindrome = True   
    i = 0   
    while(i < (count/2+1)):         
        if(inpstr[i] != inpstr[count- i- 1]):             
            palindrome = False           
            break       
        i = i + 1   
    return palindrome

my_str = input ("Enter a string:")
print IsPalindrome(my_str)
