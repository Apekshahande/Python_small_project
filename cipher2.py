def encrypt():
  message = input("Enter the message you want to encrypt")

  ascii_message = [ord(char)+3 for char in message]
  print([ord(char)+3 for char in message])# it is giving number in acii value numbers
  encrypt_message = [ chr(char) for char in ascii_message] 
  # print(encrypt_message) # it will print letter list
  print (''.join(encrypt_message))


def decrypt():
  message = input("Enter the message you want to decrypt")
  ascii_message = [ord(char) for char in message]
  decrypt_message = [ chr(char) for char in ascii_message]  
  print (''.join(decrypt_message))

flag = True
while flag:
  choice = input("What do you want to do? \n1. Encrypt a message 2. Decrypt a message \nEnter E or D respectively!")
  if choice == 'E' or "e":
    encrypt()
  elif choice == 'D' or "d":
    decrypt()    
  else:
      play_again = input("Do you want to try agian or Do you want to exit? (Y/N)")
      if play_again == 'Y':
          continue
      elif play_again == 'N':
          break
