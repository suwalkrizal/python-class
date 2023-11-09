from abc import ABC,abstractmethod

class food(ABC):
    
    @abstractmethod
    def process(self,item):
        pass
    
    def cooking(self,item):
        self.process(item)
    
class momo(food):
    def process(self,item):
        print(f"{item} is steaming.")
        
class chewmin(food):
    def process(self, item):
        print(f"{item} is being ready.")
        
        
momo = momo()
momo.cooking("buff momo")

chewmin = chewmin()
chewmin.cooking("buff chewmin")