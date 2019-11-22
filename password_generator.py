import secrets

ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
printable = ascii_letters + '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
non_conflating = 'acdefghjkmnpqrtuvwxyzACDEFGHJKMNPQRTUVWXYZ234679#$%&()+;<=>?@[]~'

print("")
lenghts = [16, 32]

for length in lenghts:
    i = 0
    output = ''
    while i < length:
        i += 1
        output = output + printable[secrets.randbelow(len(printable))]
    print(output + " "*(32-length) + f"  <= A {length}-char using all")

    i = 0
    output = ''
    while i < length:
        i += 1
        output = output + ascii_letters[secrets.randbelow(len(ascii_letters))]
    print(output + " "*(32-length) + f"  <= A {length}-char using only alphanumeric")
    
    i = 0
    output = ''
    while i < length:
        i += 1
        output = output + non_conflating[secrets.randbelow(len(non_conflating))]
    print(output + " "*(32-length) + f"  <= A {length}-char using non-conflating")