lis = []
inp = input("Enter student score (or ENTER to finish): ")
while inp != '':
    lis.append(int(inp))
    inp = input("Enter student score (or ENTER to finish): ")
for i in range(len(lis)):
    print(f"Student #{i+1} score: {lis[i]}")
print("Average score is {:.2f}".format(sum(lis)/len(lis)))
print("Minimum score is",min(lis))
print("Maximum score is",max(lis))
