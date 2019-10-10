a=input("Enter an alphabet ")
b=ord(a)
if b>=65 and b<=97:
    if a=='a' or a=='e'or a=='i'or a=='o'or a=='u':
        print('the alphabet is an vowel and is a small letter')
    else:
        print('yhe letter is an constanant and a small letter')


else:
    if a=='A' or a=='E'or a=='I'or a=='O'or a=='U':
        print('the alphabet is an vowel and is a capital letter')
    else:
        print('yhe letter is an constanant and a capital letter')
