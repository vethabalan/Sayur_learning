#importing all the seperated files
from Birds_Main_File import *
from Crow_func_file import *
from Penguin_File import *
from Eagle_file import *
from Kiwi_file import *
        
#Assiging a variable for crow class       
Crow1 = Crow()
Crow2 = Crow()
#Assigning name for the above variables
Crow1.name = 'Bobo'
Crow2.name = 'Momo'
#Calling the function by each birds in the crow
Birds_details(Crow1)
print()
Birds_details(Crow2)
print()

#Assiging a variable for Penguin class 
Penguin1 = Penguin()
Penguin2 = Penguin()
#Assigning name for the above variables
Penguin1.name = 'Penny'
Penguin2.name = 'Pingo'
#Calling the function by each birds in the penguin
Birds_details(Penguin1)
print()
Birds_details(Penguin1)
print()

#Assiging a variable for Eagle class
Eagle1 = Eagle()
Eagle2 = Eagle()
#Assigning name for the above variables
Eagle1.name = 'Griffin'
Eagle2.name = 'Foxy'
#Calling the function by each birds in the Eagle
Birds_details(Eagle1)
print()
Birds_details(Eagle1)
print()

#Assiging a variable for Kiwi class
Kiwi1 = Kiwi()
Kiwi2 = Kiwi()
#Assigning name for the above variables
Kiwi1.name = 'Kiwis'
Kiwi2.name = 'Ludwig'
#Calling the function by each birds in the Kiwi
Birds_details(Kiwi1)
print()
Birds_details(Kiwi2)
print()