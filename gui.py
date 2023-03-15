import chore_functions
import PySimpleGUI as sg



label = sg.Text("Add something to your chore list")
input_box = sg.InputText(tooltip="Enter chore", key="chore")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=chore_functions.get_chores(), key='chores', 
                        enable_events=True, size=[45, 10])
edit_button=sg.Button("Edit")

window = sg.Window('Chore App', 
                layout=[[label], [input_box, add_button], [list_box, edit_button]], font=('Helvetica', 14))
while True:
    event, values = window.read()
    match event:
        case "Add":
            chores = chore_functions.get_chores()
            new_chore = values['chore'] + '\n'
            chores.append(new_chore)
            chore_functions.write_chores(chores)
            window['chores'].update(values=chores)
        case "Edit":
            chore_to_edit = values['chores'][0]
            new_chore = values['chore']

            chores = chore_functions.get_chores()
            index = chores.index(chore_to_edit)
            chores[index] = new_chore + '\n'
            chore_functions.write_chores(chores)
            window['chores'].update(values=chores)
        case 'chores':
            window['chore'].update(value=values['chores'][0])
        case sg.WIN_CLOSED:
            break

window.close()