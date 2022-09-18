# Exercise 1
def getdoublealphabet(alphabet):
    doublealphabet = alphabet + alphabet
    return doublealphabet

# Exercise 2
def getmessage():
    stringtoencrypt = input("Please enter the message you want to encrypt: ")
    return stringtoencrypt

# Exercise 3
def getcypherkey():
    shiftamount = input("Please enter a key (whole number fro, 1-25: ")
    return shiftamount

# Exercise 4
# Before writing the code, you should plan out the algorithm for encryption as follows:
# 1. Take three arguements: The message, the key and the alphabet
# 2. Initialize variables
# 3. Use for loop to traverse each letter in the message
# 4. For a specific letter, find the position
# 5. For a specific letter, determine the new position given the cypher key
# 6. If current letter is in the alphabet, append a new letter to the encrypted message
# 7. If current letter is not in the alphabet, append the current letter
# 8. Return the encrypted message after exhausting all letters in the message
def encryptmessage(message, cipherkey, alphabet):
    encryptedmessage = ""
    uppercasemessage = ""
    uppercasemessage = message.upper()
    for currentcharacter in uppercasemessage:
        position = alphabet.find(currentcharacter)
        newposition = position + int(cipherkey)
        if currentcharacter in alphabet:
            encryptedmessage = encryptedmessage + alphabet[newposition]
        else:
            encryptedmessage = encryptedmessage + currentcharacter
    return encryptedmessage

# Exercise 5
def decryptmessage(message, cypherkey, alphabet):
    decryptkey = -1 * int(cypherkey)
    return encryptmessage(message, decryptkey, alphabet)

# Exercise 6
# Before you look at the code, plan out your logic:
# 1. Define a string variable to contain the English alphabet.
# 2. To be able to shift letters, double your alphabet string.
# 3. Get a message to encrypt from the user.
# 4. Get a cipher key from the user.
# 5. Encrypt the message.
# 6. Decrypt the message.
def runcaesarcipherprogram():
    myalphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'alphabet: {myalphabet}')
    myalphabet2 = getdoublealphabet(myalphabet)
    print(f'alphabet2: {myalphabet2}')
    mymessage = getmessage()
    print(mymessage)
    mycipherkey = getcypherkey()
    print(mycipherkey)
    myencryptedmessage = encryptmessage(mymessage, mycipherkey, myalphabet2)
    print(f'Encrypted Message: {myencryptedmessage}')
    mydecryptedmessage = decryptmessage(myencryptedmessage, mycipherkey, myalphabet2)
    print(f'Decrypted Message: {mydecryptedmessage}')

runcaesarcipherprogram()