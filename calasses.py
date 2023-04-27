# -*- coding: utf-8 -*-

#%%
class Matematik:
    def __init__ (self,sayi1,sayi2):
        self.sayi1=sayi1
        self.sayi2=sayi2
        
    def topla ( self):
        return self.sayi1 + self.sayi2
    
    def cıkar ( self):
        return self.sayi1 - self.sayi2
    
    def carp ( self):
        return self.sayi1 * self.sayi2
    
    def bol ( self):
        return self.sayi1 / self.sayi2
    
    
matematik = Matematik(55,5)
print("Sonuc:"+str (matematik.topla()))
#%%
class person:
    def __init__ (self,firstname,lastname,age):
        self.firstname=firstname
        self.lastname=lastname
        self.age=age
        
person1=person("Saban","Suren","24")
print(person1.firstname)  

class worker (person):
    def __init__ (self,salary):
        self.salary=salary
        
        
        
        
class customer (person):
    def __init__ (self,creditcardnumber):
        self.creditcardnumber=creditcardnumber
        
ahmet=worker() 
 

mehmet=customer()   
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    