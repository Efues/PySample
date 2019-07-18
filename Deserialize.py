import json
import Student

with open('student.json') as f:
    student = Student.Student(**json.loads(f.read()))

print(student.first_name)
print(student.last_name)
print(student.age)