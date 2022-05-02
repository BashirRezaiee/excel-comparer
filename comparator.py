# from openpyxl.worksheet import WorkSheet;
import PySimpleGUI as sg
from openpyxl import load_workbook

def dp(window, event, values):
    print('Inside dp')

    dp_file_path = values['-dpDpFile-']
    country_name = values['-dpCountryName-']
    spirit = values['-dpSpirit-']
    sheet = 'Time Periods'

    # dp_file_path = '/home/bashir/projects/python/excel-comparer/venv/dp.xlsx'
    # country_name = 'France'
    # spirit = 'Y1/W5'

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


def check_brand(window, event, values):
    print('Inside check_brand')




# def case1(ws1: WorkSheet, ws2: WorkSheet, col1: str, col2: str):
#     # load the column and sort
#     col1_data = list(ws1[col1])
#     col2_data = list(ws2[col2])

#     # remove first row
#     del col1_data[0]
#     del col2_data[0]

#     for idx, d in enumerate(col1_data):
#         col1_data[idx] = d.value

#     for idx, d in enumerate(col2_data):
#         col2_data[idx] = d.value.removeprefix('5 Cs - ')

#     col1_data = [k for k in col1_data if isinstance(k, str)]
#     col2_data = [k for k in col2_data if isinstance(k, str)]

#     not_in_col2 = [k for k in col1_data if k not in col2_data]
#     not_in_col1 = [k for k in col2_data if k not in col1_data]

#     for i in not_in_col2:
#         print(f"{i} is not in column {col2} on worksheet {ws2.title}")

#     print('\n')

#     for i in not_in_col1:
#         print(f"{i} is not in column {col1} on worksheet {ws1.title}")