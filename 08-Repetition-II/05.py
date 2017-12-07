h = int(input("Enter the depth of the well: "))
u = int(input("Enter the height the frog can jump: "))
d = int(input("Enter the height the frog slips down: "))
if u-d>0 or u>=h:
    count = 1
    while h>u:
        h -= u
        print(f"On day {count} the frog leaps to the depth of {h} meters.")
        h += d
        print(f"At night he slips down to the depth of {h} meters.")
        count += 1
    print(f"The frog can escape the well on day {count}.")
else:
    print("The frog will never escape from the well.")
