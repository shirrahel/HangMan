def uniques( your_string ):    
    seen = set()
    return ' '.join( seen.add(i) or i for i in your_string.split() if i not in seen )


def choose_word(file_path, index):
 with open(file_path,"r") as input_file:
  Words = input_file.read()
  UniquesWords = uniques(Words)
  print (Words)
  print (UniquesWords)
  
  SumOfUniWords= len(UniquesWords.split())
  if index>len(Words.split()):
   index= index%len(Words.split())
   
  SecretWord=Words.split(' ')[index-1]
 
 return (SumOfUniWords,SecretWord)
 
print(choose_word(r"C:\Users\Shir\Desktop\Hangman\TheProject\words.txt", 18))
