import xlrd
import numpy as np

file_location = "C:\\Users\\Deepp\\PycharmProjects\\CS141_GradeLookup\\output.xlsx"
xlrd.open_workbook(file_location)

workbook = xlrd.open_workbook(file_location)

sheet_1 = workbook.sheet_by_index(0)
sheet_2 = workbook.sheet_by_index(1)
sheet_3 = workbook.sheet_by_index(2)
sheet_4 = workbook.sheet_by_index(3)

nrows = sheet_1.nrows
ncols = sheet_1.ncols

c = 0
r = 0

for r in range(nrows):
    row = sheet_1.row(r)
    for c, cell in enumerate(row):
            if cell.value == "Code#":
                codec = c
                coder = r

nrows = sheet_1.nrows + sheet_2.nrows + sheet_3.nrows + sheet_4.nrows

code_NUM = []
lab1_Quiz = []
lab2_Quiz = []


r = 0
for r in range(r, nrows - 10):
    code_NUM.append(sheet_1.cell_value(coder + 4 + r, codec))


print(len(code_NUM))
print(len(lab1_Quiz))
print(len(lab2_Quiz))


#codename =
#lab1_Quiz :
