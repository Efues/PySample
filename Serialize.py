import json
import Student

student = Student.Student(first_name="Jake", last_name="Doyle2", age = 20)

with open('student.json', mode='w') as f:
    f.write(json.dumps(student.__dict__))