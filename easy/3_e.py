# Challenge 3, easy
# https://www.reddit.com/r/dailyprogrammer/comments/pkw2m/2112012_challenge_3_easy/

def caesar_shift(input_text, shift):
    text_list = list(input_text)                    # make into list
    print(f"OLD TEXT: {text}")

    for i in range(len(text_list)):
        if text_list[i].isupper():
            if ord(text_list[i]) + int(shift) > ord('Z'):
                text_list[i] = chr(ord(text_list[i]) + int(shift) - 26)
            elif ord(text_list[i]) + int(shift) < ord('A'):
                text_list[i] = chr(ord(text_list[i]) + int(shift) + 26)
            else:
                text_list[i] = chr(ord(text_list[i]) + int(shift))
        if text_list[i].islower():
            if ord(text_list[i]) + int(shift) > ord('z'):
                text_list[i] = chr(ord(text_list[i]) + int(shift) - 26)
            elif ord(text_list[i]) + int(shift) < ord('a'):
                text_list[i] = chr(ord(text_list[i]) + int(shift) + 26)
            else:
                text_list[i] = chr(ord(text_list[i]) + int(shift))

    new_text = "".join(text_list)
    print("TRANSLATED: ", new_text)

caesar_shift(text, 19)
