tasks = []

while True:
    print("\n----- TO-DO LIST -----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("No tasks found.")
        else:
            for i, task in enumerate(tasks, 1):
                print(i, task)

    elif choice == "3":
        num = int(input("Enter task number: "))
        new_task = input("Enter new task: ")
        tasks[num - 1] = new_task
        print("Task updated!")

    elif choice == "4":
        num = int(input("Enter task number: "))
        tasks.pop(num - 1)
        print("Task deleted!")

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")