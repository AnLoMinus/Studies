import PySimpleGUIQt as sg

form = sg.FlexForm('My first GUI')

layout = [ [sg.Text('Enter your First Name', size=(15, 1)), sg.InputText()],
           [sg.Text('Enter your Last Name', size=(15, 1)), sg.InputText()],
           [sg.Text('Enter your Country', size=(15, 1)), sg.InputText()],
           [sg.Text('Enter your Phone', size=(15, 1)), sg.InputText()],
           [sg.Text('Enter your City', size=(15, 1)), sg.InputText()],
           [sg.OK(), sg.Cancel()] ]

button, values = form.Layout(layout).Read()
name = values[0]
lname = values[1]
country = values[2]
phone = values[3]
city = values[4]

print(f"First Name: {name}, Last Name: {lname}, Country: {country}, Phone: {phone}, City: {city}")
