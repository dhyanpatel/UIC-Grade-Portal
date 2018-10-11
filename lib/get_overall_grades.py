import xlrd
import pandas as pd
import numpy as np
from pprint import pprint

file_location = "C:\\Users\\Deepp\\PycharmProjects\\CS141_GradeLookup\\output.xlsx"
xlrd.open_workbook(file_location)

workbook = xlrd.open_workbook(file_location)

sheet_1 = workbook.sheet_by_index(0)
sheet_2 = workbook.sheet_by_index(1)
sheet_3 = workbook.sheet_by_index(2)
sheet_4 = workbook.sheet_by_index(3)

for t in range(0, 3):
    sheet_Master = sheet_[t]

nrows = sheet_1.nrows
nrows2 = sheet_2.nrows
nrows3 = sheet_3.nrows
nrows4 = sheet_4.nrows
ncols = sheet_1.ncols

c, r, row, col = 0, 0, 0, 0

for r in range(nrows):
    row = sheet_1.row(r)
    for c, cell in enumerate(row):
        if cell.value == "Code#":
            codec = c
            coder = r
            break

for w in range(nrows):
    chill = sheet_1.row(w)
    for d, cell in enumerate(chill):
        if cell.value == "Quiz":
            cool = w
            col = d
            break

code_NUM = []
lab1_Quiz = []
lab2_Quiz = []
lab3_Quiz = []
lab4_Quiz = []
lab6_Quiz = []

lab_Quizes_PER_Score = []


def getCode():
    for a in range(0, nrows - coder - 3):
        code_NUM.append(sheet_1.cell_value(coder + 3 + a, codec))

    for a in range(0, nrows2 - coder - 3):
        code_NUM.append(sheet_2.cell_value(coder + 3 + a, codec))

    for a in range(0, nrows3 - coder - 3):
        code_NUM.append(sheet_3.cell_value(coder + 3 + a, codec))

    for a in range(0, nrows4 - coder - 3):
        code_NUM.append(sheet_4.cell_value(coder + 3 + a, codec))

def get_LAB1_QUIZ():
    for a in range(0, nrows - coder - 3):
        lab1_Quiz.append(sheet_1.cell_value(coder + 3 + a, codec + 1))

    for a in range(0, nrows2 - coder - 3):
        lab1_Quiz.append(sheet_2.cell_value(coder + 3 + a, codec + 1))

    for a in range(0, nrows3 - coder - 3):
        lab1_Quiz.append(sheet_3.cell_value(coder + 3 + a, codec + 1))

    for a in range(0, nrows4 - coder - 3):
        lab1_Quiz.append(sheet_4.cell_value(coder + 3 + a, codec + 1))

def get_LAB2_QUIZ():
    for a in range(0, nrows - coder - 3):
        lab2_Quiz.append(sheet_1.cell_value(coder + 3 + a, codec + 2))

    for a in range(0, nrows2 - coder - 3):
        lab2_Quiz.append(sheet_2.cell_value(coder + 3 + a, codec + 2))

    for a in range(0, nrows3 - coder - 3):
        lab2_Quiz.append(sheet_3.cell_value(coder + 3 + a, codec + 2))

    for a in range(0, nrows4 - coder - 3):
        lab2_Quiz.append(sheet_4.cell_value(coder + 3 + a, codec + 2))

def get_LAB3_QUIZ():
    for a in range(0, nrows - coder - 3):
        lab3_Quiz.append(sheet_1.cell_value(coder + 3 + a, codec + 3))

    for a in range(0, nrows2 - coder - 3):
        lab3_Quiz.append(sheet_2.cell_value(coder + 3 + a, codec + 3))

    for a in range(0, nrows3 - coder - 3):
        lab3_Quiz.append(sheet_3.cell_value(coder + 3 + a, codec + 3))

    for a in range(0, nrows4 - coder - 3):
        lab3_Quiz.append(sheet_4.cell_value(coder + 3 + a, codec + 3))

def get_LAB4_QUIZ():
    for a in range(0, nrows - coder - 3):
        lab4_Quiz.append(sheet_1.cell_value(coder + 3 + a, codec + 4))

    for a in range(0, nrows2 - coder - 3):
        lab4_Quiz.append(sheet_2.cell_value(coder + 3 + a, codec + 4))

    for a in range(0, nrows3 - coder - 3):
        lab4_Quiz.append(sheet_3.cell_value(coder + 3 + a, codec + 4))

    for a in range(0, nrows4 - coder - 3):
        lab4_Quiz.append(sheet_4.cell_value(coder + 3 + a, codec + 4))

def get_LAB6_QUIZ():
    for a in range(0, nrows - coder - 3):
        lab6_Quiz.append(sheet_1.cell_value(coder + 3 + a, codec + 5))

    for a in range(0, nrows2 - coder - 3):
        lab6_Quiz.append(sheet_2.cell_value(coder + 3 + a, codec + 5))

    for a in range(0, nrows3 - coder - 3):
        lab6_Quiz.append(sheet_3.cell_value(coder + 3 + a, codec + 5))

    for a in range(0, nrows4 - coder - 3):
        lab6_Quiz.append(sheet_4.cell_value(coder + 3 + a, codec + 5))


'''
def get_LAB7_QUIZ():
    a = 0
    for a in range(a, nrows - coder - 3):
        lab7_Quiz.append(sheet_1.cell_value(coder + 3 + a, codec + 6))

    a = 0
    for a in range(a, nrows2 - coder - 3):
        lab7_Quiz.append(sheet_2.cell_value(coder + 3 + a, codec + 6))

    a = 0
    for a in range(a, nrows3 - coder - 3):
        lab7_Quiz.append(sheet_3.cell_value(coder + 3 + a, codec + 6))

    a = 0
    for a in range(a, nrows4 - coder - 3):
        lab7_Quiz.append(sheet_4.cell_value(coder + 3 + a, codec + 6))
'''

def lab_Quizes_PERCENTAGE_Score():
    for a in range(0, nrows - cool - 5):
        lab_Quizes_PER_Score.append(sheet_1.cell_value(cool + 5 + a, col))

    for a in range(0, nrows2 - cool - 5):
        lab_Quizes_PER_Score.append(sheet_2.cell_value(cool + 5 + a, col))

    for a in range(0, nrows3 - cool - 5):
        lab_Quizes_PER_Score.append(sheet_3.cell_value(cool + 5 + a, col))

    for a in range(0, nrows4 - cool - 5):
        lab_Quizes_PER_Score.append(sheet_4.cell_value(cool + 5 + a, col))

getCode()
get_LAB1_QUIZ()
get_LAB2_QUIZ()
get_LAB3_QUIZ()
get_LAB4_QUIZ()
get_LAB6_QUIZ()
lab_Quizes_PERCENTAGE_Score()

for t in range(0, len(lab6_Quiz)):
    print(lab6_Quiz[t], " ")

students = {}

for student in range(len(code_NUM)):
    if code_NUM[student] == "":
        continue

    students[code_NUM[student]] = {'Lab1_Quiz': lab1_Quiz[student],
                                   'Lab2_Quiz': lab2_Quiz[student],
                                   'Lab3_Quiz': lab3_Quiz[student],
                                   'Lab4_Quiz': lab4_Quiz[student],
                                   'Lab6_Quiz': lab6_Quiz[student],
                                   'lab_Quizes_PER_Score': lab_Quizes_PER_Score[student],
                                   }

pprint(students)
