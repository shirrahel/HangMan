def AvailableChar(char):
 
 if (len(char)>1 and (char.isalpha()==0)):
    print ('E3')

 else:
   if len(char)>1:
    print ('E1')
   elif char.isalpha()==0:
    print ('E2')
   else:
    print (char.lower())
   
letter=input("insert letter: ")
AvailableChar(letter)