s = int(input("Enter block size: "))
print((input("Character to use: ")*s+'\n')*s,end='')
"""
#========== Just for fun ===============
s = int(input("Enter block size: "))
c = input("Character to use: ")
c = c*s + '\n'
c = c*s
print(c,end='')
"""
