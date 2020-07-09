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



HANGMAN_PHOTOS= {1:FirstPose(),2:SecondPose(),3:ThirdPose(),4:FourthPose(),5:FithPose(),6:SixthstPose(),7:SeventhtPose()}


def print_hangman(num_of_tries):
  print(HANGMAN_PHOTOS[7-num_of_tries])

print_hangman(6)
print_hangman(5)
print_hangman(4)
print_hangman(3)
print_hangman(2)
print_hangman(1)
print_hangman(0)
