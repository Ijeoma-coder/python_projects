record = [1,2,3,4]

for i in range(4) :
    record[i-1]=int(input("What's your score "))

sum=(record[1-1]+ record[1] + record[2] + record[3])

print(sum)

n= len(record)

yes=True
no= False

avg=bool(input("Do you want your average score? "))

if avg== True : 
    print(sum // n)
    if avg < 65 : print("You got work to do? ")

else : print(sum)
