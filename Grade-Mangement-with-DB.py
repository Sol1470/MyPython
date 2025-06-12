import sqlite3

class Student:
    def __init__(self, studentID, name, english, cLanguage, python, total=None, average=None, grade=None, rank=1):
        self.studentID = studentID
        self.name = name
        self.english = english
        self.cLanguage = cLanguage
        self.python = python
        self.sum = total if total is not None else english + cLanguage + python
        self.averageScore = average if average is not None else self.sum / 3
        self.grade = grade if grade is not None else self.calculateGrade()
        self.rank = rank

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

class GradeManager:
    def __init__(self):
        self.conn = sqlite3.connect("grades.db")
        self.cursor = self.conn.cursor()
        self.createTable()

    def createTable(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                studentID INTEGER PRIMARY KEY,
                name TEXT,
                english INTEGER,
                cLanguage INTEGER,
                python INTEGER,
                total INTEGER,
                average REAL,
                grade TEXT,
                rank INTEGER
            )
        ''')
        self.conn.commit()

    def inputValue(self):
        for i in range(5):
            print(f"\ninput {i + 1}'s student Information")
            student = self.createStudent()
            self.insertToDB(student)
        self.calculateRank()

    def createStudent(self):
        studentID = int(input("Student ID: "))
        name = input("Student name: ")
        english = int(input("English score: "))
        cLanguage = int(input("C Language score: "))
        python = int(input("Python score: "))
        return Student(studentID, name, english, cLanguage, python)

    def insertToDB(self, student):
        self.cursor.execute('''
            INSERT INTO students VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (student.studentID, student.name, student.english, student.cLanguage,
              student.python, student.sum, student.averageScore, student.grade, student.rank))
        self.conn.commit()

    def printAll(self):
        print("\n=====================================================")
        print("학번\t이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
        print("=====================================================")
        for row in self.cursor.execute("SELECT * FROM students ORDER BY rank"):
            print("\t".join(str(x) for x in row))

    def insertValue(self):
        print("\nInsert new student information")
        student = self.createStudent()
        self.insertToDB(student)
        self.calculateRank()

    def deleteValue(self):
        del_id = int(input("Enter the student ID to delete: "))
        self.cursor.execute("DELETE FROM students WHERE studentID=?", (del_id,))
        self.conn.commit()
        print("Deleted successfully.\n")
        self.calculateRank()

    def searchValue(self, search_id=None, search_name=None):
        if search_id is not None:
            self.cursor.execute("SELECT * FROM students WHERE studentID=?", (search_id,))
        elif search_name is not None:
            self.cursor.execute("SELECT * FROM students WHERE name=?", (search_name,))
        result = self.cursor.fetchone()
        if result:
            print("학번:", result[0], "이름:", result[1], "영어:", result[2],
                  "C:", result[3], "파이썬:", result[4], "총점:", result[5],
                  "평균:", f"{result[6]:.2f}", "학점:", result[7], "등수:", result[8])
        else:
            print("Student not found.\n")

    def sortList(self):
        print("\nSorted by total score:")
        for row in self.cursor.execute("SELECT * FROM students ORDER BY total DESC"):
            print(row[5])  # total 점수만 출력
        self.calculateRank()

    def count80Score(self):
        self.cursor.execute("SELECT COUNT(*) FROM students WHERE average >= 80")
        count = self.cursor.fetchone()[0]
        print(f"Num of Student Over 80 Scores : {count}\n")

    def calculateRank(self):
        self.cursor.execute("SELECT studentID, total FROM students ORDER BY total DESC")
        students = self.cursor.fetchall()
        rank = 1
        for i, (studentID, _) in enumerate(students):
            self.cursor.execute("UPDATE students SET rank=? WHERE studentID=?", (rank, studentID))
            rank += 1
        self.conn.commit()

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
