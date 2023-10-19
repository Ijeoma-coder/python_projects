import os


condition=""
scale_dirty= int(input("On a scale of one to ten, how dirty is your place?"))
if scale_dirty <= 4 :
        condition=("Sweep")
        print (condition)

elif scale_dirty > 4 and scale_dirty < 7 :
        condition=("Brush")
        print (condition)

elif scale_dirty > 8 and scale_dirty < 10:
        condition=("Sweep and Scrub")       
        print (condition)

        materials=["Klin","Ariel","Sunlight","Good Mama","Mama Lemon"]
        print(materials)

        choice_material= input("What material would you like us to use to mop?")

        if choice_material in materials :
            print("OK")
            bleach=input('''Would you like to apply Bleach? "Y or N" ''' )

            if bleach == "Y" or bleach== "Yes" or bleach =="y" or bleach=="yes" :
                bleach_condition = "Present"
                bleach_options=["Hypo","Jik",]
                print (bleach_options)
                
                bleach_decision= input("Which bleach product do you desire to use?")
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
         "Material = ", choice_material, '\n',
         "Bleach= ", bleach_condition, bleach_decision,'\n',
        )

        else:
            print('''Error.
             Please select a material to use.''')
            print(materials, choice_material)
        
       




        confirm=(input("Are your details correct?__"))
        
        def confirmation (confirm) :
            return
        yes=True
        no= False
        if confirm == yes:
         print ("OK")
        else :
         print("We're sorry, there seems to have been a mistake somewhere. Please re-do your selection."),
         import whatever.py    
        state= confirmation(confirm)

tp=0
fp=0
def price(number,tops) :
        if number > 5 and number < 8:
         fp= 6000
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

total= price(scale_dirty,bleach_condition)

print("Your total price is__", total)

