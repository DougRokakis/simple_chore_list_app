from functions import get_todos, write_todos
import PySimpleGUI as sg



label = sg.Text("Add something to your chore list")
input_box = sg.InputText(tooltip="Enter chore")
add_button = sg.Button("Add")

window = sg.Window('Chore App', layout=[[label], [input_box, add_button]])
window.read()
window.close()