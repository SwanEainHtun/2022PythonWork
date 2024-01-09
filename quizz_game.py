#----------------------------------------
def new_game():
    guessess = []
    correct_guesses = 0
    question_number = 1
    for key in questions:
        print("---------------------------------")
        print(key)
        for i in options[question_number-1]:
            print(i)
        guess = input("Enter 'A' OR 'B' OR 'C' OR 'D' : ").upper()
        guessess.append(guess)
        question_number +=1
        correct_guesses += check_answer(questions.get(key),guess)
    display_score(correct_guesses,guessess)
#-----------------------------------------
def check_answer(answer,guess):
    if answer == guess:
        print("CORRECT")
        return 1
    else:
        print("WRONG")
        return 0
#-------------------------------------------
def display_score(correct_guesses,guesses):
    print("---------------------------------")
    print("RESULT")
    print("---------------------------------")
    print("ANSWER  : ",end="")
    for i in questions:
        print(questions.get(i),end=" ")
    print()
    print("GUESSES : ", end="")
    for i in guesses:
        print(i,end=" ")
    print()
    score = int((correct_guesses/len(questions))*100)
    print("Your score is :"+ str(score)+"%")



#------------------------------------------
def play_again():
    response = input("Do you want to play again?(yes/no) : ")
    response = response.upper()
    if response == "YES":
        return True
    else:
        return False
#-------------------------------------------

questions= {"which kpop group has largest number of members: ":"B",
            "When was seventeen debuted? ":"B",
            "Whose song is peekaboo? ":"A",
            "Who gets national daughter award?":"C"}
options = [["EXO","NCT","TREASURE","SEVENTEEN"],
           ["2014","2015","2016","2017"],
           ["RED VELVERT","TWICE","SNSD","Black Pink"],
           ["Suzy","Yoona","IU","Jennie"]]
new_game()
while play_again():
    new_game()
print("BYEE!")