from random import randint # random is labrary and we are import randint meanse randamely from this library.
#variables for the aline
aline = True# aline is variable in that i assign True value.
stamina = 10 #we took stamina varible in that i assign 10 value.

#This function runs each time you attack the alien.
def report(stamina):# def is a pree difine kewword report is a varible ()parntates and inside the prantates i pass the parameter  
	if stamina > 8:#if stamina is greater than 8 then exceute the print line. 
		print("The aline is strong! It resists your pathetic attack!")
	elif stamina > 5:#if , if condition is false then it will check elif condition if this is also false then it will check next elif statement.
		print("With a loud grunt, the alien stands firm.")
	elif stamina > 3:
		print("Your attack seems to be having an effect! The aline stumbles!")
	elif stamina > 0 :
		print("The alien is certain to fall soon! It staggers and reels!")
	else: # if all the condition is false it will execute the else statement.
		print("That's it! The alien is finshed!")


def fight(stamina):# def is a pree difine keyword fight is variable and inside the paramiter i pass the paramiter.
	while stamina > 0:# in while condition i give condition statement greater then 0
		response = input("> Enter a move 1. hit 2.attack 3.fight 4.run :- ")# i took user input in response variable.
		#Chose a response from (Hit,attack, fight and run)
		if "hit" in response or "attack" in response:#if user will give hit or attack in response variable then 
			less = randint(0,stamina)# i difine less variable in that i assign  randint 0 , stamina (randam 0 to stamina it will take in less varible)
			stamina -= less# subtract random int from stamina.
			report(stamina)#i call the report function .
		elif "fight" in response:#we can write "fight" == response. then also it will give same output.
			print("Fight how? You have no weapons, silly space traveler!")
		elif "run" in response:
			print("Sadly,there is nowhere to run.")
			print("The spaceship is not very big.")
		else:
			print("The alien zaps you with its powerful ray gun!")
			return True# it will provide return true value. if we are not return this value our loop will not stop.
	return False# it will return False value. when it will return false then out of loop condition will started executing.
print("A threatening alien wants to fight you!\n")# \n for coming second line.
#quotes at the end.
# call the function - what is returns will be the value of alive 
alive = fight(stamina)
if alive:#means if alive == True
	print("\nThe alien lives on,and you, sadly ,do not.\n")
else:
	print("\n The alien has been vanquished .Good Work!\n")

