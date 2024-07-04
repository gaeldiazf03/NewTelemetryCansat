import serial
import serial.tools.list_ports
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

    def connect(self, port: str, baud: int) -> None:
        self.vector.port = port
        self.vector.baudrate = baud
        self.vector.open()

    def disconnect(self) -> None:
        try:
            self.vector.close()
        except AttributeError:  # Si la conexión no es creada
            print("There is no serial connection!")

    def read(self) -> str | None:
        try:
            return str(self.vector.readline())
        except AttributeError:
            pass
        except serial.SerialException:
            pass

    def check_connection(self) -> bool:
        return self.vector.is_open


if __name__ == '__main__':
    connection: ArduinoConnection = ArduinoConnection()
    print(connection.check_connection())
