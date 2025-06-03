# todo_list.py

todo_list = []

def show_menu():
    print("\n--- To-Do List ---")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

def show_tasks():
    if not todo_list:
        print("No tasks yet!")
    else:
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ")
    todo_list.append(task)
    print("Task added!")

def remove_task():
    show_tasks()
    try:
        task_num = int(input("Enter the task number to remove: "))
        removed = todo_list.pop(task_num - 1)
        print(f"Removed task: {removed}")
    except (IndexError, ValueError):
        print("Invalid task number!")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == '1':
        show_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
