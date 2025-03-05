import time

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', 
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', 
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', 
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', 
    ' ': '/'
}
MORSE_CODE_DICT_REV = {value: key for key, value in MORSE_CODE_DICT.items()}

def text_to_morse(text):
    return ' '.join(MORSE_CODE_DICT.get(char.upper(), '?') for char in text)

def morse_to_text(morse_code):
    return ''.join(MORSE_CODE_DICT_REV.get(code, '?') for code in morse_code.split(' '))

def main():
    print("Choose what you want to do: ")
    print("1. From English to morse.")
    print("2. From morse to English.")
    
    x = int(input(""))
    a = input("Input your message: ")
    
    if x == 1:
        print(text_to_morse(a))
    elif x == 2:
        print(morse_to_text(a))
        
    print("Do you want to save your message? (y/n)")
    b = input("")
    
    if b == "y":
        name = f"morse_message_{time.strftime('%Y-%m-%d_%H-%M-%S')}.txt"
        f = open(name, "w")
        f.write(text_to_morse(a))
        f.close()
        print(f"Message saved to {name}")
        time.sleep(3)
        return
    return

if __name__ == "__main__":
    main()
