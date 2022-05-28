import PySimpleGUI as sg
import comparator

sg.theme("TealMono")
app_name = "Excel Comparer"
font = "Arial, 12"

dp_layout = [
    [sg.Text(f'\n In this tab we check if the specified wave for a given country is present in the \n Prime DP Global Spec file. \n \n The following checklist items will be checked:\n - checklist 1 \n - checklist 2')],
    [sg.HorizontalSeparator()],
    [sg.Text('DP File: ')],
    [sg.Input(key='-dpDpFile-'), sg.FileBrowse(file_types=(("Excel Files", "*.xlsx"),))],
    [sg.Text('Country Name: ')],
    [sg.Input('Canada', key='-dpCountryName-')],
    [sg.Text('Wave: ')],
    [sg.Input('Y1/W1', key='-dpSpirit-')],
    [sg.Button('Search')]
]

labeled_layout = [
    [sg.Text(f'\n In this tab we check if all benner files (KPI and BrandCo) from Prime DP Global Spec file \n is present in the specified folder for a specific country. \n \n The following checklist items will be checked:\n - checklist 1 \n - checklist 2')],
    [sg.HorizontalSeparator()],
    [sg.Text('Prime DP Global Spec File: ')],
    [sg.Input(key='-labeledDpFile-'), sg.FileBrowse(file_types=(("Excel Files", "*.xlsx"),))],
    [sg.Text('Country Code: ')],
    [sg.Input('AR', key='-labeledCountryCode-')],
    [sg.Text('Folder to search in: ')],
    [sg.Input(key='-labeledSearchFolder-'), sg.FolderBrowse()],
    [sg.Text('Lookup upto row: ')],
    [sg.Input('20', key='-labeledMaxRow-')],
    [sg.Button('Go')]   
]

check_brand_layout = [
    [sg.Text('Brand list file: ')],
    [sg.Input(key='-brandListFile-'), sg.FileBrowse(file_types=(("Excel Files", "*.xlsx"),))],
    [sg.Text('Country Code: ')],
    [sg.Input('AR', key='-countryCode-')],
    [sg.Text('Banner Type: ')],
    [sg.Radio('BrandCo', 'BannerType', default=True, key='-BrandCo-'), 
     sg.Radio('KPI', 'BannerType', key='-KPI-'), 
     sg.Radio('KPI Yearly', 'BannerType', key='KPIYearly')],
    [sg.Text('Year: ')],
    [sg.Input('FY18', key='-brandYear-')],
    [sg.Text('Quarter: ')],
    [sg.Input('2', key='-brandQuarter-')],
    [sg.Text('Folder to search in: ')],
    [sg.Input(key='-brandSearchFolder-'), sg.FolderBrowse()],
    # [sg.Text('Baner file: ')],
    # [sg.Input(key='-brandBanerFile-'), sg.FileBrowse(file_types=(("Excel Files", "*.xlsx"),))],
    [sg.Button('Check')]   
]

layout = [[
    sg.TabGroup([
        [sg.Tab('Wave Defined in DP', dp_layout),
         sg.Tab('Brand Files Lebeled Correctly', labeled_layout),
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
            comparator.dp(values)
        elif event == "Go":
            comparator.labeled(values)
        elif event == "Check":
            comparator.check_brand(values)
    except Exception as ex:
        sg.PopupError('Something went wrong', 'close this window and copy command line from text printed out in main window','Here is the output from the run', ex)

window.close()