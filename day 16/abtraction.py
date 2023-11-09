from abc import ABC,abstractmethod

class computer(ABC):
    
    @abstractmethod
    def process(self,app):
        pass

    def run(self,app):
        self.process(app)
        
class laptop(computer):
    def process(self,app):
        print(f"{app} is running in laptop ")
        
class mobile(computer):
    def process(self,app):
        print(f"{app} is running in mobile")
        
laptop=laptop()
laptop.run("chrome")

mobile=mobile()
mobile.run("PUBG")



#inheritance example
# abstraction example