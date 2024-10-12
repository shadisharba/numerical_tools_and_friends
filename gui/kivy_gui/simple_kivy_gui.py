from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout

KV = '''
BoxLayout:
    orientation: 'vertical'

    MDRaisedButton:
        text: '1'
        on_press: app.button_pressed(1)

    MDRaisedButton:
        text: '2'
        on_press: app.button_pressed(2)

    MDRaisedButton:
        text: '3'
        on_release: app.button_released(3)
'''

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def button_pressed(self, button_number):
        print(f'Button {button_number} pressed.')

    def button_released(self, button_number):
        print(f'Button {button_number} clicked.')

if __name__ == '__main__':
    MyApp().run()
