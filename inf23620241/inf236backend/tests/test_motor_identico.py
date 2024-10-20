import unittest
import requests

class CreacionMotorMismoIDTest(unittest.TestCase):

    def setUp(self):
        # URL del endpoint de la API para crear motores
        self.url = 'http://localhost:8000/api/motor/create'
        
        # El mismo motor con el mismo número de serie (ID)
        self.motor_data = {
            'n_serie': 'MOTOR123',
            'operativo': True,
            'fecha_inicio': '2024-01-01',
            'tiempo_en_uso': 100,
            'durabilidad': 5000
        }

    def test_crear_motor_mismo_id(self):
        # Primer intento de crear el motor (debería ser exitoso)
        response1 = requests.post(self.url, json=self.motor_data)
        #print(response1.text)  # Agrega esta línea antes de `self.assertIn('n_serie', response2.json())`
        self.assertEqual(response1.status_code, 201)  # Verifica que el motor fue creado

        # Intentar crear otro motor con el mismo número de serie (debería fallar)
        response2 = requests.post(self.url, json=self.motor_data)
        #print(response2.text)  # Agrega esta línea antes de `self.assertIn('n_serie', response2.json())`
        self.assertEqual(response2.status_code, 401)  # Verifica que se rechaza por ID duplicado

        # Verificar que la respuesta contiene un mensaje de error
        self.assertIn('n_serie', response2.json())
        self.assertIn('already exists', response2.json()['n_serie'])

if __name__ == '__main__':
    unittest.main()