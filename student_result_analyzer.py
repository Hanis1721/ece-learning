students = []

while True:
    print("\n===== Student Result Analyzer =====")
    print("1. Add Student")
    print("2. View Results")
    print("3. Find Topper")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Student Name: ")

        m1 = float(input("Maths Marks: "))
        m2 = float(input("Physics Marks: "))
        m3 = float(input("Programming Marks: "))

        average = (m1 + m2 + m3) / 3

        if average >= 90:
            grade = "A"
        elif average >= 75:
            grade = "B"
        elif average >= 60:
            grade = "C"
        else:
            grade = "D"

        students.append({
            "name": name,
            "average": average,
            "grade": grade
        })

        print("Student added successfully!")

    elif choice == "2":
        if not students:
            print("No student records found.")
        else:
            print("\nStudent Results:")
            for s in students:
                print(
                    f"Name: {s['name']} | Average: {s['average']:.2f} | Grade: {s['grade']}"
                )

    elif choice == "3":
        if not students:
            print("No records available.")
        else:
            topper = max(students, key=lambda x: x["average"])
            print("\nTopper Details")
            print(f"Name: {topper['name']}")
            print(f"Average: {topper['average']:.2f}")
            print(f"Grade: {topper['grade']}")

    elif choice == "4":
        print("Exiting Program...")
        break

    else:
        print("Invalid choice. Try again.")
