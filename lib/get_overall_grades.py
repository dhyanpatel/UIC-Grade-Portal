import xlrd
from pprint import pprint
import json

def dictionary():
    file_location = "C:\\Users\\Deepp\\PycharmProjects\\CS141_GradeLookup\\lib\\final template.xlsx"
    workbook = xlrd.open_workbook(file_location)

    sheets = workbook.nsheets

    worksheet = workbook.sheet_by_index(1)

    nrows = worksheet.nrows
    ncols = worksheet.ncols

    code_NUM = []
    lab1_Quiz = []
    lab2_Quiz = []
    lab3_Quiz = []
    lab4_Quiz = []
    lab6_Quiz = []
    lab7_Quiz = []
    lab8_Quiz = []
    lab9_Quiz = []
    lab11_Quiz = []
    lab12_Quiz = []
    lab13_Quiz = []
    lab14_Quiz = []
    lab_Quizes_PER_Score = []
    lab_Quizes_Avg = []

    lab1_inClass = []
    lab2_inClass = []
    lab3_inClass = []
    lab4_inClass = []
    lab6_inClass = []
    lab7_inClass = []
    lab8_inClass = []
    lab9_inClass = []
    lab11_inClass = []
    lab12_inClass = []
    lab13_inClass = []
    lab14_inClass = []
    lab_inClass_Avg = []
    lab_InClass_5PER_Score = []

    program1 = []
    program2 = []
    program3 = []
    program4 = []
    program5 = []
    program6 = []
    avg_4_All_Programs = []
    programs_30PER_score = []

    zyante_PER_Done = []
    zyante_10PER_score = []

    iClickers = []
    iClickers_5PER_Score = []

    midterm1_inClass = []
    midterm1_Lab = []
    midterm1_Total = []
    midterm1_10PER_Score = []

    midterm2_inClass = []
    midterm2_Lab = []
    midterm2_Total = []
    midterm2_15PER_Score = []

    final_inClass = []
    final_Lab = []
    final_Total = []
    final_20PER_Score = []

    overallPER_in_Class = []
    final_grade_inClass = []

    for a in range(8, worksheet.nrows):
        code_NUM.append(worksheet.cell_value(a, 0))
        lab1_Quiz.append(worksheet.cell_value(a, 1))
        lab2_Quiz.append(worksheet.cell_value(a, 2))
        lab3_Quiz.append(worksheet.cell_value(a, 3))
        lab4_Quiz.append(worksheet.cell_value(a, 4))
        lab6_Quiz.append(worksheet.cell_value(a, 5))
        lab7_Quiz.append(worksheet.cell_value(a, 6))
        lab8_Quiz.append(worksheet.cell_value(a, 7))
        lab9_Quiz.append(worksheet.cell_value(a, 8))
        lab11_Quiz.append(worksheet.cell_value(a, 9))
        lab12_Quiz.append(worksheet.cell_value(a, 10))
        lab13_Quiz.append(worksheet.cell_value(a, 11))
        lab14_Quiz.append(worksheet.cell_value(a, 12))

    for t in range(worksheet.nrows):
        row = worksheet.row(t)
        for d, cell in enumerate(row):
            if cell.value == "Quiz":
                for a in range(8, worksheet.nrows):
                    lab_Quizes_PER_Score.append(worksheet.cell_value(a, d))
                    lab_Quizes_Avg.append(worksheet.cell_value(a, d - 1))
                    lab1_inClass.append(worksheet.cell_value(a, d + 1))
                    lab2_inClass.append(worksheet.cell_value(a, d + 2))
                    lab3_inClass.append(worksheet.cell_value(a, d + 3))
                    lab4_inClass.append(worksheet.cell_value(a, d + 4))
                    lab6_inClass.append(worksheet.cell_value(a, d + 5))
                    lab7_inClass.append(worksheet.cell_value(a, d + 6))
                    lab8_inClass.append(worksheet.cell_value(a, d + 7))
                    lab9_inClass.append(worksheet.cell_value(a, d + 8))
                    lab11_inClass.append(worksheet.cell_value(a, d + 9))
                    lab12_inClass.append(worksheet.cell_value(a, d + 10))
                    lab13_inClass.append(worksheet.cell_value(a, d + 11))
                    lab14_inClass.append(worksheet.cell_value(a, d + 12))

    for s in range(worksheet.nrows):
        row = worksheet.row(s)
        for t, cell in enumerate(row):
            if cell.value == "Lab":
                for j in range(8, worksheet.nrows):
                    lab_InClass_5PER_Score.append(worksheet.cell_value(j, t))
                    lab_inClass_Avg.append(worksheet.cell_value(j, t - 1))
                    program1.append(worksheet.cell_value(j, t + 1))
                    program2.append(worksheet.cell_value(j, t + 2))
                    program3.append(worksheet.cell_value(j, t + 3))
                    program4.append(worksheet.cell_value(j, t + 4))

    for n in range(worksheet.nrows):
        row = worksheet.row(n)
        for q, cell in enumerate(row):
            if cell.value == "Prog":
                for b in range(8, worksheet.nrows):
                    program5.append(worksheet.cell_value(b, q - 3))
                    program6.append(worksheet.cell_value(b, q - 2))
                    avg_4_All_Programs.append(worksheet.cell_value(b, q - 1))
                    programs_30PER_score.append(worksheet.cell_value(b, q))
                    zyante_PER_Done.append(worksheet.cell_value(b, q + 1))
                    zyante_10PER_score.append(worksheet.cell_value(b, q + 2))
                    iClickers.append(worksheet.cell_value(b, q + 3) * 100)
                    iClickers_5PER_Score.append(worksheet.cell_value(b, q + 4))

    for e in range(worksheet.nrows):
        row = worksheet.row(e)
        for v, cell in enumerate(row):
            if cell.value == "Mid1":
                for u in range(8, worksheet.nrows):
                    midterm1_inClass.append(worksheet.cell_value(u, v))
                    midterm1_Lab.append(worksheet.cell_value(u, v + 1))
                    midterm1_Total.append(worksheet.cell_value(u, v + 2))
                    midterm1_10PER_Score.append(worksheet.cell_value(u, v + 3))

    for f in range(worksheet.nrows):
        row = worksheet.row(f)
        for z, cell in enumerate(row):
            if cell.value == "Mid2":
                for u in range(8, worksheet.nrows):
                    midterm2_inClass.append(worksheet.cell_value(u, z))
                    midterm2_Lab.append(worksheet.cell_value(u, z + 1))
                    midterm2_Total.append(worksheet.cell_value(u, z + 2))
                    midterm2_15PER_Score.append(worksheet.cell_value(u, z + 3))

    for k in range(worksheet.nrows):
        row = worksheet.row(k)
        for r, cell in enumerate(row):
            if cell.value == "Final":
                for u in range(8, worksheet.nrows):
                    final_inClass.append(worksheet.cell_value(u, r))
                    final_Lab.append(worksheet.cell_value(u, r + 1))
                    final_Total.append(worksheet.cell_value(u, r + 2))
                    final_20PER_Score.append(worksheet.cell_value(u, r + 3))

    for k in range(worksheet.nrows):
        row = worksheet.row(k)
        for r, cell in enumerate(row):
            if cell.value == "Overall":
                for u in range(8, worksheet.nrows):
                    overallPER_in_Class.append(worksheet.cell_value(u, r))
                    final_grade_inClass.append(worksheet.cell_value(u, r + 1))

    students = {}

    for student in range(len(code_NUM)):
        if code_NUM[student] == "":
            continue

        students[code_NUM[student]] = {'Lab1_Quiz': lab1_Quiz[student],
                                       'Lab2_Quiz': lab2_Quiz[student],
                                       'Lab3_Quiz': lab3_Quiz[student],
                                       'Lab4_Quiz': lab4_Quiz[student],
                                       'Lab6_Quiz': lab6_Quiz[student],
                                       'Lab7_Quiz': lab7_Quiz[student],
                                       'Lab8_Quiz': lab8_Quiz[student],
                                       'lab9_Quiz': lab9_Quiz[student],
                                       'lab11_Quiz': lab11_Quiz[student],
                                       'lab12_Quiz': lab12_Quiz[student],
                                       'lab13_Quiz': lab13_Quiz[student],
                                       'lab14_Quiz': lab14_Quiz[student],
                                       'lab_Quizes_5%_Score': lab_Quizes_PER_Score[student],
                                       'lab_Quizes_Avg': lab_Quizes_Avg[student],
                                       'lab1_inClass': lab1_inClass[student],
                                       'lab2_inClass': lab2_inClass[student],
                                       'lab3_inClass': lab3_inClass[student],
                                       'lab4_inClass': lab4_inClass[student],
                                       'lab6_inClass': lab6_inClass[student],
                                       'lab7_inClass': lab7_inClass[student],
                                       'lab8_inClass': lab8_inClass[student],
                                       'lab9_inClass': lab8_inClass[student],
                                       'lab11_inClass': lab8_inClass[student],
                                       'lab12_inClass': lab8_inClass[student],
                                       'lab13_inClass': lab8_inClass[student],
                                       'lab14_inClass': lab8_inClass[student],
                                       'lab_InClass_5%_Score': lab_InClass_5PER_Score[student],
                                       'lab_inClass_Avg': lab_inClass_Avg[student],
                                       'program1': program1[student],
                                       'program2': program2[student],
                                       'program3': program3[student],
                                       'program4': program4[student],
                                       'program5': program5[student],
                                       'program6': program6[student],
                                       'avg_4_All_Programs': avg_4_All_Programs[student],
                                       'programs_30%_score': programs_30PER_score[student],
                                       'zyante_%_Done': zyante_PER_Done[student],
                                       'zyante_10%_score': zyante_10PER_score[student],
                                       'iClickers': iClickers[student],
                                       'iClickers_5%_Score': iClickers_5PER_Score[student],
                                       'midterm1_inClass': midterm1_inClass[student],
                                       'midterm1_Lab': midterm1_Lab[student],
                                       'midterm1_Total': midterm1_Total[student],
                                       'midterm1_10%_Score': midterm1_10PER_Score[student],
                                       'midterm2_inClass': midterm2_inClass[student],
                                       'midterm2_Lab': midterm2_Lab[student],
                                       'midterm2_Total': midterm2_Total[student],
                                       'midterm2_15%_Score': midterm2_15PER_Score[student],
                                       'final_inClass': final_inClass[student],
                                       'final_Lab': final_Lab[student],
                                       'final_Total': final_Total[student],
                                       'final_20%_Score': final_20PER_Score[student],
                                       'overall%_in_Class': overallPER_in_Class[student],
                                       'final_grade_inClass': final_grade_inClass[student],
                                       }

    pprint(students)
    cs141grade = json.dumps(students)

    return cs141grade




