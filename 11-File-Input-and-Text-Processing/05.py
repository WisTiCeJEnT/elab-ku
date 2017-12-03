dic = { "A":4.0,
        "B":3.0,
        "C":2.0,
        "D":1.0,
        "F":0.0,
        "B+":3.5,
        "C+":2.5,
        "D+":1.5,
        }
text = open(input("Enter grade file: ")).read().splitlines()
lis = [s.split(',') for s in text if s != '']
credit = 0
point = 0
for i in range(len(lis)):
    print(f"subject: {lis[i][0]} credits: {lis[i][1]} grade: {lis[i][2]:2} point: {dic[lis[i][2]]}")
    credit += int(lis[i][1])
    point += int(lis[i][1])*dic[lis[i][2]]
print("Total credits =",credit)
print("GPA = {:.2f}".format((point/credit)))
