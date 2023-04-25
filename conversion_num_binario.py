import unittest

def binario2decimal(numbers):
    decimal = 0
    for i in numbers:
        decimal = decimal * 2 + int(i)
    return decimal

def decimal2binario(numbers):
    binario = ''
    while numbers > 1:
        resto = numbers % 2
        numbers = numbers // 2
        binario = str(resto) + binario
    return binario

def binario2hexadecimal(numbers):
    decimal = 0
    potencia = len(numbers) - 1
    hexadecimal = ""
    for i in len(numbers):
        decimal = decimal*2 + int(i)
    while decimal > 0:
        resto = decimal % 16
    if resto < 10:
        hexadecimal = str(resto) + hexadecimal
    else:
        hexadecimal = chr(resto - 10 + ord('A')) + hexadecimal
        decimal //= 16
    return hexadecimal

def binario2octales(numbers):
    decimal = 0
    octal = 0
    for i in len(numbers):
        decimal = decimal*2 + int(i)
    while decimal > 0:
        resto = decimal % 8
        decimal = decimal // 8
        octal = str(resto) + str(octal)
    octal = int(str(octal)[::-1])
    return octal



if __name__ == '__main__':
    unittest.main()