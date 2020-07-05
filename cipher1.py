
def find_in_list(query, mainlist):# def is key word in that find_in_list is a variable in that i pass two paramiter.query for our password input first letter. and main list mense chars list first elements.
    mainlist_len = len(mainlist)#i difine mainlist_len variable in that i difine len mainlist.26
    # print(mainlist_len)
    range_for_loop = range(mainlist_len)# i difine frange_for_loop variable in that i assign range of mainlist_len. (0,26)
    # print(range_for_loop)
    index = None#index value is None mense 0 nothing is inside the index the variable 
    for i in range_for_loop:#i difine i variable for starting our loop to range_for_loop meanse 0 to 26 it will itereated. 
        element = mainlist[i]# i difine element variable in that i assign mainlist[i] value.
        if element == query:#in if condition i wrote element value is equal to equal to query .
            index = i# number of your elements
            return index # then i reterun index.

chars =         ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
shifted_chars = ['c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b']

def encrypt_message(plain_msg):
    encrypted_msg = ""#this is empty variable in that i assign " " value.
    for character in plain_msg:# in loop it will check  character in  plain_msg(plain_message) or not. 
        if character in chars:#if character in chars list if yes then excute the inside code.
            char_index = find_in_list(character, chars)# i difine char_index inside this variable i called the find_in_list_function.
            new_char = shifted_chars[char_index]#i difine new_char variable in that i assign shifted_chars[char_index] value.
            # print(new_char)
            encrypted_msg = encrypted_msg + new_char # encrypted_msg = encrypted_msg string value pluse new_char 
        else:
            encrypted_msg = encrypted_msg + character#encrypted_msg = encrypted_msg string value pluse  character.
    # print(encrypted_msg)
    return(encrypted_msg)

def decrypt_message(encrypted_msg):
    decrypted_msg = ""
    for character in encrypted_msg:
        if character in shifted_chars:
            char_index = find_in_list(character, shifted_chars)
            new_char = chars[char_index]
            decrypted_msg = decrypted_msg + new_char
        else:
            decrypted_msg = decrypted_msg + character
    # print(decrypted_msg)
    return(decrypted_msg)

############################################### Code starts from here ##################################################
flag = True# i difine one variable flag in that i assign True value.
while flag :#if while condition is True .
    choice = input("What do you want to do? 1. Encrypt a message 2. Decrypt a message  Enter `e` or `d` respectively!")
    if choice == 'e':# if choice is equeal equal to e .then execute inside the code.
        plain_message = input("Enter message to encrypt??")#ask user to write encrypt message.
        print(encrypt_message(plain_message))#i called encrypt_message in that i pass the plain_message argument.
        flag = False# then i assign False value in flag variable.
    elif choice == 'd':
        encrypted_msg = input("Enter message to decrypt?")
        print(decrypt_message(encrypted_msg))
        flag = False
    else:
        play_again = input("Do you want to try agian or Do you want to exit? (Y/N)")
        if play_again == 'Y':
            continue
        elif play_again == 'N':
            break