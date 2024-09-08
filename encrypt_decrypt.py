import string
# to handle both upper and lower case 
char = string.ascii_lowercase + string.ascii_uppercase

# function to encrpyt
def encrypt(word, key):
            cipher_text=''
           
            for letter in word:
                if letter in char:
                    index = char.find(letter) + key
                    
                    # to handle index out of range , this will reverse the index back to starting if out of range happens.
                    if index >= len(char):
                        index -=len(char)
                    cipher_text +=char[index]
                else:
                    cipher_text +=letter
            print('Encrypted word: '+ cipher_text)
            
#function to decrypt
def decrypt(word, key):
            cipher_text=''
            for letter in word:
                if letter in char:
                    index = char.find(letter) - key
                    cipher_text +=char[index]
                else:
                    cipher_text +=letter
            print('Descrypted word: '+cipher_text)

while True:
    # Show menu
    print('1. Encrypt \n2. Decrypt \n3. Exit')
    case = input("Choose one of the options: ")

    # Handle user selection
    match case:
        case '1':
            encrypt_input = input("Enter the word you want to encrypt: ")
            shift = int(input('Enter the number for shift: '))
            encrypt(encrypt_input, shift)

        case '2':
            encrypt_input = input("Enter the word you want to decrypt: ")
            shift = int(input('Enter the number for shift: '))
            decrypt(encrypt_input, shift)

        case '3':
            print("Exiting...")
            break

        case _:
            print("Invalid option. Please try again.")