import string 


def decrypt_caesar():
    letters = string.ascii_letters

    text = input("enter the text to decrypt: ")
    shift = int(input("enter the shift of cipher: "))

    decrypted_text= ''
    for i in range(len(text)):
        if text[i] == ' ':
            decrypted_text += ' '
        else:        
            index_of_decryptedLetter = letters.index(text[i])
            decrypted_text += letters[index_of_decryptedLetter+shift]

    print(decrypted_text)

def encrypt_caesar():
    letters = string.ascii_letters
    text = input("enter the text to encrypt: ")
    shift = int(input("enter the shift of cipher: "))

    encrypted_text= ''
    for i in range(len(text)):
        if text[i] == ' ':
            encrypted_text += ' '
        else:        
            index_of_encryptedLetter = letters.index(text[i])
            encrypted_text += letters[index_of_encryptedLetter-shift]

    print(encrypted_text)


choice = input("do you wanna encrypt or decrypt: ")

if choice == 'encrypt':
    encrypt_caesar()
elif choice == 'decrypt':
    decrypt_caesar()
else:
    print("don't make me mad, know what you want: ")
    