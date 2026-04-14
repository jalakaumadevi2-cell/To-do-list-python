# To-Do List Application

def show_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def workload_status(tasks):
    n = len(tasks)
    if n <= 3:
        return "Light"
    elif n <= 6:
        return "Moderate"
    else:
        return "Heavy"

tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully!")
    
    elif choice == 2:
        show_tasks(tasks)
        print("Workload Status:", workload_status(tasks))
    
    elif choice == 3:
        show_tasks(tasks)
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Task '{removed}' deleted.")
        else:
            print("Invalid task number!")
    
    elif choice == 4:
        print("Exiting program...")
        break
    
    else:
        print("Invalid choice! Try again.")
