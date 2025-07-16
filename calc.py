def calculate_average_grade():
    print("Student Grade Average Calculator")

    while True:
        try:
            num_subjects = int(input("Enter the number of subjects: "))
            if num_subjects <= 0:
                print("Number of subjects must be greater than zero.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    total = 0
    for i in range(1, num_subjects + 1):
        while True:
            try:
                grade = float(input(f"Enter the grade for subject {i}: "))
                if grade < 0 or grade > 100:
                    print("Please enter a grade between 0 and 100.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        total += grade

    average = total / num_subjects

    print(f"\nYour average grade is: {average:.2f}")

    if average >= 90:
        print("Your grade is: A")
    elif average >= 80:
        print("Your grade is: B")
    elif average >= 70:
        print("Your grade is: C")
    elif average >= 60:
        print("Your grade is: D")
    else:
        print("Your grade is: F")