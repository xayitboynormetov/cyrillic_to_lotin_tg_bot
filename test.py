# import transliterate
from transliterate import to_cyrillic, to_latin
# print(to_cyrillic("Assalomu alaykum"))
# print(to_latin("лотинча"))
s = input()
if s.isascii():
    print(to_cyrillic(s))

else:
    print(to_latin)