import unittest

from conversion_num_binario import binario2decimal, binario2hexadecimal, decimal2binario
from conversion_num_octales import decimal2octal, octal2binario, octal2decimal, octal2hexadecimal
from conversion_num_hexadecimal import decimal2hexa, hexa2binario, hexa2decimal, hexa2octal



class Binario2DecimalTestCase(unittest.TestCase):
    def test_uno(self):
        resultado = binario2decimal('1010')
        self.assertEqual(resultado, 10)

class TestDecimal2Binario(unittest.TestCase):
    def test_dos(self):
        resultado = decimal2binario(9)
        self.assertEqual(resultado, '1001')

class TestBinario2Hexadecimal(unittest.TestCase):
    def test_tres(self):
        resultado = binario2hexadecimal(101)
        self.assertEqual(resultado, 5)

class TestDecimal2Octal(unittest.TestCase):
    def test_cuatro(self):
        resultado = decimal2octal(20)
        self.assertEqual(resultado, 24)

class TestOctal2Binario(unittest.TestCase):
    def test_cinco(self):
        resultado = octal2binario(11)
        self.assertEqual(resultado, '1001')
    
class TestOctal2Hexadecimal(unittest.TestCase):
    def test_seis(self):
        resultado = octal2hexadecimal(17)
        self.assertEqual(resultado, 'F')

class TestDecimal2Hexadecimal(unittest.TestCase):
    def test_siete(self):
        resultado = decimal2hexa(59)
        self.assertEqual(resultado, '3B')

class TestHexadecimal2Binario(unittest.TestCase):
    def test_ocho(self):
        resultado = hexa2binario('4A')
        self.assertEqual(resultado, '01001010')

class TestHexadecimal2Octal(unittest.TestCase):
    def test_nueve(self):
        resultado = hexa2octal('38')
        self.assertEqual(resultado, 70)



if __name__ == '__main__':
    unittest.main()