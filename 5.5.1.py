def is_valid_input(letter_guessed):
  if (len(letter_guessed)>1 and (letter_guessed.isalpha()==0)):
    print ('E3')
    return 0

  else:
   if len(letter_guessed)>1:
    print ('E1')
    return 0
   elif letter_guessed.isalpha()==0:
    print ('E2')
    return 0
   else:
    print (letter_guessed.lower())
    return 1
 
 
result= is_valid_input (input ("insert letter:"))
print (result)