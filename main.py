def encode(input_str):
    morse_code = {
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        ".": ".-.-.-",
        ",": "--..--",
        "?": "..--..",
        "!": "-.-.--",
        "-": "-....-",
        "/": "-..-.",
        "@": ".--.-.",
        "(": "-.--.",
        ")": "-.--.-"
    }

    morse_code_str = []
    for char in input_str.lower():
        if char in morse_code:
            morse_code_str.append(morse_code[char])
        elif char == ' ':
            morse_code_str.append('/')
        else:
            raise ValueError(f"Invalid character: {char}")
    return ' '.join(morse_code_str)


def decode(morse_code_str):
    morse_code = {
        "-----": "0",
        ".----": "1",
        "..---": "2",
        "...--": "3",
        "....-": "4",
        ".....": "5",
        "-....": "6",
        "--...": "7",
        "---..": "8",
        "----.": "9",
        ".-": "a",
        "-...": "b",
        "-.-.": "c",
        "-..": "d",
        ".": "e",
        "..-.": "f",
        "--.": "g",
        "....": "h",
        "..": "i",
        ".---": "j",
        "-.-": "k",
        ".-..": "l",
        "--": "m",
        "-.": "n",
        "---": "o",
        ".--.": "p",
        "--.-": "q",
        ".-.": "r",
        "...": "s",
        "-": "t",
        "..-": "u",
        "...-": "v",
        ".--": "w",
        "-..-": "x",
        "-.--": "y",
        "--..": "z",
        ".-.-.-": ".",
        "--..--": ",",
        "..--..": "?",
        "-.-.--": "!",
        "-....-": "-",
        "-..-.": "/",
        ".--.-.": "@",
        "-.--.": "(",
        "-.--.-": ")"
    }

    text_str = []
    for code in morse_code_str.split():
        if code in morse_code:
            text_str.append(morse_code[code])
        elif code == '/':
            text_str.append(' ')
        else:
            raise ValueError(f"Invalid code: {code}")
    return ''.join(text_str)


choice = input("Decode or encode: ")
if choice == "decode":
    word = input("Enter a morse code: ")
    print(decode(word))
else: 
    word = input("Enter a word: ")
    print(encode(word))
