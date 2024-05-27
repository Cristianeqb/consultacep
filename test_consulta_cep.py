import unittest
from consulta_cep import consulta_cep

class TestConsultaCEP(unittest.TestCase):
    def test_cep_valido(self):
        cep = "01001000"
        resultado = consulta_cep(cep)
        self.assertIsNotNone(resultado)
        self.assertIn('logradouro', resultado)
        self.assertIn('bairro', resultado)
        self.assertIn('localidade', resultado)
        self.assertIn('uf', resultado)

    def test_cep_invalido(self):
        cep = "00000000"
        resultado = consulta_cep(cep)
        self.assertIsNone(resultado)

if __name__ == '__main__':
        unittest.main()
