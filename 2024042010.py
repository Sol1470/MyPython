class Student:
    def __init__(self):
        self.eng = 0
        self.cLan = 0
        self.py = 0
        self.sum = 0
        self.avg = 0
        self.grade = ''
        self.name = 0
    def subInput(self, name):
        try:
            self.eng = int(input("영어 성적: "))
            self.cLan = int(input("C언어 성적: "))
            self.py = int(input("파이썬 성적: "))
            self.name = name
        except ValueError:
            print("숫자로 입력하세요!")
            return
        
        self.calcScore()
        self.calcGrade()

    def calcScore(self):
        self.sum = self.eng + self.cLan + self.py
        self.avg = self.sum / 3

    def calcGrade(self):
        if self.avg > 80:
            self.grade = 'A'
        elif self.avg > 60:
            self.grade = 'B'
        else:
            self.grade = 'C'

    def displayInfo(self, rank):
        print(f"{rank}위 | {self.name} | 총점: {self.sum} | 평균: {self.avg:.2f} | 학점: {self.grade}")

students = [Student() for i in range(5)]
for i in range(5):
    print(f"{i+1}번째 학생")
    students[i].subInput(i+1)

students.sort(key=lambda x: x.avg, reverse=True)

for rank, student in enumerate(students, start=1):
    student.displayInfo(rank)