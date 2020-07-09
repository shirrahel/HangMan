def check_win(secret_word, old_letters_guessed):
 count=0
 for i in secret_word:
  if secret_word[count] in old_letters_guessed:
   count+=1
  
 print("count=",count)
 if count== len(secret_word):
  return 1
 else:
  return 0
  
  
  
secret_word1 = "friends"
old_letters_guessed1 = ['d', 'e', 'i', 'f', 's', 'r']
print(check_win(secret_word1, old_letters_guessed1))