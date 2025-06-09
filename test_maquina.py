import unittest
from maquina_expendedora_ICS import MaquinaExpendedora


class TestMaquinaExpendedora(unittest.TestCase):
    def setUp(self):
        self.maquina = MaquinaExpendedora([
            [24, 7, 6, 7, 5, 2, 4], # Galletitas $24
            [15, 1, 5, 2, 7, 4, 2], # Alfajor $15
            [8, 6, 1, 2, 3, 5, 3], # Chicle $8
            [37, 4, 3, 7, 4, 5, 1], # Chips $37
            [45, 7, 6, 1, 3, 2, 5] # Coca-cola $45
        ])
        self.maquina.total_ingresado = 50

    def test_ingresa_mas_billetes(self):
        self.assertFalse(self.maquina.comprueba_billetes([1, 3, 2, 0])) # Devuelve falso por exceso de billetes 
        self.assertFalse(self.maquina.comprueba_billetes([0, 1, 4, 2])) # Devuelve falso por exceso de billetes
        self.assertFalse(self.maquina.comprueba_billetes([4, 1, 0, 3])) # Devuelve falso por exceso de billetes
        self.assertFalse(self.maquina.comprueba_billetes([5, 3, 0, 0])) # Devuelve falso por exceso de billetes
        self.assertFalse(self.maquina.comprueba_billetes([8, 0, 1, 0])) # Devuelve falso por exceso de billetes

    def test_ingresa_menos_billetes(self):
        self.assertTrue(self.maquina.comprueba_billetes([0, 0, 3, 0])) # Devuelve verdadero a la cantidad de billetes
        self.assertTrue(self.maquina.comprueba_billetes([1, 2, 0, 1])) # Devuelve verdadero a la cantidad de billetes
        self.assertTrue(self.maquina.comprueba_billetes([0, 0, 1, 0])) # Devuelve verdadero a la cantidad de billetes
        self.assertTrue(self.maquina.comprueba_billetes([1, 1, 1, 1])) # Devuelve verdadero a la cantidad de billetes
        self.assertTrue(self.maquina.comprueba_billetes([1, 1, 1, 2])) # Devuelve verdadero a la cantidad de billetes

    def test_devuelve_vuelto(self):
        self.assertEqual(self.maquina._MaquinaExpendedora__devuelve_vuelto(18), [1,1,1,1]) # Vuelto de $18 en 1 billete de cada tipo
        self.assertEqual(self.maquina._MaquinaExpendedora__devuelve_vuelto(14), [0,2,0,1]) # Vuelto de $14 en dos de $2 y uno de $10

    def test_recarga_existencias(self):
        self.assertEqual(self.maquina.recarga_existencias(20, 3), 'Artículos recargados. cantidad sobrante: 2.')
        self.assertEqual(self.maquina.recarga_existencias(15, 1), 'Artículos recargados. cantidad sobrante: 0.')

if __name__ == '__main__':
    unittest.main()