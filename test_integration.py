import unittest
from consulta_cep import consulta_cep

class TestIntegrationCEP(unittest.TestCase):
    def test_integration_via_cep(self):
        # Teste de integração que verifica se a API ViaCEP está respondendo corretamente
        cep = "01001000"
        resultado = consulta_cep(cep)
        self.assertIsNotNone(resultado)
        self.assertIn('logradouro', resultado)
        self.assertIn('bairro', resultado)
        self.assertIn('localidade', resultado)
        self.assertIn('uf', resultado)

if __name__ == '__main__':
    unittest.main()
