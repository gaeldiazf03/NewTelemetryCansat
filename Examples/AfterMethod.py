import tkinter as tk
from tkinter import ttk
import time


class ExampleApp(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack()

        self.label1 = ttk.Label(self, text="Actualizando cada 500 ms")
        self.label1.pack(pady=10)
        self.label2 = ttk.Label(self, text="Actualizando cada 1000 ms")
        self.label2.pack(pady=10)

        self.update_label1()
        self.update_label2()

    def update_label1(self):
        self.label1.config(text="Tiempo actual: {}".format(self.get_current_time()))
        self.after(500, self.update_label1)  # Reprogramar después de 500 ms

    def update_label2(self):
        self.label2.config(text="Fecha actual: {}".format(self.get_current_date()))
        self.after(1000, self.update_label2)  # Reprogramar después de 1000 ms

    @staticmethod
    def get_current_time():
        return time.strftime('%H:%M:%S')

    @staticmethod
    def get_current_date():
        return time.strftime('%Y-%m-%d')


if __name__ == '__main__':
    root = tk.Tk()
    app = ExampleApp(root)
    root.mainloop()
