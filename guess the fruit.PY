import random 
class fruit_quiz:
    a=["mango","banana","apple","grapes","strawberry","papaya","coconut","watermelon","melon"]
    computer=random.choice(a)
    user=input("enter the choice")
    if user==computer:
        print("you won the match  ")
    else:
        print("computer won the match the answer is", computer)
obj=fruit_quiz()        
