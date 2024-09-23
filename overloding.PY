class fun:
    def __init__(self,game):
        self.game=game
    def __lt__(self,others):
        if self.game<others.game:
            print("game is less than others")
        else:
            print("others is less than game")
    def __eq__(self,others):
        if self.game==others.game:
            print("both are equel")
        else:
            print("both are not equel")
        
obj1=fun(5)
obj2=fun(2)               
print(obj1<obj2)
print(obj1==obj2)