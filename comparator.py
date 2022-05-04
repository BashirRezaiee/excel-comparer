import PySimpleGUI as sg
from openpyxl import load_workbook
from os import listdir

def dp(window, event, values):
    print('Inside dp')

    dp_file_path = values['-dpDpFile-']
    country_name = values['-dpCountryName-']
    spirit = values['-dpSpirit-']
    sheet = 'Time Periods'

    # load excel file
    wb = load_workbook(dp_file_path)

    # get the sheet
    ws = wb[sheet]

    # find the cell containing the country name
    header_row = ws.iter_cols(min_row=2, min_col=7, max_row=2)

    for a in header_row:
        if country_name in str(a[0].value):
           target_col = a[0]
           break

    if target_col:
        rows = ws.iter_rows(min_col=target_col.column, max_col=target_col.column, min_row=7)

        for r in rows:
            if spirit == r[0].value:
                sg.popup(f'The {spirit} has been found on {target_col.column_letter}{r[0].row}.')
                return
        
        sg.popup(f'Could not find {spirit} for country {country_name} in this file.')


def labeled(window, event, values):
    print('Inside labeled')

    dp_file_path = values['-labeledDpFile-']
    country_code = values['-labeledCountryCode-']
    max_row = int(values['-labeledMaxRow-'])
    folder_path = values['-labeledSearchFolder-']
    sheet = 'Time Periods'

    # load excel file
    wb = load_workbook(dp_file_path)

    # get the sheet
    ws = wb[sheet]

    # find the cell containing the country name
    header_row = ws.iter_cols(min_row=6, max_row=max_row, min_col=2, max_col=3)

    # get filenames to search in the folder
    filenames = []
    for i, e in enumerate(header_row):
        filenames = filenames + list(e)
    filtered = [i.value.replace('MarketCountryCode', country_code) for i in filenames if i.value != None]

    folder_files = listdir(folder_path)
    folder_files_without_extension = [x.split('.')[0] for x in folder_files]

    diff = set(filtered) - set(folder_files_without_extension) 

    result = f'The Following {len(diff)} files is not present in the specified folder:\n\n'

    for d in diff:
        result += f'- {d}\n'

    sg.popup(result)

def check_brand(window, event, values):
    print('Inside check_brand')

    brand_list_path = values['-brandListFile-']
    baner_path = values['-brandBanerFile-']
    country_code = values['-countryCode-']

    # load files
    brand_list_file = load_workbook(brand_list_path, read_only=True)
    brand_baner_file = load_workbook(baner_path, read_only=True)

    # sheets
    listSheet = brand_list_file[country_code]
    banerSheet = brand_baner_file['Home']

    # load brand list 
    cols = listSheet.iter_rows(min_row=2, min_col=7, max_col=7)
    brand_list = [item.value for sublist in list(cols) for item in sublist if item.value != None]

    # load baner 
    cols2 = banerSheet.iter_rows(min_row=2, min_col=2, max_col=2)
    baner_list = [item.value.removeprefix('5 Cs - ') for sublist in list(cols2) for item in sublist if item.value != None]
    
    diff = set(brand_list) - set(baner_list)

    result = f'The following Brand Names from brand master list is not present on the Baner file.\n\n'
    for d in diff: 
        result += f'- {d}\n'

    sg.popup(result, title='Differences')