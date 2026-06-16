import pyperclip
  5
.   6 . # the string to be encrypted/decrypted
  7 . message = 'This is my secret message.'
  8
.   9 . # the encryption/decryption key
 1 0. key = 13
 1
1.  1 2. # tells the program to encrypt or  decrypt
 1 3. mode = 'encrypt' # set to 'encrypt' or 'decrypt'
 1
4.  1 5. # every possible symbol that can be encrypted
 1 6. LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
 1
7.  1 8. # stores the encrypted/decrypted form of the message
 1 9. translated = ''
 2
0.  2 1. # capitalize the string in message
 2 2. message = message.upper()
 2
3.  2 4. # run the encryption/decryption code on each symbol in the message string
 2 5. for symbol in message:
 26.     if symbol in LETTERS:
 27.         # get the encrypted (or decrypted) number for this symbol
 28.         num = LETTERS.find(symbol) # get the number of the symbol
 29.         if mode == 'encrypt':
 30.             num = num + key
 31.         elif mode == 'decrypt':
 32.             num = num -  key