class Cipher:

  def halliday(self, message):
    # simple caesar decipher
    # Crystal Key = Pelfgny Xrl
    # Orb of Osuvox = Beo bs Bfhibk
    # key = 13

    key = 13
    words = message.split()
    
    ciphered_message = ""

    for word in words:
      for character in word:
        if(character >= 'A' and character <= 'Z'):
          character_cipher = (((ord(character) - (ord('A') + 26)) + key) % 26) + ord('A')
          ciphered_message += chr(character_cipher)
        elif(character >= 'a' and character <= 'z'):
          character_cipher = (((ord(character) - (ord('a') + 26)) + key) % 26) + ord('a')
          ciphered_message += chr(character_cipher)
        else:
          ciphered_message += character
      ciphered_message += ' '

    ciphered_message = ciphered_message.rstrip()
    return ciphered_message
