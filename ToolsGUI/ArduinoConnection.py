import serial
import serial.tools.list_ports
from measurement import singleton


def get_ports() -> list[str]:
    return [port.device for port in serial.tools.list_ports.comports()]


@singleton
class ArduinoConnection:
    def __init__(self) -> None:
        self.vector = None
        self.baudrates = [9600, 115200]
        self.puertos = get_ports()
        self.reading = self.read()        

    def connect(self, port: str, baud: int = 115200) -> None:
        try:
            self.vector = serial.Serial(port, baud, timeout=0.1)
        except serial.SerialException:
            print("Could not connect to Arduino, check your connection and try again.")

    def disconnect(self) -> None:
        try:
            self.vector.close()
        except AttributeError:  # Si la conexión no es creada
            print("There is no serial connection!")

    def read(self) -> str:
        try:
            return str(self.vector.readline())
        except AttributeError:
            print("Couldn't read from Arduino!")


if __name__ == '__main__':
    pass
