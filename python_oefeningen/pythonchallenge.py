#een

def een_letters_verplaatsen(text):
    nieuwe_string = ''
    alfabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter in text:
            if letter not in alfabet:
               nieuwe_string += letter
            else:
                letter_index = alfabet.index(letter)
                letter_index += 2
                
                if letter_index <= len(alfabet) -1:
                    nieuwe_letter = alfabet[letter_index]
                    nieuwe_string += nieuwe_letter
                elif letter_index == len(alfabet) + 1:
                    nieuwe_letter = 'b'
                    nieuwe_string += nieuwe_letter
                elif letter_index == len(alfabet):
                    nieuwe_letter = 'a'
                    nieuwe_string += nieuwe_letter
    print(nieuwe_string)

def een_letters_maketrans(text):
    table = text.maketrans(
        'abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab'
    )
    result = text.translate(table)
    print(result)

een_input = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

#een_letters_verplaatsen(een_input)
#een_letters_maketrans('map')

http://www.pythonchallenge.com/pc/def/ocr.html