def crypted(sentence):
    translation=""
    for element in sentence:
        if element in "Aa":
            translation=translation + "1"
        elif element in "Bb":
            translation=translation + "2"
        elif element in "Cc":
            translation=translation + "3"
        elif element in "Dd":
            translation = translation + "4"
        elif element in "Ee":
            translation = translation + "5"
        elif element in "Ff":
            translation = translation + "6"
        elif element in "Gg":
            translation = translation + "7"
        elif element in "Hh":
            translation = translation + "8"
        elif element in "Ii":
            translation = translation + "9"
        elif element in "Jj":
            translation = translation + "!"
        elif element in "Kk":
            translation = translation + "@"
        elif element in "Ll":
            translation = translation + "#"
        elif element in "Mm":
            translation = translation + "$"
        elif element in "Nn":
            translation = translation + "%"
        elif element in "Oo":
            translation = translation + "^"
        elif element in "Pp":
            translation = translation + "&"
        elif element in "Qq":
            translation = translation + "*"
        elif element in "Rr":
            translation = translation + "("
        elif element in "Ss":
            translation = translation + ")"
        elif element in "Tt":
            translation = translation + "-"
        elif element in "Uu":
            translation = translation + "_"
        elif element in "Vv":
            translation = translation + "+"
        elif element in "Ww":
            translation = translation + "="
        elif element in "Xx":
            translation = translation + "~"
        elif element in "Yy":
            translation = translation + "}"
        elif element in "Zz":
            translation = translation + "{"
        else:
            translation=translation+ element

    return translation

print(crypted(input("What do you want to crypt: ")))