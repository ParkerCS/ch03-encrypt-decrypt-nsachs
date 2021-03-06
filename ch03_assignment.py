# MODULES AND LIBRARIES
'''
For this assignment, we will practice the use of imports to encrypt and decrypt messages.
The functions are already contained in the files.  Your job is to use them to encrypt and decrypt strings.  Good luck
'''

from decode import decode
from encode import encode
from encryption_key import key

#1 Decrypt this message using imports from the decode.py and encryption_key.py.  Make the result print in a friendly format that is easy for the user to understand. (10pt)
encrypted_message = "¿®ªªÈÙ®ÏT¤ÕEÓ¹âeCíÉÁÏº¢¡i¸ºÇ¿"
print(decode(key, encrypted_message))

#2 Encrypt your name and print the encrypted result.  Make the result print in a friendly format that is easy for the user to understand. (5pt)
print(encode(key, "Nina Sachs"))

#3 Decrypt the encrypted code from part 2 to ensure that it worked properly and print the result.  Make the result print in a friendly format that is easy for the user to understand. (5pt)
encrypted_message2 = "È¡³Q§Ò¨É¤"
print(decode(key, encrypted_message2))