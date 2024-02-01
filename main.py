""" Portofolio project #1 from 100 Days of Code Course on Udemy,Section 82 """

#TODO: new-feature: add choice to encode vs decode text and demorsify a morsecode to regular text
#TODO: new-feature: maybe add turtle function to "draw the morse code"

#Dictionary for Morse codes for alpenum characters including Norwegian æ,ø,å
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


#function for taking input from user
"""take funtion from user, i prefer to practise calling functions in my coding now,
this could easily be done within main function as well """
def take_input():
    return input("What text would you like to morsify?\n")

#Function to look up letter in dictionary, should return correct Morse encoding, if no match return the letter/char i.e !
def look_up_morse(letter: str) -> str:
    try:
        return MORSE_DICT[letter]
    except:
        return letter

#main function
def main():
    text=take_input()
    morse_encoded=""
    for _ in text:
        morse=look_up_morse(_.lower())
        morse_encoded += " " + morse
    print (morse_encoded)
    

if __name__ == "__main__":
    main()