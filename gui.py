import chore_functions
import PySimpleGUI as sg



label = sg.Text("Add something to your chore list")
input_box = sg.InputText(tooltip="Enter chore", key="chore")
add_button = sg.Button("Add")

window = sg.Window('Chore App', 
                layout=[[label], [input_box, add_button]], font=('Helvetica', 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            chores = chore_functions.get_chores()
            new_chore = values['chore'] + '\n'
            chores.append(new_chore)
            chore_functions.write_chores(chores)
        case sg.WIN_CLOSED:
            break

window.close()