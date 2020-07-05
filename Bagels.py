import random#import is a library  
def getSecretNum(numDigits):# getSecreatNum will pass the paramiter to secreat number variable. (numDigits value =  3 means three digits number.)

  numbers = list(range(10))#number is a variable in that i assign list(range(10 )) menase 0 to 9 number it will take in list.
  random.shuffle(numbers)#it is taking random number from numbers variable list.
  secretNum = ''#empty variable in that i assign string value.
  for i in range(numDigits):# i is a variable it will work range of numDigits = 3
    secretNum += str(numbers[i])#Then it will store  in secreatNum string variable.
  return(secretNum)#when i loop will finsh then it will return secreatNum.

def getClues(guess, secretNum):#getClues function passing the parameter in guess and secretNum variable

  if guess == secretNum:#if your guess is equal equal then return "you got it."
    return 'You got it!'
  clue = []# clue is empty list
  for i in range(len(guess)):#for loop i in range of len of guess
    if guess[i] in secretNum[i]:#if guess and secretnum i value  is same then
      clue.append('Fermi')#append Fermi inside the clue.
    elif guess[i] in secretNum:#if guess i value inside the secretNum then 
      clue.append('Pico')# apped pico in clue.
    else:
      clue.append('None') #append None in clue.  
  return ' '.join(clue)# when we will return then clue we will join this all clue.

# def isOnlyDigits(num):
# # Returns True if num is a string made up only of digits. Otherwise returns False.
#   if num == '':
#     return True

#   for i in num:
#     if i not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
#       return True

def playAgain():#it will passing the argument in playAgain function.
    play = input("Do you want to play again? Yes or No?") # user input in play variable.
    if play == "Yes":# if paly is eqal to equal to yes 
      return(True)# then return True .
    else:
      return(False)# if not then return False.

#first this part will work .
NUMDIGITS = 3
MAXGUESS = 10

print('I am thinking of a %s-digit number. Try to guess what it is.' % (NUMDIGITS))
print('Here are some clues:')
print('When I say:    That means:')
print('  Pico         One digit is correct but in the wrong position.')
print('  Fermi        One digit is correct and in the right position.')
print('  None       No digit is correct.')
on = True# i assign True value in on variable.
while on:# True.
    
    secretNum = getSecretNum(NUMDIGITS)#inside secreatNum variable i call getsecreatNum(NUMDIGITS) function and i pass the NUMDIGITS = 3 value inside this argument.then getsecreatNum function will give secreat number.
    print (secretNum)# 
    print('I have thought up a number. You have %s guesses to get it.' % (MAXGUESS))# replace of %s % MAXGUESS value will print
    numGuesses = 1# numGuesses variable for loop

    while numGuesses <= MAXGUESS:#it will itreated 10 times 
        guess =input("Guess The number :-")#it will ask user to guess your number.
        if len(guess) == 3:
          clue = getClues(guess, secretNum)# inside the clue variable i called the getClues function and i pass guess and secretNum value in argument.
          print (clue)#after completing function it will return clue value then it will print
        
          numGuesses += 1# increment of numGuesses variable
          if guess == secretNum:# if guess == secretNum then it will break
            
            break
        else:
          print("Your guess shoud be three digit number")
          on = True
    if numGuesses > MAXGUESS:#if numGuesses greater then  MAXGUESS then it will excute the print statement.
      print ('You ran out of guesses. The answer was ' + str(secretNum))
  
    if not playAgain():#it will call the playAGain function.
      on = False# if it is not play again on value will change.
  
