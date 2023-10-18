from string import ascii_lowercase as letters

print('==='*30)
print(f'{"--- CAESAR CIPHER SCRIPT ---":>57s}')
print('==='*30)


def encrypt_and_decrypt_text(text, key, mode):
    """ This is a function to encrypt or decrpyt a text using Caesar's cipher. """
    result_text = ''    # result of the ciphered or plain text.

    if mode == 'd':
        key = -key  # negate key because decryption involves backward shifting -> move backwards from let's say e through z.
    
    for letter in text:
        letter = letter.lower()

        if not letter.isspace():    # if letter is not a space
            index = letters.find(letter)    # find the index of the letter. if the letter is not found, it return -1
            if index == -1:   # -1 is returned if the letter is a special character or a number
                result_text += letter
            
            else:
                newindex = index + key  # in decryption mode due to backward shifting,  the formula can be 5 + (-6).
                
                if newindex >= len(letters):   # last index is 25 for the 26 letters.
                    newindex -= len(letters)
                elif newindex < 0:  # if newindex is a negative integer.
                    newindex += len(letters)

                result_text += letters[newindex]
        
        else:
            print(f'Whitespace detected!')  # if the input is whitespace (tab or space), print this.
    
    return result_text

if __name__ == '__main__':
    print('Do you wish to encrypt or decrypt? ')
    mode = str(input('Choose your mode (e/d): ')).lower()

    if mode == 'e':
        print('*** Encryption mode selected. ***')
        key = int(input('Enter a key (1 through 26): '))
        text = str(input('Enter the text to encrypt: '))
        ciphertext = encrypt_and_decrypt_text(text, key, mode=mode)     # plain text to be ciphered.
        print()
        print(f'Cipher text: {ciphertext}')
    
    if mode == 'd':
        print('*** Decryption mode selected. ***')
        key = int(input('Enter a key (1 through 26): '))
        text = str(input('Enter the text to decrypt: '))
        plaintext = encrypt_and_decrypt_text(text, key, mode=mode)  # convert ciphered text to plain text.
        print()
        print(f'Plain text: {plaintext}')