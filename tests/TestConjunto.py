import unittest
from src.logic.Conjunto import Conjunto

class TestConjunto(unittest.TestCase):
    def test_conjunto_vacio_retornaNone(self):
        conjunto=Conjunto([])
        self.assertIsNone(conjunto.promedio())

    def test_conjunto_unElemento_retornaValorUnicoElemento(self):
        conjunto = Conjunto([5])
        self.assertEqual(5,conjunto.promedio())
    def test_conjunto_dosElementos_retornaPromedioElementos(self):
        conjunto = Conjunto([5,7])
        self.assertEqual(6,conjunto.promedio())

    def test_conjunto_nElementos_retornaValorPromedioNElementos(self):
        conjunto = Conjunto([2,4,8,10,15])
        self.assertEqual((2+4+8+10+15)/5,conjunto.promedio())