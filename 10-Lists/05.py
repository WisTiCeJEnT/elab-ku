lis = []
inp = input("Enter student score (or ENTER to finish): ")
while inp != '':
    lis.append(int(inp))
    inp = input("Enter student score (or ENTER to finish): ")
lis.sort(reverse=True)
for i in range(len(lis)):
    print(f"Rank #{i+1}: {lis[i]}")
