# Define the available flavors and their temperatures
stock = [
    {"flavor": "Vanilla", "temperature": -18},
    {"flavor": "Chocolate", "temperature": -19},
    {"flavor": "Strawberry", "temperature": -20},
    {"flavor": "Mint", "temperature": -17},
    {"flavor": "Cookie Dough", "temperature": -21}
]

# Check each flavor
for i in range(5):
    cream = stock[i]["flavor"]
    temp = stock[i]["temperature"]
    
    print(f"Checking {cream}...")
    
    if temp > -17.5875:
        print("Not Cool Enough!")
    elif temp <= -17.5875:
        print("Ready for Serve!")
