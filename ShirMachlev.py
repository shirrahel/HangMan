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

def uniques( your_string ):    
    seen = set()
    return ' '.join( seen.add(i) or i for i in your_string.split() if i not in seen )

def choose_word(file_path, index):
 with open(file_path,"r") as input_file:
  Words = input_file.read()
  UniquesWords = uniques(Words)

  
  
  SumOfUniWords= len(UniquesWords.split())
  if index>len(Words.split()):
   index= index%len(Words.split())
   
  SecretWord=Words.split(' ')[index-1]
 
 return (SumOfUniWords,SecretWord)

def FirstPose():
 return ("""    x-------x""")
    
def SecondPose():
 return ("""    x-------x
    |
    |
    |
    |
    |
""")
 
def ThirdPose():
 return ("""    x-------x
    |       |
    |       0
    |
    |
    |
""")

def FourthPose():
 return ("""    x-------x
    |       |
    |       0
    |       |
    |
    |
""")
    
def FithPose():
 return ("""    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
""")
 
def SixthstPose():

 return  ("""    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |""")

def SeventhtPose():
 return ("""    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |""")

def print_hangman(num_of_tries):
  print(HANGMAN_PHOTOS[num_of_tries])
  
def GuessLetter():
 guess=input ("Guess a letter: ")
 return guess
 
def is_valid_input(letter_guessed):
  if (len(letter_guessed)>1 or (letter_guessed.isalpha()==0)):
    
    return 0

  else:
  
    return 1
    
def PrintReminder(old_letters_guessed):
  old_letters_guessed.sort()
  
  print (*old_letters_guessed, sep='->')

 
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
 letter_guessed=letter_guessed.lower()
 length=len(old_letters_guessed)
    
 if ((letter_guessed in old_letters_guessed) or (is_valid_input(letter_guessed)==0)):
  print ('X')
  if len(old_letters_guessed)>1:
   PrintReminder(old_letters_guessed)
  return 0
 else:
  old_letters_guessed.append(letter_guessed)
  PrintReminder(old_letters_guessed)
  return 1
  
def check_correct(guessLetter, SecretWord):

 if guessLetter in SecretWord:
   return 1
 else:
   return 0

def checkcorrecT(guessLetter, SecretWord):

 if (SecretWord.find(guessLetter)!=-1):
   
   return SecretWord.find(guessLetter)
 else:
  
   return -1
   
def check_win(secret_word, old_letters_guessed):
 count=0
 for i in secret_word:
  if secret_word[count] in old_letters_guessed:
   count+=1
  
 
 if count== len(secret_word):
   return 1
 else:
   return 0
   
   
HANGMAN_PHOTOS= {1:FirstPose(),2:SecondPose(),3:ThirdPose(),4:FourthPose(),5:FithPose(),6:SixthstPose(),7:SeventhtPose()}
old_letters_guessed=[]
counter_fails=0

printHangman()
NumberOfGuesses=NumOfGuesses(5,10)
print(NumberOfGuesses)

file_path=input("Enter file path: ")
secret_index=int(input ("Enter index: "))
print ("""
Let’s start!
""")

(SumOfUniWords,SecretWord)=choose_word(file_path, secret_index)

print_hangman(1)
print ("   ","_ "*len(SecretWord))



while counter_fails<6:
 guess_letter=GuessLetter()
 
 while try_update_letter_guessed(guess_letter, old_letters_guessed)==0:
  guess_letter=GuessLetter()
 
 
 if checkcorrecT(guess_letter, SecretWord)==-1:
   counter_fails+=1
   print (":(")
   
   print_hangman(counter_fails+1)
 else:
   if check_win(SecretWord,old_letters_guessed)==1:
    print (SecretWord)
    print ("WIN")
    break
   
   else:
    
    print ("   ","_ "*len(SecretWord))
 
if counter_fails==6:
 print ("LOSE")