import PySimpleGUI as sg
import converter
import os

running=True

main_window_layout=[[sg.Text("Automatic Transcript Maker")],[sg.Text("Enter the FileName")],[sg.Input(key='-FILE_NAME-')],[sg.Button("Convert")],[sg.Text(size=(40,20),key="-OUTPUT-")],[sg.Text("®This Software was desingned and developed by Asher Mathews Shaji ")]]


window=sg.Window("Main",main_window_layout)


while running:
    event,values=window.read()

    if event==sg.WINDOW_CLOSED or event=="Quit":
        running=False
    if(event=="Convert"):
        file_name=values["-FILE_NAME-"]
        result=converter.convert(file_name)
        window["-OUTPUT-"].update(result)
        os.remove("audio.wav")



