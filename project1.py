#Feedback form 
def submit_feedback():
    employee_id=input("Enter your Employee id:")
    feedback= input("Enter your feedback:")

    with open(f"{employee_id}_feedback.txt","a") as feedback_file:
        feedback_file.write(feedback + "\n")
    print("Feedback submitted successfully!")

def view_feedback(employee_id):
    try:
        with open(f"{employee_id}_feedback.txt","r") as feedback_file:
            feedback_data = feedback_file.read()
            if feedback_data:
                print(f"Feedback for employee {employee_id}:")
                print(feedback_data)
            else:
                print(f"No feedback Found For Employee {employee_id}")
    except FileNotFoundError:
        print(f"No feedback Found For Employee {employee_id}")

while True:
    print("\nEmployee feedback system")
    print("1. Submit feedback")
    print("2. view feedback")
    print("3.Exit")

    choice = input("Enter your choice(1/2/3):")

    if choice == '1':
        submit_feedback()
    elif choice == '2':
        employee_id = input("Enter Employee ID to view feedback:")
        view_feedback(employee_id)
    elif choice=='3':
        print("Exiting the employee feedback system. \n Thank you for your valuable feedback.")
        break
    else:
        print("Invalid choice. please select 1,2, or 3.")
    
    #End the program
