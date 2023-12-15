
def decrypt_arabic_caesar(ciphertext , key):

  # Define a dictionary mapping Arabic letters to their position in the alphabet.
  arabic_alphabet = {
    "ء":1,
    "آ":2,
    "أ":3,
    "ؤ":4,
    "إ":5,
    "ئ":6,
    "ا":7,
    "ب":8,
    "ة":9,
    "ت":10,
    "ث":11,
    "ج":12,
    "ح":13,
    "خ":14,
    "د":15,
    "ذ":16,
    "ر":17,
    "ز":18,
    "س":19,
    "ش":20,
    "ص":21,
    "ض":22,
    "ط":23,
    "ظ":24,
    "ع":25,
    "غ":26,
    "ف":27,
    "ق":28,
    "ك":29,
    "ل":30,
    "م":31,
    "ن":32,
    "ه":33,
    "و":34,
    "ى":35,
    "ي":36,    
  }
 
  # Initialize empty string for decrypted text
  decrypted_text = ""
  print(key)
  # Loop through each character in the ciphertext
  for char in ciphertext:
    # Check if character is an Arabic letter
    if char in arabic_alphabet:
      # Get the current position of the letter in the alphabet
      current_position = arabic_alphabet[char]
 
      # Decrypt the letter by shifting it back 3 positions
      decrypted_position = (current_position - key) 
      if decrypted_position <= 0:
        decrypted_position += 36
      elif decrypted_position > 36:
          decrypted_position -= 36
 
      # Get the decrypted letter from the dictionary
      decrypted_letter = list(arabic_alphabet.keys())[list(arabic_alphabet.values()).index(decrypted_position)]
    else:
      # If not an Arabic letter, simply copy it to the decrypted text
      decrypted_letter = char
 
    # Add the decrypted letter to the decrypted text
    decrypted_text = decrypted_text + decrypted_letter 
 
  return decrypted_text
 

print("enter the ciphertext:")
ciphertext = input()

print("enter the shift key ( enter -1 to do brute force for all 36 shifts):")
key = int(input())

# the key -1 will do a brute force and any other key will be taken simply as a normal key.
if key == -1 :
  for i in range(35):
    decrypted_text = decrypt_arabic_caesar(ciphertext , i)
    print(decrypted_text)
else :
    decrypted_text = decrypt_arabic_caesar(ciphertext , key)
    print(decrypted_text)
