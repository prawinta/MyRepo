class Person(object): 
     def getGender( self ): 
         return "Self" 
 

class Male( Person ): 
     def getGender( self ): 
         return "Male" 
 

class Female( Person ): 
     def getGender( self ): 
         return "Female" 
Boy = Male() 
Girl= Female()
Mine=Person()
print Boy.getGender() 
print Girl.getGender()
print Mine.getGender()
