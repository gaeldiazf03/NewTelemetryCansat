import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class MonitorContainer(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.pack(fill=BOTH, expand=True)
