cryptedDataFile = open("crypted_data.crypthis", "r")
toDecrypt = cryptedDataFile.read()
cryptedDataFile.close()
passwd = input('Password: ')
def toBinary(str):
    bina = ' '.join(format(ord(x), 'b') for x in str)
    return bina.replace(' ', '')

decrypted = int(toDecrypt) - int(toBinary(passwd))
# print(int(decrypted))

def toDecimal(binary):
    decimal, i = 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return (decimal)

str_data = ''
for i in range(0, len(str(decrypted)), 7):
    temp_data = int(str(decrypted)[i:i + 7])
    decimal_data = toDecimal(temp_data)
    str_data = str_data + chr(decimal_data)

str_data = str_data.replace('__space__', ' ')
toWriteDecryptedFile = open("decrypted_data.txt", "a")
toWriteDecryptedFile.write(str_data)
toWriteDecryptedFile.close()
print("Decrypted Text: " + str_data)