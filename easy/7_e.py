# Challenge 7, easy
# https://www.reddit.com/r/dailyprogrammer/comments/pr2xr/2152012_challenge_7_easy/

# morse code translator

input_text = '.... . .-.. .-.. --- / -.. .- .. .-.. -.-- / .--. .-. --- --. .-. .- -- -- . .-. / --. --- --- -.. / .-.. ..- -.-. -.- / --- -. / - .... . / -.-. .... .- .-.. .-.. . -. --. . ... / - --- -.. .- -.--'

# create morse code dictionary
text_to_morse_dict = {
'A': '.-',
'B': '-...',
'C': '-.-.',
'D': '-..',
'E': '.',
'F': '..-.',
'G': '--.',
'H': '....',
'I': '..',
'J': '.---',
'K': '-.-',
'L': '.-..',
'M': '--',
'N': '-.',
'O': '---',
'P': '.--.',
'Q': '--.-',
'R': '.-.',
'S': '...',
'T': '-',
'U': '..-',
'V': '...-',
'W': '.--',
'X': '-..-',
'Y': '-.--',
'Z': '--..',
'1': '.----',
'2': '..---',
'3': '...--',
'4': '....-',
'5': '.....',
'6': '-....',
'7': '--...',
'8': '---..',
'9': '----.',
'0': '-----'}

morse_to_text_dict = {value: key for key, value in text_to_morse_dict.items()}

def morse_to_text(input_text):
    morse_list = input_text.split(' ')
    translated = []

    for word in morse_list:
        if word == '/':
            translated.append(' ')
        else:
            translated.append(morse_to_text_dict[word])

    print(''.join(translated))

morse_to_text(input_text)

# bonus: translate string to morse
