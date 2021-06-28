#the main window
import PySimpleGUI as main

f = open("ideas.txt", "r")
Content = f.read()

home = [[main.Text("This is the default")]]

ideas = [
    [main.Text("My Ideas: ")],
    [main.Text(Content)]
]

layout = [
    [main.Text("Welcome to my Everything")], 
    [main.TabGroup([[main.Tab('Home', home), main.Tab('IDEAS', ideas)]])],
    [main.Button("END")]]

# Create the window
w, h = main.Window.get_screen_size()
window = main.Window("Everything", layout).Finalize()
window.Maximize()

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "END" or event == main.WIN_CLOSED:
        break

window.close()
