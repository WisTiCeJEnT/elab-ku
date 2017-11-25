#=========== answer =================
def decrypt(msg):
    return "".join(list(msg.replace('G','d').replace('D','o').replace('O','g').upper())[::-1])
"""
#for debuging
    msg = msg.replace('G','d')
    msg = msg.replace('D','o')
    msg = msg.replace('O','g')
    msg = msg.upper()
    msg = list(msg)
    msg.reverse()
    msg = "".join(msg)
    return msg
"""
#====================================
def encrypt(msg):
    secret = []
    for c in msg:
        if c == "G":
            secret.append("O")
        elif c == "O":
            secret.append("D")
        elif c == "D":
            secret.append("G")
        else:
            secret.append(c)

    secret.reverse()

    return "".join(secret)
