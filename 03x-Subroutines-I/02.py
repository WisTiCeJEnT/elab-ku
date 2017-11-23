init = int(input("Enter initial amount in Baht: "))
inter = int(input("Enter interest rate in percent: "))
print(f"Total amount after 1 year is {init*(100+inter)/100:.2f} Baht.")
print(f"Total amount after 5 years is {init*((100+inter)/100)**5:.2f} Baht.")
print(f"Total amount after 10 years is {init*((100+inter)/100)**10:.2f} Baht.")
print(f"Total amount after 20 years is {init*((100+inter)/100)**20:.2f} Baht.")

