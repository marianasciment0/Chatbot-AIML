import PySimpleGUI as sg
import os
import aiml


BRAIN_FILE="brain.dump"
k = aiml.Kernel()
if os.path.exists(BRAIN_FILE):
    print("Loading from brain file: " + BRAIN_FILE)
    k.loadBrain(BRAIN_FILE)
else:
    k.bootstrap(learnFiles="learningFileList.aiml", commands="LEARN AIML")
    print("Saving brain file: " + BRAIN_FILE)
    k.saveBrain(BRAIN_FILE)

def Chatbot():
    sg.theme('SandyBeach')
    sg.set_options(font = ('Courier 16'), text_color = 'black')

    layout = [
        [sg.Output(size=(60, 15))],
        [sg.T('User >'), sg.I(size=(43, 3), key = 'INPUT'), sg.Button('Enviar', expand_x = True)]
    ]

    window = sg.Window('Chatbot', layout)

    while True:
        event, values = window.read()
        if event == 'Enviar':
            print("User > ",values['INPUT'])
            response = k.respond(values['INPUT'])
            print("Bot > ", response)
            window['INPUT'].update('')
        elif event in (sg.WIN_CLOSED):
            break
        
    window.close()

Chatbot()