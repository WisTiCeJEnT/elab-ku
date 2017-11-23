init = int(input("Enter initial amount in Baht: "))
inter = int(input("Enter interest rate in percent: "))
showlis = [1,5,10,20]
for i in range(1,21):
    init *= (100+inter)/100
    if i in showlis:
        print("Total amount after {} year is {:.2f} Baht.".format(i,init))

