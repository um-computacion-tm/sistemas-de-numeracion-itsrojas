import unittest

def decimal2octal(numero):
    octal = 0
    while numero > 0:
        resto = numero % 8
        octal = str(octal) + str(resto)
        numero = numero / 8
    octal = int(str(octal)[::-1])
    return octal

def octal2decimal(numero):
    decimal = 0
    potencia = 0
    for i in numero:
        decimal += int(i) * (8 ** potencia)
        potencia += 1
    return decimal

def octal2hexadecimal(numero):
    hexadecimal = 0
    decimal = 0
    potencia = 0
    for i in numero:
        decimal += int(i) * (8 ** potencia)
        potencia += 1
    while decimal > 0:
        resto = decimal % 16
    if resto < 10:
        hexadecimal = str(resto) + hexadecimal
    else:
        hexadecimal = chr(resto - 10 + ord('A')) + hexadecimal
        decimal //= 16
    return hexadecimal

def octal2binario(numero):
    binario = ''
    for i in numero:
        conversor = bin(i)
        binario = str(binario) + str(conversor)
    return binario



if  __name__  == '__main__':
    unittest.main