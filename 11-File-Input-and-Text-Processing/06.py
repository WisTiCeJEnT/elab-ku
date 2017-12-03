text = open(input("Enter age file: ")).read().splitlines()
lis = [pair.split(',') for pair in text if pair != '']
maxx = max([age[1] for age in lis])
print(f"Oldest person(s) with the age of {maxx}:")
for pair in lis:
    if pair[1] == maxx:
        print("-",pair[0])
