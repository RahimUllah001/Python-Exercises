target = "correct"
guess = ""
guess_limit = 3

while guess != target and guess_limit != 0 :
    guess = input("enter your guess: ")
    guess_limit -= 1
  
if guess == target:
    print("u win. ")
else:    
    print("u lose. ")
    

    

  