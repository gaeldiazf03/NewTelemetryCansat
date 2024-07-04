import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter as tk


class MenuFrame(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(master=parent, *args, **kwargs)

        self.str_conn = tk.StringVar()
        self.str_conn.set("Not connected")

        self.style_button = ttk.Style()
        self.style_button.configure(
            'MyCustomButton.TButton',
            font=("Helvetica", 12),
            background="#303030"
        )

        # Define initial button with initial command
        self.start_connection = ttk.Button(
            self,
            textvariable=self.str_conn,
            style='MyCustomButton.TButton',
            command=self.check_connectButton  # Pass the function reference without parentheses
        )
        self.start_connection.pack(side='left', padx=100)

        self.change_command_btn = ttk.Button(
            self,
            text="Change Command",
            command=self.change_button_command
        )
        self.change_command_btn.pack(side='left', padx=100)

    def check_connectButton(self):
        print("Check connection button clicked")
        self.str_conn.set("Checking connection...")
        self.start_connection["command"] = self.init_connection  # Change command to the next function

    def init_connection(self):
        print("Initiating connection")
        self.str_conn.set("Connected")
        self.start_connection["command"] = self.check_connectButton  # Optionally, you can switch back the command if needed

    def change_button_command(self):
        # Change the command of the start_connection button
        self.start_connection["command"] = self.init_connection
        print("Command changed to 'init_connection'")


if __name__ == '__main__':
    app = ttk.Window(themename='darkly')
    app.title('Change Button Command Example')
    app.geometry('400x200')

    frame = MenuFrame(app)
    frame.pack(fill="x", expand=True)

    app.mainloop()
