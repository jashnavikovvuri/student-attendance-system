while True:

    print("\n===== STUDENT ATTENDANCE SYSTEM =====")
    print("1. Add Student Attendance")
    print("2. View Attendance")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "2":

        roll = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        status = input("Enter Attendance (Present/Absent): ")

        file = open("attendance.txt", "a")
        file.write(roll + "," + name + "," + status + "\n")
        file.close()

        print("Attendance Added Successfully")

    elif choice == "3":
        print("Thank You")
        break