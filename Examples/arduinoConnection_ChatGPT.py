import tkinter as tk
from tkinter import scrolledtext
import serial
import serial.tools.list_ports
import threading
import queue
from typing import List, Optional
from measurement import singleton


def get_ports() -> List[str]:
    """Obtener una lista de puertos seriales disponibles."""
    return [port.device for port in serial.tools.list_ports.comports()]


@singleton
class ArduinoConnection:
    def __init__(self) -> None:
        self.vector: Optional[serial.Serial] = serial.Serial()
        self.running: bool = False
        self.cola: queue.Queue[str] = queue.Queue()

    def connect(self, port: str, baud: int, timeout: Optional[float] = 1.0) -> None:
        """Conectar al puerto serial con el baudrate especificado."""
        self.vector.port = port
        self.vector.baudrate = baud
        self.vector.timeout = timeout
        try:
            self.vector.open()
            self.running = True
            print(f"Conectado al puerto {port} con baudrate {baud}.")
        except serial.SerialException as e:
            print(f"Error al abrir el puerto {port}: {e}")

    def disconnect(self) -> None:
        """Desconectar del puerto serial."""
        if self.vector.is_open:
            self.running = False
            self.vector.close()
            print("Conexión serial cerrada.")
        else:
            print("No hay conexión serial para cerrar.")

    def reading(self) -> None:
        """Leer datos desde el puerto serial y añadirlos a la cola."""
        while self.running:
            try:
                data = self.vector.readline().strip().decode('utf-8')
                self.cola.put(data)
            except serial.SerialException as e:
                print(f"Error al leer desde el puerto: {e}")
                self.running = False
            except AttributeError:
                pass
            except Exception as e:
                print(f"Error inesperado: {e}")

    def start_reading(self) -> None:
        """Iniciar un hilo para leer datos desde el puerto serial."""
        threading.Thread(target=self.reading, daemon=True).start()

    def get_reading(self) -> Optional[str]:
        """Obtener la siguiente lectura de la cola."""
        try:
            return self.cola.get_nowait()
        except queue.Empty:
            return None

    def check_connection(self) -> bool:
        """Verificar si el puerto serial está abierto."""
        return self.vector.is_open


# Este es un ejemplo de uso
class SerialMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Monitor Serial Arduino")

        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20)
        self.text_area.grid(column=0, row=0, padx=10, pady=10)

        self.conn = ArduinoConnection()
        self.ports = get_ports()
        if self.ports:
            self.conn.connect('COM4', 115200, 1)
            self.conn.start_reading()

        self.update_text_area()

    def update_text_area(self):
        if self.conn.check_connection():
            data = self.conn.get_reading()
            if data:
                self.text_area.insert(tk.END, data + "\n")
                self.text_area.yview(tk.END)
                print(data)
        self.root.after(100, self.update_text_area)  # Actualizar cada 100 ms


if __name__ == '__main__':
    root = tk.Tk()
    app = SerialMonitorApp(root)
    root.mainloop()
