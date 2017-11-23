from math import ceil
minute = int(input("Enter parking time in minutes: "))
print(f"Parking fee is {ceil(minute/60)*25} baht.")
