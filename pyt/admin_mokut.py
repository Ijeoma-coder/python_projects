#programme to take stock of the acailable ice cream and corresponding temp
#average temp is -17.5875


print("Welcome to Mokut's Ice cream",  "Fill in the info, Boss")


stock = []

for i in range(5):
    flavor = input("Available flavor: ")
    temp = float(input("What's the temperature? "))
    
    stock.append({"flavor": flavor, "temperature": temp})

for i in range(5):
    cream = stock[i]["flavor"]
    temp = stock[i]["temperature"]
    
    print(f"Checking {cream}...")
    
    if temp > -17.5875:
        print("Not Cool Enough!")
    elif temp <= -17.5875:
        print("Ready for Serve!")

print (stock)

        

