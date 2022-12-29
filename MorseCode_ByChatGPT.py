def encode_morse(text):
  # Create a dictionary with the Morse code translations
  morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', ':': '---...',
    '?': '..--..', '\'': '.----.', '-': '-....-', '/': '-..-.', '(': '-.--.',
    ')': '-.--.-', '"': '.-..-.', '@': '.--.-.'
  }
  
  # Initialize an empty string to store the Morse code translation
  morse = ''
  
  # Iterate through each character in the text and look up its Morse code translation
  for char in text.upper():
    morse += morse_code[char] + ' '
  
  return morse

def decode_morse(morse):
  # Create a dictionary with the Morse code translations
  morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', ':': '---...',
    '?': '..--..', '\'': '.----.', '-': '-....-', '/': '-..-.', '(': '-.--.',
    ')': '-.--.-', '"': '.-..-.', '@': '.--.-.'
  }
  
  # Create a reverse lookup dictionary to decode the Morse code
  morse_code_rev = {v: k for k, v in morse_code.items()}
  
  # Split the Morse code into individual code elements and remove any whitespace
  morse = morse.strip().split(' ')
  
  # Initialize an empty string to store the decoded text
  text = ''
  
  # Iterate through each code element and look up its text translation
  for code in morse:
    # If the code element is not in the dictionary, skip it
    if code not in morse_code_rev:
      continue
    text += morse_code_rev[code]
  
  return text

# Main function
def main():
  # Prompt the user to choose between encoding and decoding
  choice = input('Enter 1 to encode or 2 to decode: ')
  
  # If the user chose to encode
  if choice == '1':
    # Get the text to encode from the user
    text = input('Enter the text to encode: ')
    # Encode the text and print the result
    print(encode_morse(text))
  # If the user chose to decode
  elif choice == '2':
    # Get the Morse code to decode from the user
    morse = input('Enter the Morse code to decode: ')
    # Decode the Morse code and print the result
    print(decode_morse(morse))
  # If the user entered an invalid choice
  else:
    print('Invalid choice')
    
# Run the main function
main()
