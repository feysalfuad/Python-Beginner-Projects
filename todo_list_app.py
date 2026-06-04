print("📝 Welcome to To-Do list App")

tasks = []

while True:
    print("\nWhat would you like to do?")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Done")
    print("5. Exit")
    
    choice = input("Choose 1-5: ").strip()

    # ADD TASK
    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append({"task": task, "done": False})
        print("✅ Task added!")

    # VIEW TASKS
    elif choice == "2":
        print("\n📋 Your tasks:")

        if not tasks:
            print("No tasks yet.")
        else:
            for i in range(len(tasks)):
                status = "✔" if tasks[i]["done"] else " "
                print(f"{i + 1}. [{status}] {tasks[i]['task']}")

    # DELETE TASK
    elif choice == "3":
        if not tasks:
            print("❌ No tasks to delete.")
        else:
            print("\n📋 Select a task to delete:")
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]['task']}")

            try:
                task_number = int(input("Enter task number: "))
                if 1 <= task_number <= len(tasks):
                    removed = tasks.pop(task_number - 1)
                    print(f"🗑 Task deleted: {removed['task']}")
                else:
                    print("❌ Invalid task number.")
            except:
                print("❌ Please enter a valid number.")

    # MARK AS DONE
    elif choice == "4":
        if not tasks:
            print("❌ No tasks to mark as done.")
        else:
            print("\n📋 Select a task to mark as done:")

            for i in range(len(tasks)):
                status = "✔" if tasks[i]["done"] else " "
                print(f"{i + 1}. [{status}] {tasks[i]['task']}")

            try:
                task_number = int(input("Enter task number: "))
                if 1 <= task_number <= len(tasks):
                    tasks[task_number - 1]["done"] = True
                    print("✅ Task marked as done!")
                else:
                    print("❌ Invalid task number.")
            except:
                print("❌ Please enter a valid number.")

    # EXIT
    elif choice == "5":
        print("👋 Goodbye!")
        break

    else:
        print("❌ Invalid choice. Try again.")
