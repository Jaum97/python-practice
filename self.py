//https://medium.com/quick-code/understanding-self-in-python-a3704319e5f0

class SomeClass:
    variable_1 = “ This is a class variable”
    variable_2 = 100    #this is also a class variable.

    def __init__(self, param1, param2):
        self.instance_var1 = param1
        #instance_var1 is a instance variable
        
	      self.instance_var2 = param2   
        #instance_var2 is a instance variable
        
        
        
>>> obj1 = SomeClass("some thing", 18) 
#creating instance of SomeClass named obj1
        
>>> obj2 = SomeClass(28, 6) 
#creating a instance of SomeClass named obj2

>>> obj1.variable_1
'a class variable'

>>> obj2.variable_1
'a class variable'
        
>>> obj1.instance_var1
'some thing'
        
>>> obj2.instance_var1
28
