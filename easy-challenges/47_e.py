# Challenge 47, easy
# https://www.reddit.com/r/dailyprogrammer/comments/t33vi/522012_challenge_47_easy/

# REUSED FROM CHALLENGE #3

text = '''
Spzalu - zayhunl dvtlu sfpun pu wvukz kpzaypibapun zdvykz pz uv ihzpz mvy h
zfzalt vm nvclyutlua.  Zbwyltl leljbapcl wvdly klypclz myvt h thukhal myvt aol
thzzlz, uva myvt zvtl mhyjpjhs hxbhapj jlyltvuf. Fvb jhu'a lewlja av dplsk
zbwyltl leljbapcl wvdly qbza 'jhbzl zvtl dhalyf ahya aoyld h zdvyk ha fvb! P
tlhu, pm P dlua hyvbuk zhfpu' P dhz hu ltwlylyvy qbza iljhbzl zvtl tvpzalulk
ipua ohk sviilk h zjptpahy ha tl aolf'k wba tl hdhf!... Ho, huk uvd dl zll aol
cpvslujl puolylua pu aol zfzalt! Jvtl zll aol cpvslujl puolylua pu aol zfzalt!
Olsw! Olsw! P't ilpun ylwylzzlk!
'''

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
