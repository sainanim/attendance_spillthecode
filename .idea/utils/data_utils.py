import json
from student import Student

def save_data(students, filename="data/students.json"):
    data = {}
    for name, student in students.items():
        data[name] = {
            "dates_attended": student.dates_attended,
            "fees_rate": student.fees_rate,
            "fees_paid": student.fees_paid,
            "fees_status": student.fees_status,
            "credit_classes": student.credit_classes
        }
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def load_data(filename="data/students.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        return {}
    students = {}
    for name, info in data.items():
        s = Student(name, info["fees_rate"])
        s.dates_attended = info["dates_attended"]
        s.fees_paid = info["fees_paid"]
        s.fees_status = info["fees_status"]
        s.credit_classes = info.get("credit_classes", 0)
        students[name] = s
    return students
