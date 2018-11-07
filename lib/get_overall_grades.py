import xlrd
import json


def usercodemath(uin, lastName):
    file_location = "C:\\Users\\Deepp\\PycharmProjects\\CS141_GradeLookup\\lib\\final template.xlsx"
    worksheet = xlrd.open_workbook(file_location).sheet_by_index(1)
    code_NUM = []

    for a in range(worksheet.nrows):
        code_NUM.append(worksheet.cell_value(a, 0))

    codeInt = (uin%1000) + (uin%10) + int((uin%1000000)/1000)

    lastName = lastName.upper()

    codeNUM = str(codeInt) + lastName[0] + lastName[1].lower()
    codeNUM2 = str(codeInt) + lastName[0]

    if codeNUM in code_NUM:
        return codeNUM
    elif codeNUM2 in code_NUM:
        return codeNUM2
    else:
        return None



def populate():
    file_location = "./lib/final template.xlsx"
    workbook = xlrd.open_workbook(file_location)

    worksheet = workbook.sheet_by_index(0)

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

    class_Avg_LabQuizes = 0
    class_Avg_labInClass = 0
    overall_ClassPER = 0
    zyante_ClassAvg = 0
    iClicker_AVG = 0

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

    # for loop to round the decimals
    for t in range(len(lab_Quizes_Avg)):
        if lab_Quizes_Avg[t] == "":
            continue
        lab_Quizes_Avg[t] = round((lab_Quizes_Avg[t]), 2)
        lab_Quizes_PER_Score[t] = round((lab_Quizes_PER_Score[t]), 1)
        lab_InClass_5PER_Score[t] = round((lab_InClass_5PER_Score[t]), 2)
        lab_inClass_Avg[t] = round((lab_inClass_Avg[t]), 2)
        program1[t] = round((program1[t]), 2)
        avg_4_All_Programs[t] = round((avg_4_All_Programs[t]), 2)
        programs_30PER_score[t] = round((programs_30PER_score[t]), 2)
        zyante_PER_Done[t] = round((zyante_PER_Done[t]), 2)
        zyante_10PER_score[t] = round((zyante_10PER_score[t]), 2)
        iClickers[t] = round((iClickers[t]), 2)
        iClickers_5PER_Score[t] = round((iClickers_5PER_Score[t]), 2)
        zyante_10PER_score[t] = round((zyante_10PER_score[t]), 2)
        midterm1_Total[t] = round((midterm1_Total[t]), 2)
        midterm1_10PER_Score[t] = round((midterm1_10PER_Score[t]), 2)
        midterm2_Total[t] = round((midterm2_Total[t]), 2)
        midterm2_15PER_Score[t] = round((midterm2_15PER_Score[t]), 2)
        final_Total[t] = round((final_Total[t]), 2)
        final_20PER_Score[t] = round((final_20PER_Score[t]), 2)
        overallPER_in_Class[t] = round((overallPER_in_Class[t]), 2)

        class_Avg_LabQuizes += lab_Quizes_Avg[t]
        class_Avg_labInClass += lab_inClass_Avg[t]
        overall_ClassPER += overallPER_in_Class[t]
        zyante_ClassAvg += zyante_PER_Done[t]
        iClicker_AVG += iClickers[t]

    class_Avg_LabQuizes = round((class_Avg_LabQuizes / nrows), 2)
    class_Avg_labInClass = round((class_Avg_labInClass / nrows), 2)
    overall_ClassPER = round((overall_ClassPER / nrows), 2)
    zyante_ClassAvg = round((zyante_ClassAvg / nrows), 2)
    iClicker_AVG = round((iClicker_AVG / nrows), 2)

    # define the dictionary
    students = {}

    # add vectors to the dictionary
    for student in range(len(code_NUM)):
        if code_NUM[student] == "":
            continue
        students[code_NUM[student]] = {
            'lab Quizes': {
                'lab1 Quiz': lab1_Quiz[student],
                'lab2 Quiz': lab2_Quiz[student],
                'lab3 Quiz': lab3_Quiz[student],
                'lab4 Quiz': lab4_Quiz[student],
                'lab6 Quiz': lab6_Quiz[student],
                'lab7 Quiz': lab7_Quiz[student],
                'lab8 Quiz': lab8_Quiz[student],
                'lab9 Quiz': lab9_Quiz[student],
                'lab11 Quiz': lab11_Quiz[student],
                'lab12 Quiz': lab12_Quiz[student],
                'lab13 Quiz': lab13_Quiz[student],
                'lab14 Quiz': lab14_Quiz[student],
                'lab Quizzes Avg': lab_Quizes_Avg[student],
                'lab Quizzes 5% Score': lab_Quizes_PER_Score[student],
                'class Avg -> LabQuizzes': class_Avg_LabQuizes,
            },
            'lab grades': {
                'lab1 inClass': lab1_inClass[student],
                'lab2 inClass': lab2_inClass[student],
                'lab3 inClass': lab3_inClass[student],
                'lab4 inClass': lab4_inClass[student],
                'lab6 inClass': lab6_inClass[student],
                'lab7 inClass': lab7_inClass[student],
                'lab8 inClass': lab8_inClass[student],
                'lab9 inClass': lab9_inClass[student],
                'lab11 inClass': lab11_inClass[student],
                'lab12 inClass': lab12_inClass[student],
                'lab13 inClass': lab13_inClass[student],
                'lab14 inClass': lab14_inClass[student],
                'labs InClass 5% Score': lab_InClass_5PER_Score[student],
                'labs inClass Avg': lab_inClass_Avg[student],
                'class Avg -> inClass Labs': class_Avg_labInClass,
            },
            'Programs': {
                'Program 1': program1[student],
                'Program 2': program2[student],
                'Program 3': program3[student],
                'Program 4': program4[student],
                'Program 5': program5[student],
                'Program 6': program6[student],
                'All programs Avg': avg_4_All_Programs[student],
                '30% of all Programs': programs_30PER_score[student],
            },
            'Zyante': {
                'Zyante % Done': zyante_PER_Done[student],
                '10% of Zyante % Done': zyante_10PER_score[student],
                'Class Avg -> Zyante completion': zyante_ClassAvg,
            },
            'iClickers': {
                'iClickers %': iClickers[student],
                '5% of iClickers': iClickers_5PER_Score[student],
                'Class Avg -> iClickers %': iClicker_AVG,
            },
            'Midterm 1': {
                'Midterm1 inClass': midterm1_inClass[student],
                'Midterm1 Lab': midterm1_Lab[student],
                'Midterm1 Total %': midterm1_Total[student],
                '10% of Midterm1': midterm1_10PER_Score[student],
            },
            'Midterm 2': {
                'Midterm2 inClass': midterm2_inClass[student],
                'Midterm2 Lab': midterm2_Lab[student],
                'Midterm2 Total %': midterm2_Total[student],
                '15% of Midterm2': midterm2_15PER_Score[student],
            },
            'Final': {
                'Final inClass': final_inClass[student],
                'Final Lab': final_Lab[student],
                'Final Total': final_Total[student],
                '20% of Final': final_20PER_Score[student],
            },
            'Overall Grade': {
                'Overall % in class': overallPER_in_Class[student],
                'Final grade in class': final_grade_inClass[student],
                'Class Avg -> Overall %': overall_ClassPER,
            }
        }

    cs141grade = json.dumps(students)

    return cs141grade


print(usercodemath(662500522, "Tdonkelberry"))