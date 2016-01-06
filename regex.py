import re
input1 = input ("Enter the string:")
'''string="Hello ABCD, here is my mail id example@me.com "'''
res = re.search("([^@|\s]+@[^@]+\.[^@|\s]+)",input1,re.I)
print (res.group(1))
