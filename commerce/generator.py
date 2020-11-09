import random, base64

"""secret = input("Enter the passphrase:")
"""
passes = ["DPS{1tz_R3D}", "DPS{Wh1T3_SuS}", "DPS{P1nk_V3nTed}", "DPS{1Tz_Gr3eN}", "DPS{Blu3_SuS}", "DPS{y3LL0W}", "DPS{N0T_BlaCk}", "DPS{Br0Wn_V3nTed}", "DPS{CyAN_SUs}", "DPS{0RanG3}"]

def generate(count):
    secret = passes[count] 
    indent = 0
    word = list(secret)
    random.shuffle(word)
    code=""
    for i in word:
            indents = "  " * indent
            code += indents + f"if secret[{secret.index(i)}] == '{i}':"
            code+='\n'
            indent += 1
    code+="  " * indent
    code+="print('Nice you got the password now just go to https://itcouncil.herokuapp.com/techsprint/treasurehunt_challenge/challenge and give the password. We will announce the results 30 mins after the event ends')"
    return base64.b32encode(code.encode('ascii')).decode('ascii')