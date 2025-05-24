import unittest
from maquina_expendedora_ICS import MaquinaExpendedora


class TestMaquinaExpendedora(unittest.TestCase):
    def setUp(self):
        self.__maquina = MaquinaExpendedora([
            [24, 1, 6, 7, 5, 2, 4], # Galletitas $24
            [15, 1, 5, 2, 7, 4, 2], # Alfajor $15
            [8, 6, 1, 2, 3, 5, 3], # Chicle $8
            [37, 4, 3, 7, 4, 5, 1], # Chips $37
            [45, 7, 6, 1, 3, 2, 5] # Coca-cola $45
        ])
        self.__maquina.total_ingresado = 50

    def test_devuelve_vuelto(self):
        self.assertEqual(self.__maquina.__devuelve_vuelto(18), [1,1,1,1])


if __name__ == '__main__':
    unittest.main()