def show_menu():
    print("\n---TO-DO LIST---")
    print("1. view task")
    print("2. Add task")
    print("3. Remove task")
    print("4. exit")

tasks = []

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")
    if choice == "1":
        if not tasks:
            print("Your TO-DO LIST is empty")
        else:
            print("\nYour tasks:")
            for i,task in enumerate(tasks,start=1):
                print(f"{i}.{task}")              
    elif choice =="2":
        task = input("enter a new task: ")
        tasks.append(task)
        print("task added")
    elif choice == "3":
        if not tasks:
            print("No tasks to remove")
        else:
            for i,task in enumerate(tasks,start=1):
                print(f"{i}.{task}")
                index = int(input("enter task number to remove: ")) - 1
                if 0 <= index < len(tasks):
                    removed = tasks.pop(index)
                    print(f"removed:{removed}")
                else:
                    print("invalid task number")
    elif choice == "4":
        print("Goodbye!!!!") 
    else:
        print("invalid choice,please try again")              
        