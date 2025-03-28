studentID=[]
name=[]
english=[]
cLanguage=[]
python=[]
sum=[]
averageScore=[]
grade=[]
rank=[]
act = 0
studentNum = 5
def menu():
    print("========================================\n")
    print("1. print students Information\n2. insert students Information\n3. delete students Information\n4. search students Information\n5. sort list\n6. print num of students over 80 score\n7. Quit Program\n")
    print("========================================\n")
def inputValue():
    for i in range(studentNum):
        print(f"input {i + 1}'s student Information")
        studentID.append(int(input("Student ID :")))
        name.append(input("Student name :"))
        english.append(int(input("Student's english score :")))
        cLanguage.append(int(input("Student's C language score :")))
        python.append(int(input("Student's python score :")))
def calculateScore():
    for i in range(studentNum):
        sum.append(english[i] + cLanguage[i] + python[i])
        averageScore.append(sum[i] / studentNum)
def calculateGrade():
    for i in range(studentNum):
        if averageScore[i] > 90:
            grade.append("A")
        elif averageScore[i] > 80:
            grade.append("B")
        elif averageScore[i] > 70:
            grade.append("C")
        elif averageScore[i] > 60:
            grade.append("D")
        else:
            grade.append("E")
def calculateRank():
    temp = sorted(averageScore, reverse=True)
    for i, index in enumerate(temp):
        rank[index] = i + 1
def printAll():
    print("\n=====================================================")
    print("학번\t이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
    print("=====================================================")
    for i in range(studentNum):
        print(f"{studentID[i]}\t{name[i]}\t{english[i]}\t{cLanguage[i]}\t{python[i]}\t{sum[i]}\t{averageScore[i]:.2f}\t{grade[i]}\t{rank[i]}")
def insertValue(): 
    temp = int(input("input index :"))
def deleteValue():
    True
def searchValue(ID, studentName):
    for i in range(studentNum):
        if studentID[ID] == i:
            index = i
            break
        else:
            index = False
    if index != False:
        print(f"ID:{studentID[index]}, Name:{name[index]}, English:{english[index]}, C Language:{cLanguage[index]}, Python:{python[index]}, Total:{sum[index]}, Average:{averageScore[index]}, Grade:{grade[index]}, Rank:{rank[index]}\n")
    else:
        print("Wrong Information\n")
def sortList(sum):
    temp = sorted(sum)
    for i in range(studentNum):
        print(f"{temp[i]}\t")
    print("\n")
def count80Score():
    count
    for i in range(studentNum):
        if averageScore[i] >= 80:
            count+=1
    print(f"Num of Student Over 80 Scores : {count}\n")
inputValue()
while(True):
    menu()
    act = int(input("input num:"))
    if act == 7:
        break
    elif act == 1:
        printAll()
    elif act == 2:
        insertValue()
    elif act == 3:
        deleteValue()
    elif act == 4:
        searchValue(int(input("student ID:")), int(input("student Name:")))
    elif act == 5:
        sortList(sum)
    elif act == 6:
        count80Score()