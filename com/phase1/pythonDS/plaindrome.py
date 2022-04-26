def plaindrome(s):
    return s == s[::-1]
if __name__ == '__main__':
 s = 'Tamil' # Tamil malayalam
 ans = plaindrome(s)
 print(ans)

 # s='Tamil'
 # ans = plaindrome(s1)
 # print(ans)

 if (ans ):
     print(s , " Is plaindrome")
 else:
     print(ans)
     print(s, " Is not plaindrome")