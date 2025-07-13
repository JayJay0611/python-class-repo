def main():
    students = {}

    students["Jim"] = {
        "id": 1,
        "gpa": 3.1,
        "credits-completed": 97.0,
        "grades": [80, 50, 100, 98]
    }

    students["Sarah"] = {
        "id": 2,
        "gpa": 3.6,
        "credits-completed": 40.0,
        "grades": [80, 98]
    }

    print("All student information:")
    print(students)
    print()

    print("List of Students")
    for name in students:
        print(name)
    print()

    print("Student Information")
    print("Student\tID\tGPA\tCredits Completed\tGrades")
    for name, info in students.items():
        print(f"{name}\t{info['id']}\t{info['gpa']}\t{info['credits-completed']}\t\t\t{info['grades']}")
    print()

    print("Accessing Student Information Using the Key in a Loop")
    for name in students:
        print(name, students[name])
    print()

    removed_student = students.pop("Sarah", None)
    if removed_student:
        print("Sarah has dropped out, removing from student info registry")
    print(students)
    print()

    print("Getting Jim's GPA")
    print(students["Jim"]["gpa"])
    print()

    print("Students have graduated, clearing the student registry")
    students.clear()
    print(students)

    print("Completed by, Jonathan Jewell")

if __name__ == "__main__":
    main()