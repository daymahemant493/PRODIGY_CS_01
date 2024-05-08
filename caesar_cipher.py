def encrypt(text,s):
    result =""
    
    for i in range(len(text)):
        char =text[i]
        if(char.isupper()):
            result += chr((ord(char) + s-65)% 26 +65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result

def decrypt(text,s):
    result = ""
    
    for i in range(len(text)):
        char =text[i]
        if(char.isupper()):
            result += chr((ord(char) - s-65)% 26 +65)
        else:
            result += chr((ord(char) - s-97)% 26 +97)
    return result
    
text= input("Enter Message: ")
s=int(input("Enter shift value: "))
print("text: " + text)
print("Shift: " + str(s))
enycrpt_text =encrypt(text,s)
print("Cipher Text: " + enycrpt_text)
print("Decrypted Text: " + decrypt(enycrpt_text,s))

