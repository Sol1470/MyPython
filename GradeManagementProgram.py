  ##################

  #프로그램명: 성적관리 프로그램

  #작성자자: 소프트웨어학부 / 하윤승승

  #작성일: 2025-04-12

  #프로그램 설명: 5명의 학생의 3개의 교과목(영어, C-언어, 파이썬)에 대하여 키보드로 학번, 이름, 각 과목의 점수를 입력을 받는다.
  #이후 총점, 평균, 학점, 등수를 계산하는 프로그램.

  ###################
class Student:
    def __init__(self, studentID, name, english, cLanguage, python):
        self.studentID = studentID
        self.name = name
        self.english = english
        self.cLanguage = cLanguage
        self.python = python
        self.sum = english + cLanguage + python
        self.averageScore = self.sum / 3
        self.grade = self.calculateGrade()
        self.rank = 1

    def calculateGrade(self):
        if self.averageScore >= 90:
            return 'A'
        elif self.averageScore >= 80:
            return 'B'
        elif self.averageScore >= 70:
            return 'C'
        elif self.averageScore >= 60:
            return 'D'
        else:
            return 'E'

    def __str__(self):
        return f"{self.studentID}\t{self.name}\t{self.english}\t{self.cLanguage}\t{self.python}\t{self.sum}\t{self.averageScore:.2f}\t{self.grade}\t{self.rank}"


class GradeManager:
    def __init__(self):
        self.studentList = []
        self.studentNum = 0

    def inputValue(self):
        for i in range(5):
            print(f"\ninput {i + 1}'s student Information")
            student = self.createStudent()
            self.studentList.append(student)
            self.studentNum += 1
        self.calculateRank()

    def createStudent(self):
        studentID = int(input("Student ID: "))
        name = input("Student name: ")
        english = int(input("Student's English score: "))
        cLanguage = int(input("Student's C Language score: "))
        python = int(input("Student's Python score: "))
        return Student(studentID, name, english, cLanguage, python)

    def printAll(self):
        print("\n=====================================================")
        print("학번\t이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
        print("=====================================================")
        for s in self.studentList:
            print(s)

    def insertValue(self):
        print("\nInsert new student information")
        student = self.createStudent()
        self.studentList.append(student)
        self.studentNum += 1
        self.calculateRank()

    def deleteValue(self):
        del_id = int(input("Enter the student ID to delete: "))
        found = False
        for i, s in enumerate(self.studentList):
            if s.studentID == del_id:
                del self.studentList[i]
                self.studentNum -= 1
                found = True
                print("Deleted successfully.\n")
                break
        if not found:
            print("Student ID not found.\n")
        self.calculateRank()

    def searchValue(self, search_id=None, search_name=None):
        for s in self.studentList:
            if (search_id is not None and s.studentID == search_id) or \
               (search_name is not None and s.name == search_name):
                print(f"ID:{s.studentID}, Name:{s.name}, English:{s.english}, C Language:{s.cLanguage}, Python:{s.python}, Total:{s.sum}, Average:{s.averageScore:.2f}, Grade:{s.grade}, Rank:{s.rank}\n")
                return
        print("Wrong Information\n")

    def sortList(self):
        self.studentList.sort(key=lambda s: s.sum, reverse=True)
        print("\nSorted by total score:")
        for s in self.studentList:
            print(f"{s.sum}\t")
        print("\n")
        self.calculateRank()

    def count80Score(self):
        count = 0
        for s in self.studentList:
            if s.averageScore >= 80:
                count += 1
        print(f"Num of Student Over 80 Scores : {count}\n")

    def calculateRank(self):
        for s in self.studentList:
            s.rank = 1
        for i in range(self.studentNum):
            for j in range(self.studentNum):
                if self.studentList[i].sum < self.studentList[j].sum:
                    self.studentList[i].rank += 1

    def menu(self):
        while True:
            print("========================================\n")
            print("1. print students Information")
            print("2. insert students Information")
            print("3. delete students Information")
            print("4. search students Information")
            print("5. sort list")
            print("6. print num of students over 80 score")
            print("7. Quit Program")
            print("========================================\n")

            act = input("input num: ")
            if act == '1':
                self.printAll()
            elif act == '2':
                self.insertValue()
            elif act == '3':
                self.deleteValue()
            elif act == '4':
                mode = input("Search by (1) ID or (2) Name? ")
                if mode == '1':
                    sid = int(input("Enter student ID: "))
                    self.searchValue(search_id=sid)
                elif mode == '2':
                    sname = input("Enter student Name: ")
                    self.searchValue(search_name=sname)
                else:
                    print("Invalid choice")
            elif act == '5':
                self.sortList()
            elif act == '6':
                self.count80Score()
            elif act == '7':
                print("Exiting...")
                break
            else:
                print("Invalid input.\n")


def main():
    gm = GradeManager()
    gm.inputValue()
    gm.menu()

if __name__ == "__main__":
    main()
