str1 =  ' hello, world! '
print ( ' The length of the string is: ' , len (str1))
print ( ' word initials: ' , str1.title())
print ( ' string is capitalized: ' , str1.upper())
# str1 = str1.upper()
print ( ' string is not uppercase: ' , str1.isupper())
print ( ' Does the string start with hell : ' , str1.startswith( ' hello ' ))
print ( ' string is not ending with hell : ' , str1.endswith( ' hello ' ))
print ( ' string is not beginning with an exclamation point: ' , str1.startswith( ' ! ' ))
print ( ' string is not an exclamation point end: ' , str1.endswith( ' ! ' ))
str2 =  ' - \ u9a86 \ u660a '
str3 = str1.title() +  '  '  + str2.lower()
print (str3)