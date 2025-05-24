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
        self.assertFalse(self.maquina.comprueba_billetes([1, 3, 2, 0]))
        self.assertFalse(self.maquina.comprueba_billetes([0, 1, 4, 2]))
        self.assertFalse(self.maquina.comprueba_billetes([4, 1, 0, 3]))
        self.assertFalse(self.maquina.comprueba_billetes([5, 3, 0, 0]))
        self.assertFalse(self.maquina.comprueba_billetes([8, 0, 1, 0]))

    def test_ingresa_menos_billetes(self):
        self.assertTrue(self.maquina.comprueba_billetes([0, 0, 3, 0]))
        self.assertTrue(self.maquina.comprueba_billetes([1, 2, 0, 1]))
        self.assertTrue(self.maquina.comprueba_billetes([0, 0, 1, 0]))
        self.assertTrue(self.maquina.comprueba_billetes([1, 1, 1, 1]))
        self.assertTrue(self.maquina.comprueba_billetes([1, 1, 1, 2]))

    def test_devuelve_vuelto(self):
        self.assertEqual(self.maquina._MaquinaExpendedora__devuelve_vuelto(18), [1,1,1,1])
        self.assertEqual(self.maquina._MaquinaExpendedora__devuelve_vuelto(14), [0,2,0,1])

    # def test_recarga_existencias(self):
    #     self.assertEqual(self.maquina.recarga_existencias(20, 3), 'Artículos recargados. cantidad sobrante: 0.')
    #     self.assertEqual(self.maquina.recarga_existencias(15, 1), 'Artículos recargados. cantidad sobrante: 4.')

if __name__ == '__main__':
    unittest.main()