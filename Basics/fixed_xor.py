#str1 = 1c0111001f010100061a024b53535009181c
#str2 = 686974207468652062756c6c277320657965

str1 = raw_input("Enter first string: ")
str2 = raw_input("Enter Second string: ")

print "%x" %(int(str1,16) ^ int(str2,16))
