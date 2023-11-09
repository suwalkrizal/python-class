class person:
    def __init__(self) -> None:
        self.name = "Ram"
        self._age = 12
        self.__salary = "17k"
        
    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self,salary):
        self.__salary = salary
        
        # salary = property(getting, setter)
        
        
person=person()
person.name = "Hari"
print(person.name)
print(person._age)
print(person.salary)


person.salary="19k"


