import flet as ft
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from io import BytesIO
from PIL import Image

def main(page: ft.Page):
    def plot_graph():
        x = np.linspace(-5, 5, 100)
        y = np.linspace(-5, 5, 100)
        x, y = np.meshgrid(x, y)
        z = x**2 + y**2

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(x, y, z, cmap='viridis')

        buf = BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        img = Image.open(buf)
        img.save("plot.png")
        buf.close()

        img_widget.src = "plot.png"
        page.update()

    def button_click(e):
        plot_graph()

    text_box = ft.TextField(label="Input", width=200)
    button1 = ft.TextButton(text="Button 1", on_click=button_click)
    button2 = ft.TextButton(text="Button 2", on_click=button_click)
    button3 = ft.TextButton(text="Button 3", on_click=button_click)
    img_widget = ft.Image(src="")

    page.add(text_box, button1, button2, button3, img_widget)

ft.app(target=main)