class shop1:
    
    def __init__(self):
        print(f"shop1 make {self.food}")
        
    food = "kima_noodle"
    
class shop2(shop1):
    
    def __init__(self):
        self.food = "MOMO"
        super().__init__()
        print(f"shop2 make {self.food}")
        

class shop3(shop2):
    item = "chewmin"
 
shop = shop3()   
print(shop3.food)
print(shop3.item)