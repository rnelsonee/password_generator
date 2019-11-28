# password_generator.py
# A small program to create cyrptographically-suitable random
# passwords on your local machine.

import secrets

# Set lengths of passwords desired here
lengths = [16, 32]

# I chose three sets, but these are mutable. A description followed by the character set
# which will serve as the available characters.
sets =  [
        ["alphanumerics", 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'],
        ["non-conflating characters", 'acdefghjkmnpqrtuvwxyzACDEFGHJKMNPQRTUVWXYZ234679#$%&()+;<=>?@[]~'],
        ["alphanumerics and symbols", 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~']
        ]   

for length in lengths:
    for item in sets:
        # Mmm, code golf. 
        # Note you can bring that last 'for i in range(length)' out. And use output += ouput + item[1]...
        # instead of ''.join[....]
        password = ''.join([item[1][secrets.randbelow(len(item[1]))] for i in range(length)])
        print(password + " "*(max(lengths)-length) + f"  <= A {length}-char using {item[0]}")
