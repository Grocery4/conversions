
import PySimpleGUI as sg

def main():

    margin_x = 500
    margin_y = 300

    layout = [
        [sg.Text("Welcome to Ru's converter!")],
        [sg.Button("Convert")]  
    ]

    window = sg.Window("Ru's Converter", layout, margins=(margin_x, margin_y))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

    window.close()


main()