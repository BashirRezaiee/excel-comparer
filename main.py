import PySimpleGUI as sg
import comparator

sg.theme("TealMono")
app_name = "Excel Comparer"
font = "Arial, 12"

dp_layout = [
    [sg.Text('DP File: ')],
    [sg.Input(key='-dpDpFile-'), sg.FileBrowse(file_types=(("Excel Files", "*.xls *.xlsx"),))],
    [sg.Text('Country Name: ')],
    [sg.Input('Canada', key='-dpCountryName-')],
    [sg.Text('Spirit: ')],
    [sg.Input('Y1/W1', key='-dpSpirit-')],
    [sg.Button('Search')]   
]

labeled_layout = [
    [sg.Text('DP File: ')],
    [sg.Input(), sg.FileBrowse(file_types=(("Excel Files", "*.xls *.xlsx"),))],
    [sg.Text('Country Code: ')],
    [sg.Input(key='-labeledCountryCode-')],
    [sg.Text('Folder to search in: ')],
    [sg.Input('-labeledSearchFolder-'), sg.FolderBrowse()],
    [sg.Text('Baner Type: ')],
    [sg.Checkbox('BrandCo'), sg.Checkbox("KPI")],
    [sg.Button('Go')]   
]

check_brand_layout = [
    [sg.Text('Brand list file: ')],
    [sg.Input(), sg.FileBrowse(file_types=(("Excel Files", "*.xls *.xlsx"),))],
    [sg.Text('Baner file: ')],
    [sg.Input(), sg.FileBrowse(file_types=(("Excel Files", "*.xls *.xlsx"),))],
    [sg.Text('Country Code: ')],
    [sg.Input()],
    [sg.Button('Check')]   
]

layout = [[
    sg.TabGroup([
        [sg.Tab('Is defined in DP', dp_layout),
         sg.Tab('Is labeled correctly', labeled_layout),
         sg.Tab('Check brand names', check_brand_layout)]
    ])
]]

window = sg.Window('Excel Comparer', layout)

while True:  # Event Loop
    event, values = window.read()

    try:
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        elif event == "Search":
            comparator.dp(window, event, values)
        elif event == "Go":
            comparator.labeled(window, event, values)
        elif event == "Check":
            comparator.check_brand(window, event, values)
    except Exception as ex:
        sg.PopupError('Something went wrong', 'close this window and copy command line from text printed out in main window','Here is the output from the run', ex)




window.close()