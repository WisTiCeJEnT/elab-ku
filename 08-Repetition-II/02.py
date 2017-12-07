inp = -1
n = 1
p = 0
while inp != 0:
    if inp<0:
        n += inp
    else:
        p += inp
    inp = float(input("Enter a number (or zero to exit): "))
print(f"The sum of all positive numbers is {p:.2f}")
print(f"The sum of all negative numbers is {n:.2f}")
