lis = []
while True:
    inp = input("Enter a number (just [Enter] to quit): ")
    if inp == "":
        break
    lis.append(float(inp))
if lis:
    print(f"The maximum is {max(lis):.2f}")
    print(f"The minimum is {min(lis):.2f}")
    print(f"The average is {sum(lis)/len(lis):.2f}")
else:
    print("Nothing to do.")
