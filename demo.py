class Parent():
    def __init__(self):
        self.data = "This is the public attribute"
    
    
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__data = "This is the private attribute"
        
c = Child()
print(c.data)
# print(c.__data) this will give an error 
print(c._Child__data)