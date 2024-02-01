import os

MORSE_DICT={
    "a":"•⁃",
    "b":"⁃•••",
    "c":"⁃•⁃•",
    "d":"⁃••",
    "e":"•",
    "f":"••⁃•",
    "g":"⁃⁃•",
    "h":"••••",
    "i":"••",
    "j":"•⁃⁃⁃",
    "k":"⁃•⁃",
    "l":"•⁃••",
    "m":"⁃⁃",
    "n":"⁃•",
    "o":"⁃⁃⁃",
    "p":"•⁃⁃•",
    "q":"⁃⁃•⁃",
    "r":"•⁃•",
    "s":"•••",
    "t":"⁃",
    "u":"••⁃",
    "v":"•••⁃",
    "w":"•⁃⁃",
    "x":"⁃••⁃",
    "y":"⁃•⁃⁃",
    "z":"⁃⁃••",
    "1":"•⁃⁃⁃",
    "2":"••⁃⁃",
    "3":"•••⁃",
    "4":"••••⁃",
    "5":"••••",
    "6":"⁃••••",
    "7":"⁃⁃•••",
    "8":"⁃⁃⁃••",
    "9":"⁃⁃⁃⁃•",
    "0":"⁃⁃⁃⁃⁃",
    "å":".⁃•.⁃",
    "æ":"•⁃•⁃",
    "ø":"⁃⁃⁃•",
    " ":"  ",
}

def take_input():
    return input("What text would you like to morsify?\n")

def look_up_morse(letter):
    try:
        return MORSE_DICT[letter]
    except:
        return letter

def main():
    os.system('clear')
    text=take_input()
    morse_encoded=""
    for _ in text:
        morse=look_up_morse(_.lower())
        morse_encoded += " " + morse
    print (morse_encoded)
    

if __name__ == "__main__":
    main()