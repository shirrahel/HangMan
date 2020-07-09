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
    
def PrintReminder(old_letters_guessed):
  old_letters_guessed.sort()
  
  print (*old_letters_guessed, sep='->')


def print_old_letters_guessed(old_letters_guessed):
 print (old_letters_guessed)
 
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
 letter_guessed=letter_guessed.lower()
 length=len(old_letters_guessed)
 if letter_guessed in old_letters_guessed or is_valid_input(letter_guessed)==0:
  print ('X')
  PrintReminder(old_letters_guessed)
  return 0
 else:
  old_letters_guessed.append(letter_guessed)
  print_old_letters_guessed(old_letters_guessed)
  return 1

old_letters_guessed=['a', 'p', 'c', 'f']  
while True:
 
 letter=input("insert letter: ")
 try_update_letter_guessed(letter, old_letters_guessed)