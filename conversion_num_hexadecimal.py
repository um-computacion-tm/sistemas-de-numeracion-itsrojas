import unittest

def decimal2hexa(numero):
    hexadecimal = 0
    terminos = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    while numero > 0:
        resto = numero % 16
        if resto >= 10:
             letra = terminos[resto]
             hexadecimal = letra + hexadecimal
        else:
            hexadecimal = str(resto) + hexadecimal
        numero = numero // 16
        hexadecimal = int(str(hexadecimal)[::-1])
    return hexadecimal

def hexa2decimal(numero):
    decimal = 0
    exponente = 0
    letras = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    for i in numero:
        if i in letras:
            decimal += letras[i] * 16 ** exponente
        else:
            decimal += int(i) * 16 ** exponente
        exponente -= 1
    return decimal

def hexa2binario(numero):
    decimal = 0
    exponente = 0
    binario = 0
    letras = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    for i in numero:
        if i in letras:
            decimal += letras[i] * 16 ** exponente
        else:
            decimal += int(i) * 16 ** exponente
        exponente -= 1
        while decimal > 1:
            resto = decimal % 2
            decimal = decimal / 2
            binario = str(resto) + binario
    return binario

def hexa2octal(numero):
    octal = 0
    decimal = 0
    exponente = 0
    letras = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    for i in numero:
        if i in letras:
            decimal += letras[i] * 16 ** exponente
        else:
            decimal += int(i) * 16 ** exponente
        exponente -= 1
    while numero > 0:
        resto = numero % 8
        octal = str(octal) + str(resto)
        numero = numero / 8
    octal = int(str(octal)[::-1])
    return octal



if  __name__  == '__main__':
    unittest.main