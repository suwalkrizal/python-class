class Grandfather:
    
    def __init__(self):
        print(f"Grandfather owns {self.car}")
    
    car = "lambo"

class Father(Grandfather):
    def __init__(self):
        self.car = "ferrari"
        super().__init__()
        print(f'Father owns {self.car}')
        
        
    house = "luxery house"
    
class Mother:
    jewellary = "dimond necklace"
    
class Son(Father,Mother):
    game_boy = "ps5"

son = Son()
# print(Son.house)
# print(Son.car)
# print(son.game_boy)
# print(son.jewellary)