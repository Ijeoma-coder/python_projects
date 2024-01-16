import turtle 
import random
import time
import sys



#using the first line to make all  variables not used in functions accessible
player_name1=str(input("What's your name?"))
player_name2=str(input("What's your name?"))

no=[1,0]

p1_no=int(input("Pick a number between one and zero"))

p2_no=no[not p1_no]


#error w random select; COMPARISM OF LISTS INSTEAD OF INT 


import random
first_p= p1_no
second_p=p2_no


#function to determine who goes first and who goes second
def pick_no(first, second):
    global first_p,second_p  
     
    
    ran = random.randint(0, 1)

    if first > ran or second < ran:
        print(f"{player_name2} You go first")
        first_p=player_name2

        print(f"{player_name1} You go second")
        second_p=player_name1

    elif first < ran or second > ran:
        print(f"{player_name1} You go first")
        first_p=player_name1

        print(f"{player_name2} You go second")
        second_p=player_name2
        

    elif first > ran or second > ran:
        print(f"{player_name1} You go first")
        first_p = player_name1

        print(f"{player_name2} You go second")
        second_p=player_name2

    elif first < ran or second < ran:
        print(f"{player_name2} You go first")
        first_p=player_name2

        print(f"{player_name1} You go second")
        second_p=player_name1



pick_no(p1_no, p2_no)
#calling the function based on selected number

print("First Player:", first_p)
print("Second Player:", second_p)

move_item1=['one','two','three','four','five','six','seven','eight']#string translation of no of moves
move_item2=['one','two','three','four','five','six','seven','eight']#string translation of no of moves

itbs1=''
#for player 1

itbs2=''
#for player 2

#itbs means item to be selected which has a value changed every time the function of round_1() is called.
# the value is the corresponding word of the amount of correct answer the player has amounted 
# that is to say that this variable only experiences change when amswer is correct
#im using it to get the string and run it through the move function so as to enable actual movementas player progresses
     

#turtle preparation starts here




pone= turtle.Turtle()

ptwo=turtle.Turtle()

screen= turtle.getscreen()

pone.pen(speed=1, pensize=3, fillcolor='purple',pencolor='Purple')
ptwo.pen(speed=1, pensize =3, fillcolor='orange',pencolor='blue')

pone.down()
ptwo.down()

ptwo.up()
ptwo.goto(0,-100)
ptwo.down()

#turtle preparation ends here


def do_nothing():
    pass

#movement function for player 1
def move1_p1():
    pone.down()
    pone.fd(50)#1st step
    #first move

def move2_p1():
    pone.down()
    pone.fd(50)

    pone.fd(50)
    pone.lt(90)#2nd step
    #second move(2nd step+ 1st)

def move3_p1():
    pone.down()
    pone.fd(50)

    pone.fd(50)
    pone.lt(90)

    pone.fd(50)#3rd step
    #3rd move (3rd + 2nd + 1st step)

def move4_p1():
    pone.down()
    pone.fd(50)

    pone.fd(50)
    pone.lt(90)

    pone.fd(50)

    pone.fd(50)
    pone.lt(90) #4th step    
    #4th move(4th + 3rd + 2nd + 1st step)       

def move5_p1():
    pone.down()
    pone.fd(50)

    pone.fd(50)
    pone.lt(90)

    pone.fd(50)

    pone.fd(50)
    pone.lt(90)

    pone.fd(50)#5th step
    #5th move(5th + 4 + 3rd + 2nd + 1st step)

def move6_p1():
    pone.down()
    pone.fd(50)

    pone.fd(50)
    pone.lt(90)

    pone.fd(50)

    pone.fd(50)
    pone.lt(90)

    pone.fd(50)

    pone.fd(50)
    pone.lt(90)#6th step
    #6th move(6th + 5th +4th + 3rd + 2nd + 1st step)    

def move7_p1():
    pone.down()
    pone.fd(50)

    pone.fd(50)
    pone.lt(90)

    pone.fd(50)

    pone.fd(50)
    pone.lt(90)

    pone.fd(50)

    pone.fd(50)
    pone.lt(90)

    pone.fd(50)#7th step
    #7th move( 7+6+5+4+3+2+1) steps

def move8_p1():
    pone.down()
    pone.fd(50)

    pone.fd(50)
    pone.lt(90)

    pone.fd(50)

    pone.fd(50)
    pone.lt(90)

    pone.fd(50)

    pone.fd(50)
    pone.lt(90)

    pone.fd(50)
    pone.fd(50)#8th step
    #8th move (8+7+6+5+4+3+2+1) steps


#movement functions for player 2
def move1_p2():
    ptwo.down()
    ptwo.fd(50)#1st step
    #1st move

def move2_p2():
    ptwo.down()
    ptwo.fd(50)

    ptwo.fd(50)
    ptwo.lt(90)#2nd step 
    #2nd move(2nd step + 1st step)

def move3_p2():
    ptwo.down()
    ptwo.fd(50)

    ptwo.fd(50)
    ptwo.lt(90)

    ptwo.fd(50)#3rd step
    #3rd move(3rd step+ 2nd step+ 1st step)

def move4_p2():
    ptwo.down()
    ptwo.fd(50)

    ptwo.fd(50)
    ptwo.lt(90)

    ptwo.fd(50)

    ptwo.fd(50)
    ptwo.lt(90) #4TH STEP
    #4th move(4th step + 3rd step + 2nd step + 1st step)           

def move5_p2():
    ptwo.down()
    ptwo.fd(50)

    ptwo.fd(50)
    ptwo.lt(90)

    ptwo.fd(50)

    ptwo.fd(50)
    ptwo.lt(90)

    ptwo.fd(50)#5th step
    #5th move(5th step + 4th step + 3rd step + 2nd step + 1st step)

def move6_p2():
    ptwo.down()
    ptwo.fd(50)

    ptwo.fd(50)
    ptwo.lt(90)

    ptwo.fd(50)

    ptwo.fd(50)
    ptwo.lt(90)

    ptwo.fd(50)

    ptwo.fd(50)
    ptwo.lt(90)    #6th step
    #6th move( 6th step +  5th step + 4th step + 3rd step + 2nd step + 1st step)

def move7_p2():
    ptwo.down()
    ptwo.fd(50)

    ptwo.fd(50)
    ptwo.lt(90)

    ptwo.fd(50)

    ptwo.fd(50)
    ptwo.lt(90)

    ptwo.fd(50)

    ptwo.fd(50)
    ptwo.lt(90) 

    ptwo.fd(50)#7th step
    #7th move( 7th step + 6th step + 5th step + 4th step...)

def move8_p2():
    ptwo.down()
    ptwo.fd(50)

    ptwo.fd(50)
    ptwo.lt(90)

    ptwo.fd(50)

    ptwo.fd(50)
    ptwo.lt(90)

    ptwo.fd(50)

    ptwo.fd(50)
    ptwo.lt(90) 

    ptwo.fd(50)

    ptwo.fd(50)    #8th step
    #8th move( 8th step + 7th step + 6th step + 5th step + 4th step...)    

## Function to move player 1 on the Turtle graphics board
def move_1(item):
    if item=='one':
        move1_p1()
    elif item=='two':
        move2_p1()
    elif item=='three':
        move3_p1()
    elif item=='four':
        move4_p1()
    elif item=='five':
        move5_p1()
    elif item=='six':
        move6_p1()
    elif item=='seven':
        move7_p1()
    elif item=='eight':
        move8_p1()                            


# Function to move player 2 on the Turtle graphics board
def move_2(item2):
    if item2=='one':
        move1_p2()
    elif item2=='two':
        move2_p2()
    elif item2=='three':
        move3_p2()
    elif item2=='four':
        move4_p2()
    elif item2=='five':
        move5_p2()
    elif item2=='six':
        move6_p2()
    elif item2=='seven':
        move7_p2()
    elif item2=='eight':
        move8_p2()   



#had to use list constructor because the programme identified list as tuple
questions = list((
    "What is the capital of France?",
    "Who painted the Mona Lisa?",
    "What is the powerhouse of the cell?",
    "What year did World War II end?",
    "What is the largest planet in our solar system?",
    "Who developed the theory of relativity?",
    "What is the chemical symbol for gold?",
    "What is the process of a liquid turning into a gas called?"))




questions_2=list((
    "What is the square root of 64?",
    "Who wrote 'Romeo and Juliet'?",
    "What is the freezing point of water in Celsius?",
    "What is the largest ocean on Earth?",
    "What is the chemical formula for water?",
    "Which gas do plants use for photosynthesis?",
    "What is the closest star to Earth?",
    "What is the formula for the area of a circle?"))


answers = list((
    'paris',
    'leonardo da vinci',
    'mitochondria',
    '1945',
    'jupiter',
    'albert einstein',
    'au',
    'evaporation'))




answers_2=list((  #type: ignore
    '8',
    'william shakespeare',
    '0 degrees celsius',
    'pacific ocean',
    'h2o',
    'carbon dioxide',
    'sun',
    'pi r squared'))


#i decided to make global variable within the functios rather than making thee variables out of the functions
correct_ans1=0
moves_p1=0

correct_ans2=0
moves_p2=0    


def round_1():
    global moves_p1,correct_ans1,itbs1
    global questions
  
  
    print(f"Player 1 turn,{first_p}")

    give_que_index = random.randint(0, (len(questions))-1 )#selects a question randomnly
    give_que = questions[give_que_index]

    print(questions[give_que_index])

    questions.remove(give_que)


    
    #removes the question from the list and brings it out of the list

    start_time = time.perf_counter()
   #STARTS TO COUNT FROM WHEN THE FUNCTION WAS CALLED
    

    ans_give1=(input("What's the answer?____")).lower()
    moves_p1+=1

    end_time = time.perf_counter()
    #FINISHES AFTER USER ANSWERS QUESTIONS 
    
    time_for_p1 = int(end_time - start_time)
    print(f"You elapsed {time_for_p1}seconds")

    if ans_give1 == answers[give_que_index] and time_for_p1<= 10:
        print('Correct') 
        correct_ans1+=1
        
        itbs1=(move_item1[correct_ans1-1])
        move_1(itbs1)
        #allows player to move in accordane to no of correct answer, read my itbs1 comment to understand

        time.sleep(5)
       
    elif time_for_p1 >=10 :
        print(f'\033[1;3m','Out of time',{first_p},'\033[0m;')      
        time.sleep(5)

    elif ans_give1!= answers[give_que_index]:
        print('\033[1;3m',"Wrong Answer heediot",'\033[0m')    
        time.sleep(5)


def round_2():
    global moves_p2,correct_ans2,itbs2
    global questions_2
    

  
    print(f"Player 2 round,{second_p}")

    moves_p2+=1

    give_que2_index=random.randint(0,(len(questions_2))-1)    
    give_que2= questions_2[give_que2_index]
    
    questions_2.remove(give_que2)
    
    print(give_que2)
    #removes the question from the list and brings it out of the list

    start_time2=time.perf_counter()
    #starts timer for round

    ans_give2=(input("What's the answer?____" )).lower()
    end_time2=time.perf_counter()

    time_for_p2= int(end_time2 - start_time2)
    print(f"You elapsed {time_for_p2}seconds")

    if ans_give2== answers_2[(give_que2_index)] and time_for_p2<10:
        print ("Correct answer.")
        correct_ans2+=1
        itbs2=move_item2[(correct_ans2-1)]
        #uses the no of correct answers to find the string translation in list of string moves
        move_2(itbs2)
        #allows player to move in accordane to no of correct answer, read my itbs1 comment to understand
        time.sleep(5)


    elif time_for_p2>10:
        print(f'\033[1;3m',"Out of time for", {second_p},'\033[0m')
        time.sleep(5)

    elif ans_give2!= answers_2[give_que2_index]:
        print('\033[1;3m',"Wrong Answer heediot",'\033[0m')    
        time.sleep(5)

#winning decision based on mumber of correct numbers
def decide_win():
    fav_p1=correct_ans1-correct_ans2
    fav_p2= correct_ans2- correct_ans1

    if correct_ans1 > correct_ans2:
        if fav_p1> 2:
            print(f"{first_p} WINS, close victory")
        elif fav_p1> 5:
            print(f"{first_p} WINS, flawless victory")
        elif fav_p1> 7:
            print(f"{first_p} WINS, FATALITY")
        print("Thanks for playing, it means a lot, hope you had fun")
        sys.exit()

    elif correct_ans2 > correct_ans1:
        if fav_p2> 2:
            print(f"{second_p} WINS, close victory")
        elif fav_p2> 5:
            print(f"{second_p} WINS, flawless victory")
        elif fav_p2> 7:
            print(f"{second_p} WINS, FATALITY")
        print("Thanks for playing, it means a lot, hope you had fun")    
        sys.exit()

    else:
        print(f"It's a tie between {first_p}, and {second_p}.")
        print(f"I guess that means both of y'all are dumb, thanks for playing"), sys.exit()
        
#winning condition when moves arent exceeded but one player has more correct answers than the other player
while correct_ans1<8 and correct_ans2 < 8 and moves_p1 < 8 and moves_p2 < 8:
    round_1()
    round_2()
#winning condition when a player runs out of moves 
    if moves_p1>=8 or moves_p2>=8:
        if moves_p1>=8:
            print(f"{second_p} is out of Moves")
        elif moves_p2>=8:  
            print(f"{first_p} is out of Moves")  
        decide_win()      
    
else:
    decide_win()         






