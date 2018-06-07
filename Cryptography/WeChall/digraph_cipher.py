#!/usr/bin/python3.6

import math

input = "qtigazcektdrxfaynfdrxfkgigazjaid thigay hpctofktzxznxfcthp xfebkgja bfctjajadrcect jaayofofctjajajwaynfnfzxid eadrja azigxf xfigig hpkgjwjwkgofaynfxf ctkgxfebctktao ewdrja kgxfzt eactnfnfao ceigighp pwigkiid ljazxfctkt xfebkgja rmctzxewigkthp drja jaignfayxfkgigazbd ofkgnfnfofigigebigjahpigid"

digraph_map = {
    'ja': 's',
    'ig': 'o',
    'nf': 'l',
    'ay': 'u',
    'xf': 't',
    'kg': 'i',
    'az': 'n',
    'bd': ':',
    'th': 'Y',
    'eb': 'h',
    'qt': 'C',
    'ce': 'g',
    'kt': 'r',
    'dr': 'a',
    'id': '.',
    'hp': 'd',
    'pw': 'j',
    'ki': 'b',
    'ct': 'e',
    'of': 'c',
    'bf': 'm',
    'zx': 'y',
    'zn': 'p',
    'jw': 'f',
    'ea': 'W',
    'ao': ',',
    'zt': '?',
    'ew': 'w',
    'lj': 'E',
    'rm': 'k'
}

result = ''
index = 0
while index < len(input):
    if ' ' == input[index]:
        result += ' '
        index += 1
    else:
        character = input[index : index + 2]
        result += digraph_map.get(character, character)
        index += 2

print(result)
