import os
import pyaes

## Abrir arquivo criptografado 

file_name = 'teste.txt.assinatura'
file = open(file_name,'rb')
file_data = file.read()
file.close()

## chave descriptografia

key =b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## Remover o arquivo antigo
os.remove(file_name)

## Criar o arquivo sem criptografia

new_file = 'teste.txt'
new_file = open(f'{new_file}', 'wb')
new_file.write(decrypt_data)
new_file.close()
