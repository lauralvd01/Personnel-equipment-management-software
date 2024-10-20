import unittest
import requests
from datetime import datetime, timedelta

class CreacionMotorFechaFuturaTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.url = 'http://localhost:8000/api/motor/create'
        cls.motor_data_anterior = {
            "n_serie": "12345",
            "operativo": True,
            "fecha_inicio": (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d'),  # Fecha anterior
            "tiempo_en_uso": 100,
            "durabilidad": 500
        }
        cls.motor_data_futuro = {
            "n_serie": "67890",
            "operativo": True,
            "fecha_inicio": (datetime.now() + timedelta(days=365)).strftime('%Y-%m-%d'),  # Fecha futura
            "tiempo_en_uso": 200,
            "durabilidad": 600
        }

    def test_crear_motor_fecha_anterior(self):
        # Intentar crear un motor con fecha anterior
        response = requests.post(self.url, json=self.motor_data_anterior)
        #print(f"Response: {response.text}")  # Depurar la respuesta

        # Verificar que al intentar crear un motor con fecha anterior se reciba un okay
        self.assertEqual(response.status_code, 201)
        '''try:
            data = response.json()
            self.assertIn('fecha_inicio', data)  # Verificar que el error menciona el campo fecha_inicio
        except requests.exceptions.JSONDecodeError:
            self.fail(f"Error al decodificar JSON: {response.text}")
        '''
    def test_crear_motor_fecha_futura(self):
        # Crear un motor con fecha futura
        response = requests.post(self.url, json=self.motor_data_futuro)
        #print(f"Response: {response.text}")  # Depurar la respuesta

        # Verificar que el motor NO FUE CREADO
        self.assertEqual(response.status_code, 401)
        self.assertIn('n_serie', response.json())  # Verificar que la respuesta contiene el campo n_serie
        try:
            data = response.json()
            self.assertIn('fecha_inicio', data)  # Verificar que el error menciona el campo fecha_inicio
        except requests.exceptions.JSONDecodeError:
            self.fail(f"Error al decodificar JSON: {response.text}")
            
if __name__ == '__main__':
    unittest.main()