studentID = []
name = []
english = []
clanguage = []
python = []
total = []
avr = []
grade = []
rank = []

def Input():
    for i in range(5):
        studentID.append(int(input("학번: ")))
        name.append(input("이름: "))
        english.append(int(input("영어: ")))
        clanguage.append(int(input("C-언어: ")))
        python.append(int(input("파이썬: ")))

def calcScore():
    for i in range(5):
        t = english[i] + clanguage[i] + python[i]
        a = t / 3
        total.append(t)
        avr.append(a)

def calcGrade():
    for i in range(5):
        if avr[i] >= 90:
            grade.append('A')
        elif avr[i] >= 80:
            grade.append('B')
        elif avr[i] >= 70:
            grade.append('C')
        else:
            grade.append('D')

def calcRank():
    temp = sorted(avr, reverse=True)
    for i in range(5):
        for j in range(5):
            if temp[j] == avr[i]:
                rank.append(j + 1)


def printInformation():
    print("\n=====================================================")
    print("학번\t이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
    print("=====================================================")
    for i in range(5):
        print(f"{studentID[i]}\t{name[i]}\t{english[i]}\t{clanguage[i]}\t{python[i]}\t{total[i]}\t{avr[i]:.2f}\t{grade[i]}\t{rank[i]}")

Input()
calcScore()
calcGrade()
calcRank()
printInformation()