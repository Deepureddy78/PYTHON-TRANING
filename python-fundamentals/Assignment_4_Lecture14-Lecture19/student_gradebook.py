'''
5. Student Gradebook (Dictionaries + Classes)
Task: Manage grades using dictionaries & a class.
Input:
grades = {"Alice": {"Math": 90, "Science": 85}, "Bob": {"Math": 70, "Science": 95}}
Expected Output:
Alice GPA: 87.5
Bob GPA: 82.5
'''


class Student:
    def __init__(self, name):
        self.name = name
        self.subjects = {}
        print(f"object Student: {self.name} created")
        
    def __del__(self):
        print(f"object Student: {self.name} deleted")
        
    def add_subject_and_score(self, sub_name, sub_score):
        self.subjects[sub_name] = sub_score
        
    def calculate_cgpa(self):
        total = 0
        for sub, score in self.subjects.items():
            total += score
        percentage = total/(len(self.subjects)*100)*100
        self.cgpa = round(percentage,2)
        
    def __repr__(self):
        return f"{self.name} GPA: {self.cgpa}"

           
grades = {
    "Alice": {
        "Math": 90, 
        "Science": 85,
        "English": 78
    }, 
    "Bob": {
        "Math": 70, 
        "Science": 95
    }
}

for student, subjects in grades.items():
    s = Student(student)
    for subject, score in subjects.items():
        s.add_subject_and_score(subject, score)
    s.calculate_cgpa()
    print(s)          
    
'''
s = Student("Bob")
s.add_subject_and_score("Math", 70)
s.add_subject_and_score("Science", 95)
s.calculate_cgpa()
print(s) 
'''