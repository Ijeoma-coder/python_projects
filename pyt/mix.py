weather= []

for i in range(5) :
    weather.append(int(input("Rain quantity :" )))

avg_rain= ((weather[0] + weather[1] + weather[2] + weather[3] + weather[4] ) / len(weather))

print (avg_rain)


if avg_rain > 180 :
    print("They've curse you ooo!!!!!!!")
elif avg_rain > 120 :
    print("Get ready for a storm!!!!!")  
elif avg_rain < 120  : 
    print ("Your kinda safe? ")
elif avg_rain < 100 :
    print("Don't Bother.")    

else : print ("Your in the safara.")    
