class flashcards:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):
        return self.word+":"+self.meaning   
    
flash=[]
while True:
    word=input("ENTER THE WORD")
    meaning=input("ENTER THE MEANING")
    
    flash.append(flashcards(word,meaning))
    option=int(input("enter 1 for dicontinue 0 for countinue"))
    if option:
        break
    
for i in flash:
    print(i)    
    
