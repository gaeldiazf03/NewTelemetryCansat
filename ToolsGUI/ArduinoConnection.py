import serial
import serial.tools.list_ports
import threading
import queue
from measurement import singleton


def get_ports() -> list[str]:
    return [
        port.device
        for port in serial.tools.list_ports.comports()
    ]


@singleton
class ArduinoConnection:
    def __init__(self) -> None:
        self.vector = serial.Serial()
        self.running = False
        self.cola = queue.Queue()

    def connect(self, port: str, baud: int) -> None:
        self.vector.port = port
        self.vector.baudrate = baud
        self.vector.open()
        self.running = True

    def disconnect(self) -> None:
        try:
            self.running = False
            self.vector.close()
        except AttributeError:  # Si la conexión no es creada
            print("There is no serial connection!")

    def reading(self) -> None:
        while self.running:
            try:
                data = str(self.vector.readline().strip().decode('utf-8'))
                self.cola.put(data)
            except AttributeError:
                pass
            except serial.SerialException:
                pass

    def start_reading(self) -> None:
        threading.Thread(target=self.reading, daemon=True).start()

    def get_reading(self):
        return self.cola.get()

    def check_connection(self) -> bool:
        return self.vector.is_open


if __name__ == '__main__':
    connection: ArduinoConnection = ArduinoConnection()
    print(connection.check_connection())
