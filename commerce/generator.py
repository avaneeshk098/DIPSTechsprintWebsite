import random

head_code = \
"""secret = input("Enter the passphrase:")
"""

passes = ["DPS{1tz_R3D}", "DPS{Wh1T3_SuS}", "DPS{P1nk_V3nTed}", "DPS{1Tz_Gr3eN}", "DPS{Blu3_SuS}", "DPS{y3LL0W}", "DPS{N0T_BlaCk}", "DPS{Br0Wn_V3nTed}", "DPS{CyAN_SUs}", "DPS{0RanG3}"]

def generate(count):
    secret = passes[count%10] 
    with open("staticfiles/code.txt", "w") as fp:
        fp.write(head_code)
    indent = 0
    word = list(secret)
    random.shuffle(word)
    with open("staticfiles/code.txt", "a") as fp:
        for i in word:
            indents = "  " * indent
            fp.write(indents + f"if secret[{secret.index(i)}] == '{i}':")
            fp.write('\n')
            indent += 1

generate(9)