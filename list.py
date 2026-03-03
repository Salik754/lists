student_names = []
student_grades = []

def create_course()-> str:
    return input("Enter course name: ").strip().title()

def add_student():
    # FIXED: Changed .stript() to .strip()
    name = input("Enter student name: ").strip().title()
    grade = int(input("Enter student percentage: ").strip())

    student_names.append(name)
    student_grades.append(grade)

def update_grade():
    name = input("Enter student name to update: ").strip().title()

    if name in student_names:
        index = student_names.index(name)
        # FIXED: Changed .stript() to .strip()
        new_grade = int(input(f"Enter new grade for {name}: ").strip())
        student_grades[index] = new_grade
    else:
        print("No student by that name.")

def remove_student():
    name = input("Which student do you want to remove? ").strip().title()
    
    if name in student_names:
        index = student_names.index(name)
        student_names.pop(index)
        student_grades.pop(index) # FIXED: Removed space before .pop
        print("Student removed.")
    else:
        print("There are no students by that name.")

def show_roster():
    if not student_names:
        print("No students in course")
        return
    print("\nClass Roster")
    for i in range(len(student_names)):
        print(student_names[i], " - ", student_grades[i])

def show_statistics():
    if not student_names:
        print("No students in course")
        return

    average = sum(student_grades) / len(student_grades)
    print("\nClass Statistics")
    print("Average Grade:", round(average, 2))
    print("Highest Grade:", max(student_grades))
    print("Lowest Grade:", min(student_grades))

def main():
    course_name = create_course()
    print(f"\nWelcome to {course_name}!")
    
    while True:
        print("\n1. Add student")
        print("2. Update grade")
        print("3. Remove student")
        print("4. Show roster")
        print("5. Show statistics")
        print("6. Exit")
        
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            update_grade()
        elif choice == "3":
            remove_student()
        elif choice == "4":
            show_roster()
        elif choice == "5":
            show_statistics()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
