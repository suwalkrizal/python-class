class pizza:
    
    def dough(self):
        print("dough")
        return self
    
    
    def sauce(self):
        print("sauce")
        return self
    
    def salade(self):
        print("salade")
        return self
    
    def chicken(self):
        print("chicken")
        return self
    
    def cheese(self):
        print("cheese")
        return self
    
    
pizza = pizza()

pizza\
    .dough()\
    .sauce()\
    .salade()\
    .chicken()\
    .cheese()