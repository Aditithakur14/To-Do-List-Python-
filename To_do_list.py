tasks = []

def menu():
    print("\n--- TO DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added!")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks yet.")
    else:
        print("\nYour Tasks:")
        for i in range(len(tasks)):
            print(i+1, ".", tasks[i])

def delete_task():
    view_tasks()
    if len(tasks) == 0:
        return

    num = int(input("Enter task number to delete: "))
    if num >= 1 and num <= len(tasks):
        tasks.pop(num - 1)
        print("Task deleted!")
    else:
        print("Invalid number")

while True:
    menu()
    choice = input("Enter choice (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Bye 👋")
        break
    else:
        print("Wrong choice, try again")
