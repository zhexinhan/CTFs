#!/usr/bin/python3.6

import base64
import string

input = """2B 53 53 48 20 4E 53 46 10 20 5D 53 59 20 57 53\
50 5A 49 48 20 53 52 49 20 51 53 56 49 20 47 4C\
45 50 50 49 52 4B 49 20 4D 52 20 5D 53 59 56 20\
4E 53 59 56 52 49 5D 12 20 38 4C 4D 57 20 53 52\
49 20 5B 45 57 20 4A 45 4D 56 50 5D 20 49 45 57\
5D 20 58 53 20 47 56 45 47 4F 12 20 3B 45 57 52\
0B 58 20 4D 58 23 20 15 16 1C 20 4F 49 5D 57 20\
4D 57 20 45 20 55 59 4D 58 49 20 57 51 45 50 50\
20 4F 49 5D 57 54 45 47 49 10 20 57 53 20 4D 58\
20 57 4C 53 59 50 48 52 0B 58 20 4C 45 5A 49 20\
58 45 4F 49 52 20 5D 53 59 20 58 53 53 20 50 53\
52 4B 20 58 53 20 48 49 47 56 5D 54 58 20 58 4C\
4D 57 20 51 49 57 57 45 4B 49 12 20 3B 49 50 50\
20 48 53 52 49 10 20 5D 53 59 56 20 57 53 50 59\
58 4D 53 52 20 4D 57 20 46 49 4A 49 4D 4D 4B 47\
46 52 56 45 12"""

message = base64.b16decode(input.replace(' ', '')).decode('utf-8')

for i in range(1, 128):
    should_print = True
    result = ''
    for character in message:
        index = ord(character)
        new_character = chr((index + i) % 128)
        if not new_character in string.printable:
            should_print = False
            break
        result += new_character

    if should_print:
        print(result)
