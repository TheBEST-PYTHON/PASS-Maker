# password maker 
# you can do this app for create strong password !!
import os
import random
os.system('cls'or 'clear')

class color:
    GREEN = '\033[92m'
    RED = '\033[91m'
    WHTIE = '\033[0m'
    YELLOW = '\033[93m'
    sed = '\033[96m'
    
print(color.GREEN+'=======>>> (: PASSWORD :) <<<=======')
print(color.RED+'=======>>> (: MAKER,GENRATOR :) <<<======')
print('----------------------------------------------------')
print('----------------------------------------------------')

chars = 'QWERTYUIOPSDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm!@#$%^&*1234567890?'

number = int(input(color.YELLOW + 'enter how many password make =====> '))
leng = int(input(color.YELLOW + 'enter lengtch of pass =====>'))

class passd:
    for pwd in range(number):
        password = ''
        for i in range(leng):
            password += random.choice(chars)
        print(color.RED +'---------------------------------------------------')
        
        print(color.sed + password)
        
        print(color.RED +'---------------------------------------------------')
        
        print(color.YELLOW + 'PSSWORD MAKE SUCEFULLY :) SEE YOU (:')

