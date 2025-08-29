import openpyxl

wb = openpyxl.load_workbook('sample.xlsx')

ws = wb.active

ws['A1'] = 'Excelsio!'

wb.save('sample.xlsx')
