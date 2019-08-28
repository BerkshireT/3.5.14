# **********************************************************
#
#    filename:  3_5_14.py
#
#    description: Implements the evaluator in 3.4.15 for HW1
#
#    author: Tyler Berkshire
#    login id:  none
#
#    class:  CPS 452
#    instructor:  Perugini
#    assignment:  Homework #1
#
#    assigned:  Aug 21, 2019
#    due:  Aug 26, 2019
#
# **********************************************************

import PySimpleGUI as sg
import evaluator

layout = [[sg.Text("Expression:"), sg.InputText(key='__INPUT__')],
          [sg.Text("Answer:"), sg.Text("", size = (25, 1), key='__ANSWER__')],
          [sg.Button("Evaluate"), sg.Button("Clear")]]

window = sg.Window("Postfix Evaluator", layout)

# Active window
while True:
    event, values = window.Read()
    if event is "Evaluate":
        window.FindElement('__ANSWER__').Update(evaluator.evaluate_postfix(values['__INPUT__']))
    if event is "Clear":
        window.FindElement('__INPUT__').Update("")
        window.FindElement('__ANSWER__').Update("")
    if event is None:
        break;

window.Close()
