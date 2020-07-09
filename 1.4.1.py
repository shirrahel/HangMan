import random


def printHangman():
 print("""  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/""")
                     
def NumOfGuesses(a,b):

 return random.randint(a,b)
                   
printHangman()

NumberOfGuesses=NumOfGuesses(5,10)

print(NumberOfGuesses)
                       