"""
Módulo creado con bastante ayuda de ChatGPT, por lo que intenta no modificarlo!
Funciona creando un hilo independiente, donde estará leyendo el serial en paralelo y regresando
lo que recibe. Desde el tkinter se debe de actualizar cada cierto tiempo una función solamente
para reflejar lo que recibes de este módulo.

A este módulo hace falta un ejemplo de uso, pero es verdaderamente intuitivo.
Es por eso que el ejemplo se encuentra en el documento Examples\\arduinoConnection_ChatGPT.py
"""

# Librerías encargadas del serial
import serial
import serial.tools.list_ports
# Librerías encargadas de crear el hilo y una 'cola' (aquí se guarda lo recibido del serial)
from threading import Thread
from queue import Queue, Empty
# Otras librerías
from typing import List  # Para especificar lo que me regresa alguna que otra función
from measurement import singleton  # Patrón Singleton, si no recuerdas busca referencias


def get_ports() -> List[str]:
    return [port.device for port in serial.tools.list_ports.comports()]


@singleton
class ArduinoConnection:
    running: bool = False
    cola: Queue = Queue()

    def __init__(self) -> None:
        self.vector: serial.Serial = serial.Serial()

    def connect(self, port: str, baud: int, timeout: float = 5) -> None:
        self.vector.port = port
        self.vector.baudrate = baud
        self.vector.timeout = timeout

        try:
            self.vector.open()
            self.running = True
            print(f'ESP32 at {port} with baudrate in {baud}.')
        except Exception as e:
            raise Exception(e)

    def disconnect(self) -> None:
        if self.vector.is_open:
            self.running = False
            self.vector.close()
            self.vector.__del__()
            print('Closed connection')
        else:
            print('No connection')

    def reading(self) -> None:
        while self.running:
            try:
                data = str(self.vector.readline().strip().decode('utf-8'))
                self.cola.put(data)
            except serial.SerialException as e:
                print(f'Error al abrir puerto. {e}')
                self.running = False
            except AttributeError:
                pass
            except Exception as e:
                print(f'Error: {e}')

    def start_reading(self) -> None:
        Thread(target=self.reading, daemon=True).start()

    def get_reading(self):
        try:
            return self.cola.get_nowait()
        except Empty:
            return None

    def check_connection(self) -> bool:
        return self.vector.is_open

    def reset_connection(self):  # Ayuda a que lea bien el serial
        self.vector.reset_input_buffer()
