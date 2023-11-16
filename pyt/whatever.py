import os
import sys

#correct error with wrong decision for soap, meant to go back not prnt
#fix condition for less than 8 scale of mess
def select_soap():
     global need
     need=input('Which soap do you want to use?')
   
     return need

def select_bleach():
     global bleach_decision
     bleach_decision= input('Which bleach do you want to use?') 
     return bleach_decision


def price(number,tops) :
    global tp, fp
    if number > 5 and number < 8:
          fp = 6000
    elif number == 5:
         fp= 5500
    elif number >= 8 :
         fp= 7500
    else :
         fp=4000

    if tops ==  "Present" :
             tp=fp + 1500
    else:
         tp=fp
    return tp


condition=""
scale_dirty= int(input("On a scale of one to ten, how dirty is your place?__"))
if scale_dirty <= 4 :
        condition=("Sweep")
        print (condition)
        bleach_condition='None'
        total= price(scale_dirty,bleach_condition)

        print('\033[1;3m' ,('Your total price is__', total ),'\033[0m')
        print('Thank you for using Bambi'), sys.exit(0)

elif scale_dirty > 4 and scale_dirty <= 7 :
        condition=("Brush")
        print (condition)
        bleach_condition='None'
        total= price(scale_dirty,bleach_condition)

        print('\033[1;3m' ,('Your total price is__', total ),'\033[0m')
        print('Thank you for using Bambi!'), sys.exit(0)

elif scale_dirty >= 8 :
        condition=("Sweep and Scrub")       
        print (condition)

        materials=["Klin","Ariel","Sunlight","Good Mama","Mama Lemon"]
        print(materials)

        select_soap()

        if need in materials :
            print("OK")
            bleach=input('''Would you like to apply Bleach? "Y or N" ''' )

            if bleach == "Y" or bleach== "Yes" or bleach =="y" or bleach=="yes" :
                bleach_condition = "Present"
                bleach_options=["Hypo","Jik",]
                print (bleach_options)
                
                select_bleach()
                if bleach_decision in bleach_options :
                    print("OK")
                else :
                    print("OK")    
            else :
                print ("OK")  
                bleach_condition="None"  
                bleach_decision=""

            print("Please confirm your details,",'\n',
          "condition = ", condition,'\n',
         "Material = ", need, '\n',
         "Bleach= ", bleach_condition, bleach_decision,'\n',
        )

        else:
            print('''Error.
             Please select a material to use.''')
            print(materials),select_soap()
        
       




        Yes= True
        No=False
        status_deal=(input("Are your details correct?__Yes or No  "))
       
       

        def confirmation (confirm) :
            
            if confirm== 'Yes' :
             print ("OK")
            else :
             print("We're sorry, there seems to have been a mistake somewhere. Please re-do your selection.")
             import whatever 
               
           
            
        state = confirmation(status_deal)
tp=0
fp=0

total= price(scale_dirty,bleach_condition)

print('\033[1;3m' ,('Your total price is__', total ),'\033[0m')



