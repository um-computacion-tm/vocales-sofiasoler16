import unittest

from contar import contar_vocales
        
class TestContarVocales(unittest.TestCase):
    def test_sin_vocales(self):
        palabra = "tryhgf"
        resultado = contar_vocales(palabra)
        self.assertEqual(resultado, {})

    def test_con_vocal_o(self):
        palabra = "sol"
        resultado = contar_vocales(palabra)
        self.assertEqual(resultado, {"o": 1})

    def test_con_vocal_doble_o(self):
        palabra = "solo"
        resultado = contar_vocales(palabra)
        self.assertEqual(resultado, {"o": 2})

    def test_con_dos_vocales(self):
        palabra = "sola"
        resultado = contar_vocales(palabra)
        self.assertEqual(resultado, {"o": 1, "a": 1})

    def test_con_todas_las_vocales(self):
        palabra = "solamente quiero que gane Boca"
        resultado = contar_vocales(palabra)
        self.assertEqual(
            resultado,
            {"a": 3, "e": 5, "i": 1, "o": 3, "u": 2},
        )

    def test_con_vocales_en_mayuscula(self):
        palabra = "SOlAmente quIerO"
        resultado = contar_vocales(palabra)
        self.assertEqual(
            resultado,
            {"a": 1, "e": 3, "i": 1, "o": 2, "u": 1},
        )

    def test_contar(self):
        palabra = "solamente quiero que gane Boca"

        resultado = contar_vocales(palabra)
        self.assertEqual(resultado, 
                         {"a":3, "e":5, "i":1, "o":3, "u":2})
        
if __name__ == '__main__':
    unittest.main()