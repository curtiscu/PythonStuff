

'''

Uses OpenPyXL..
    https://openpyxl.readthedocs.io/en/stable/ \n
    https://medium.com/aubergine-solutions/working-with-excel-sheets-in-python-using-openpyxl-4f9fd32de87f \n


'''

# utility function by curtiscu
# nice/ pretty print stuff ...
def pp(tab_count, str):
    print('\t'*tab_count, str)


import openpyxl
from openpyxl.compat import range
from openpyxl.utils import get_column_letter

# load our excel sheet
cxn = openpyxl.load_workbook('Customers2016.xlsx')

pp(0,'csn type: {}'.format(type(cxn)))

sheet1 = cxn['Sheet1']

pp(0,'\n A1 cell: {}'.format(sheet1['A1'].value))

# TODO - finish this stuff off

