text = open(input("Enter score file: ")).read().splitlines()
lis = [int(s) for s in text if s != '']
for i in range(len(lis)):
    print(f"Student #{i+1} score: {lis[i]}")
print("Average score is {:.2f}".format(sum(lis)/len(lis)))
print("Minimum score is",min(lis))
print("Maximum score is",max(lis))
