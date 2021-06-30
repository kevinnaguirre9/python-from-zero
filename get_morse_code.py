
def get_morse_code():  
    word = input("Please, enter a word: ")

    morse_code = {
        "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", 
        "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": "·---", "k": "-.-", 
        "l": ".-..", "m": "--", "n": "-.", "ñ": "--.--", "o": "---", "p": ".__.", 
        "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", 
        "w": ".--", "x": "-..-", "y": "-.--", "z": "--..",    
        "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", 
        "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
        ".": ".-.-.-", ",": "-.-.--", "?": "..--..", "\"": ".-..-."
    }

    word_in_morse_code = ""

    for letter in word:
        if letter.lower() in morse_code:
            word_in_morse_code += morse_code.get(letter.lower())
    
    print("The word in morse code is: {}".format(word_in_morse_code))


get_morse_code()