# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def encrypt(text):
    newstr = ""
    for i in range(len(text)):
        if (ord(text[i]) < 87):
            newstr += chr(ord(text[i]) + 4)
        else: 
            newstr += chr(ord(text[i]) - 22)
    return newstr

print(encrypt("PINEAPPLE"))
print(encrypt("ZEBRA"))
print(encrypt("NETWORK"))

