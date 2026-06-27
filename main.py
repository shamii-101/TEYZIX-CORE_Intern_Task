import pandas as pd

df = pd.read_csv('data.csv', index_col=0)

choice = -1

while choice != 0:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. View First 3 Students")
    print("2. View Last 2 Students")
    print("3. Show Full Data")
    print("4. Add New Student")
    print("5. Update Student Marks")
    print("6. Delete Student")
    print("7. Performance Calculation")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    # ---------------- VIEW ----------------
    if choice == 1:
        print(df.head(3))

    elif choice == 2:
        print(df.tail(2))

    elif choice == 3:
        print(df)

    # ---------------- ADD ----------------
    elif choice == 4:
        print("Add New Student")

        sid = int(input("Enter ID: "))
        name = input("Enter Name: ")
        cls = int(input("Enter Class: "))
        math = int(input("Enter Math Marks: "))
        english = int(input("Enter English Marks: "))
        science = int(input("Enter Science Marks: "))

        df.loc[sid] = {
            "name": name,
            "class": cls,
            "math": math,
            "english": english,
            "science": science
        }

        df.to_csv('data.csv')
        print("Student added successfully!")

    # ---------------- UPDATE ----------------
    elif choice == 5:
        print("Update Student")

        sid = int(input("Enter Student ID: "))

        if sid in df.index:
            math = int(input("Enter new Math marks: "))
            english = int(input("Enter new English marks: "))
            science = int(input("Enter new Science marks: "))

            df.loc[sid, "math"] = math
            df.loc[sid, "english"] = english
            df.loc[sid, "science"] = science

            df.to_csv('data.csv')
            print("Student updated successfully!")

        else:
            print("Student not found!")

    # ---------------- DELETE ----------------
    elif choice == 6:
        print("Delete Student")

        sid = int(input("Enter Student ID: "))

        if sid in df.index:
            df = df.drop(sid)
            df.to_csv('data.csv')
            print("Student deleted successfully!")
        else:
            print("Student not found!")

    # ---------------- PERFORMANCE ----------------
    elif choice == 7:
        print("Performance Calculation")

        df["total"] = df["math"] + df["english"] + df["science"]
        df["average"] = df["total"] / 3
        df["percentage"] = (df["total"] / 300) * 100

        def grade(p):
            if p >= 80:
                return "A"
            elif p >= 70:
                return "B"
            elif p >= 60:
                return "C"
            else:
                return "Fail"

        df["grade"] = df["percentage"].apply(grade)

        print(df)

    # ---------------- EXIT ----------------
    elif choice == 0:
        print("Exiting program...")

    else:
        print("Invalid choice, try again!")