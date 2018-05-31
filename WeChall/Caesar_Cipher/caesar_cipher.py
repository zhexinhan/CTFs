#!/usr/bin/python3.6

import string

input = "DRO AESMU LBYGX PYH TEWZC YFOB DRO VKJI NYQ YP MKOCKB KXN IYEB EXSAEO CYVEDSYX SC MLPMZNYWPQYL".lower()

for i in range(1, 27):
    result = ''
    for character in input:
        index = string.ascii_lowercase.find(character)
        if index >= 0:
            new_character_index = (index + i) % 26
            result += string.ascii_lowercase[new_character_index]
        else:
            result += ' '
    print(result)