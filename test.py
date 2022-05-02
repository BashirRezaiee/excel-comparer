import PySimpleGUI as sg

sg.theme('Dark Blue 3')  # please make your windows colorful

# layout = [[sg.Text('Filename')],
#             [sg.Input(), sg.FileBrowse()],
#             [sg.OK(), sg.Cancel()] ]

# window = sg.Window('Get filename example', layout)
# event, values = window.read()
# window.close()

# sg.Popup(event, values[0])



# layout = [[sg.Text('SHA-1 and SHA-256 Hashes for the file')],
#                  [sg.InputText(), sg.FileBrowse()],
#                  [sg.Submit(), sg.Cancel()]]

# window = sg.Window('SHA-1 & 256 Hash', layout)

# event, values = window.read()
# window.close()

# source_filename = values[0]   



# layout = [[sg.Text('Your typed chars appear here:'), sg.Text(size=(12,1), key='-OUTPUT-')],
#           [sg.Input(key='-IN-')],
#           [sg.Button('Show'), sg.Button('Exit')]]

# window = sg.Window('Window Title', layout)

# while True:  # Event Loop
#     event, values = window.read()
#     print(event, values)
#     if event == sg.WIN_CLOSED or event == 'Exit':
#         break
#     if event == 'Show':
#         # change the "output" element to be the value of "input" element
#         window['-OUTPUT-'].update(values['-IN-'])

# window.close()



# layout = [[sg.Text('Rename files or folders')],
#       [sg.Text('Source for Folders', size=(15, 1)), sg.InputText(), sg.FolderBrowse()],
#       [sg.Text('Source for Files ', size=(15, 1)), sg.InputText(), sg.FileBrowse()],
#       [sg.Submit(), sg.Cancel()]]

# window = sg.Window('Rename Files or Folders', layout)

# event, values = window.read()
# window.close()
# folder_path, file_path = values[0], values[1]       # get the data from the values dictionary
# print(folder_path, file_path)





"""
    Demo - Element List

    All 34 elements shown in 1 window as simply as possible.

    Copyright 2022 PySimpleGUI
"""

# use_custom_titlebar = False

# def make_window(theme=None):
#     NAME_SIZE = 23

#     def name(name):
#         dots = NAME_SIZE-len(name)-2
#         return sg.Text(name + ' ' + '•'*dots, size=(NAME_SIZE,1), justification='r',pad=(0,0), font='Courier 10')

#     sg.theme(theme)

#     treedata = sg.TreeData()

#     treedata.Insert("", '_A_', 'Tree Item 1', [1234], )
#     treedata.Insert("", '_B_', 'B', [])
#     treedata.Insert("_A_", '_A1_', 'Sub Item 1', ['can', 'be', 'anything'], )

#     layout_l = [[name('Text'), sg.Text('Text')],
#                 [name('Input'), sg.Input(s=15)],
#                 [name('Multiline'), sg.Multiline(s=(15,2))],
#                 [name('Output'), sg.Output(s=(15,2))],
#                 [name('Combo'), sg.Combo(sg.theme_list(), default_value=sg.theme(), s=(15,22), enable_events=True, readonly=True, k='-COMBO-')],
#                 [name('OptionMenu'), sg.OptionMenu(['OptionMenu',],s=(15,2))],
#                 [name('Checkbox'), sg.Checkbox('Checkbox')],
#                 [name('Radio'), sg.Radio('Radio', 1)],
#                 [name('Spin'), sg.Spin(['Spin',], s=(15,2))],
#                 [name('Button'), sg.Button('Button')],
#                 [name('ButtonMenu'), sg.ButtonMenu('ButtonMenu', sg.MENU_RIGHT_CLICK_EDITME_EXIT)],
#                 [name('Slider'), sg.Slider((0,10), orientation='h', s=(10,15))],
#                 [name('Listbox'), sg.Listbox(['Listbox', 'Listbox 2'], no_scrollbar=True,  s=(15,2))],
#                 [name('Image'), sg.Image(sg.EMOJI_BASE64_HAPPY_THUMBS_UP)],
#                 [name('Graph'), sg.Graph((125, 50), (0,0), (125,50), k='-GRAPH-')]  ]

#     layout_r  = [[name('Canvas'), sg.Canvas(background_color=sg.theme_button_color()[1], size=(125,50))],
#                 [name('ProgressBar'), sg.ProgressBar(100, orientation='h', s=(10,20), k='-PBAR-')],
#                 [name('Table'), sg.Table([[1,2,3], [4,5,6]], ['Col 1','Col 2','Col 3'], num_rows=2)],
#                 [name('Tree'), sg.Tree(treedata, ['Heading',], num_rows=3)],
#                 [name('Horizontal Separator'), sg.HSep()],
#                 [name('Vertical Separator'), sg.VSep()],
#                 [name('Frame'), sg.Frame('Frame', [[sg.T(s=15)]])],
#                 [name('Column'), sg.Column([[sg.T(s=15)]])],
#                 [name('Tab, TabGroup'), sg.TabGroup([[sg.Tab('Tab1',[[sg.T(s=(15,2))]]), sg.Tab('Tab2', [[]])]])],
#                 [name('Pane'), sg.Pane([sg.Col([[sg.T('Pane 1')]]), sg.Col([[sg.T('Pane 2')]])])],
#                 [name('Push'), sg.Push(), sg.T('Pushed over')],
#                 [name('VPush'), sg.VPush()],
#                 [name('Sizer'), sg.Sizer(1,1)],
#                 [name('StatusBar'), sg.StatusBar('StatusBar')],
#                 [name('Sizegrip'), sg.Sizegrip()]  ]

#     layout = [[sg.MenubarCustom([['File', ['Exit']], ['Edit', ['Edit Me', ]]],  k='-CUST MENUBAR-',p=0)] if use_custom_titlebar else [sg.Menu([['File', ['Exit']], ['Edit', ['Edit Me', ]]],  k='-CUST MENUBAR-',p=0)],
#               [sg.Checkbox('Use Custom Titlebar & Menubar', use_custom_titlebar, enable_events=True, k='-USE CUSTOM TITLEBAR-')],
#               [sg.T('PySimpleGUI Elements - Use Combo to Change Themes', font='_ 18', justification='c', expand_x=True)],
#               [sg.Col(layout_l), sg.Col(layout_r)]]

#     window = sg.Window('The PySimpleGUI Element List', layout, finalize=True, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT, keep_on_top=True, use_custom_titlebar=use_custom_titlebar)

#     window['-PBAR-'].update(30)                                                     # Show 30% complete on ProgressBar
#     window['-GRAPH-'].draw_image(data=sg.EMOJI_BASE64_HAPPY_JOY, location=(0,50))   # Draw something in the Graph Element

#     return window

# # Start of the program...
# window = make_window()

# while True:
#     event, values = window.read()
#     sg.popup(event, values)                     # show the results of the read in a popup Window
#     if event == sg.WIN_CLOSED or event == 'Exit':
#         break
#     if values['-COMBO-'] != sg.theme():
#         sg.theme(values['-COMBO-'])
#         window.close()
#         window = make_window()
#     if event == '-USE CUSTOM TITLEBAR-':
#         use_custom_titlebar = values['-USE CUSTOM TITLEBAR-']
#         window.close()
#         window = make_window()
# window.close()

import time

def my_function():
    time.sleep(30)

def my_function_with_parms(duration):
    time.sleep(duration)
    return 'My Return Value'

layout = [  [sg.Text('Call a lengthy function')],
            [sg.Button('Start'), sg.Button('Start 2'), sg.Button('Exit')]  ]

window = sg.Window('Long Operation Example', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Start':
        window.perform_long_operation(my_function, '-FUNCTION COMPLETED-')
    elif event == 'Start 2':
        window.perform_long_operation(lambda: my_function_with_parms(10), '-FUNCTION COMPLETED-')
    elif event == '-FUNCTION COMPLETED-':
        sg.popup('Your function completed!')
window.close()



