import chore_functions
import PySimpleGUI as sg



label = sg.Text("Add something to your chore list")
input_box = sg.InputText(tooltip="Enter chore", key="chore")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=chore_functions.get_chores(), key='chores', 
                        enable_events=True, size=[45, 10])
edit_button=sg.Button("Edit")
complete_button = sg.Button("Completed")
exit_button = sg.Button("Exit")

window = sg.Window('Chore App', 
                layout=[[label], [input_box, add_button], [list_box, edit_button, complete_button], [exit_button]], font=('Helvetica', 14))
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
        case "Completed":
            chore_to_complete = values['chores'][0]
            chores = chore_functions.get_chores()
            chores.remove(chore_to_complete)
            chore_functions.write_chores(chores)
            window['chores'].update(values=chores)
            window['chore'].update(value='')
        case "Exit":
            break
        case 'chores':
            window['chore'].update(value=values['chores'][0])
        case sg.WIN_CLOSED:
            break

window.close()