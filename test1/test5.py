# generate 10 to 32 character password list using hex numbers, 0-9 A-F
x = range(17592186044415 , 295147905179352830000)
def gen_pwd():
    x = range(17592186044415 , 295147905179352830000)

    def toHex(dec):
        x = (dec % 16)
        digits = "0123456789ABCDEF"
        rest = dec / 16
        if (rest == 0):
            return digits[x]
        return toHex(rest) + digits[x]

    for x in range(x):
        print
        toHex(x)
    f = open("sdnlnk_pwd.txt")
    print(f)
    value = x
    string = str(value)
    f.write(string)


gen_pwd()
