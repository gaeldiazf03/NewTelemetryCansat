import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class MonitorContainer(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.configure(padding=(15, 30, 15, 30))
        self.value_example = 0

        self.altura_lblframe = ttk.Labelframe(
            self,
            text='Altura',
            style='info.TLabelFrame'
        )
        self.altura_lblframe.pack()

        self.altura = ttk.Progressbar(
            self.altura_lblframe,
            maximum=100,
            mode='determinate',
            length=500,
            value=self.value_example
        )
        self.altura.pack(pady=10)
        self.update_progressbar()

    def update_progressbar(self) -> None:
        if self.value_example >= 100:
            self.value_example = 0
        else:
            self.value_example += 1
            self.altura.step(1)
        print(self.value_example)
        self.after(100, self.update_progressbar)


if __name__ == '__main__':
    import tkinter as tk
    from tkinter import ttk

    def calculate_progress(value):
        absolute_min = 2
        absolute_max = 50
        progress_min = 0
        progress_max = 100
        absolute_range = absolute_max - absolute_min
        progress_range = progress_max - progress_min
        if value <= 24:
            progress = 1.5625 * value + 3.125
        else:
            progress = 2.0833 * value - 22.0833
        progress_percentage = ((progress - absolute_min) * progress_range) / absolute_range
        return progress_percentage

    def update_progress():
        global sensor_reading
        sensor_reading+=1
        progress = calculate_progress(sensor_reading)
        progress_bar['value'] = progress

    sensor_reading = 0
    root = tk.Tk()
    root.title("Non-Linear Progress Bar Example")

    progress_bar = ttk.Progressbar(root, length=400, mode='determinate', maximum=100)
    progress_bar.pack(pady=20)
    b = tk.Button(root,text='update', command=update_progress)
    b.pack()
    root.mainloop()
