import os
import os.path
import logging

height=float(input("How tall are you?"))

big = True
small = False

body_size = bool(input("Are you big or small?  "))

if body_size == big :
    fit=True
    fat= False
    sub=bool(input("Are you fit-big or fat-big ?"))

elif body_size == small : 
    fit=True
    lanky=False
    bestie= bool(input("Are you fit-small or lanky-small?")) 

body_count= int(input("Number of smashes you've had__ "))

dark= True
light = False

skin_color = bool(input("What's your skin colour?__ "))

ukwu= bool(input("How is your bom-bom?__"))

big=True
small=False

if height >= 179 and body_size == fit and body_count <= 2 and skin_color == dark and ukwu == big and (sub == fit or bestie==fit) :
    print ("AWWWWWWWWWWWWWWWWWWWWWWWWWWW!") 
    print('\033[1;3m' , "Now for the personality part of the test !!", '\033[0m')

    personality= ['funny', 'smart', 'goal-driven', 'polite', 'sassy', 'dumb', 'playful','cook', ]
    print (personality)

    n=int(input("How many of these personality traits, do you have?"))
    personal=[]

    for i in range(n) : 
     div= input("Which of them are you? ")
     personal.append(div) 

    if personal == ['funny', 'smart','sassy','polite'] :  
        print("You're good for Kaira")
    elif personal == [ 'funny', 'smart','sassy','goal-driven'] :
        print("You're good for Mokut ")    
    
    print ("NOW FOR THE FINAL QUESTION?")
    yes=True
    no= False
    
    status_quo= bool(input("Are you willing to spend crazy money on me?____ "))
    if status_quo == yes : 
        print("Welcome to my Heart BABYYYY!!!!!")
    else :
        print('\033[1;3m' +  "WE COULD'VE WORKED OUT, but YOU BROKE !!" + '\033[0m')    

 



    
    
else : print("Sorry for you boo!")   