from tkinter import messagebox as mb
import tkinter as tk


def start_gui():
    """Start the GUI application."""
    root = tk.Tk()
    root.overrideredirect(1)
    root.withdraw()
    mb.showinfo('Test Message',
                'Everything works! \n This is a test message from '
                'python_tkinter_demo!')
    version_num = 0.1
    print('The version of the called programm is ' + str(version_num))
    root.destroy()


if __name__ == '__main__':
    start_gui()
