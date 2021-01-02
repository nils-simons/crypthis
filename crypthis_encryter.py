from fractions import Fraction
toCrypt = input('Data to Encrypt: ')
toCrypt = toCrypt.replace(' ', '__space__')
passwd = input('Password: ')
def toBinary(str):
    bina = ' '.join(format(ord(x), 'b') for x in str)
    return bina.replace(' ', '')
print("Text: " + toBinary(toCrypt))
print("Passwd: " + toBinary(passwd))
crypted = int(toBinary(toCrypt))*int(toBinary(passwd))
toWriteCryptedFile = open("crypted_data.crypthis", "w")
toWriteCryptedFile.write(str(crypted))
toWriteCryptedFile.close()
print(int(crypted))