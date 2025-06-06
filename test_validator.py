import unittest
from validator import is_valid_address

class TestValidator(unittest.TestCase):
    def test_valid_address(self):
        print("Probando dirección válida...")  # <-- Este mensaje aparecerá en consola Jenkins
        self.assertTrue(is_valid_address("Av. Siempre Viva 742"))

    def test_missing_number(self):
        print("Probando dirección sin número...")
        self.assertFalse(is_valid_address("Av. Siempre Viva"))

    def test_empty_string(self):
        print("Probando cadena vacía...")
        self.assertFalse(is_valid_address(""))

    def test_not_a_string(self):
        print("Probando entrada no string...")
        self.assertFalse(is_valid_address(12345))

if __name__ == "__main__":
    print("Iniciando tests de dirección...")  # <-- Mensaje al inicio
    unittest.main()
