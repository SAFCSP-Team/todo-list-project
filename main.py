def add_task(list , task):
    list.append(task)
def remove_task(remove_task , list):
    if remove_task in list:
        list.remove(remove_task)
        print("task removed")
    else:
        print("task not found")
def display(list):
        for task in list:
            print(task)



todo_list = []
while True:
    print("1. add task")
    print("2. remove task")
    print("3. display task")
    print("4. quit")
    choice = input("enter your choice from 1 to 4")

    if choice == "1":
        task1 = input("enter a task to add")
        add_task(todo_list , task1)
        print("task added")
    elif choice == "2":
        task2 = input("enter task to remove")
        remove_task(task2,todo_list )
    elif choice == "3":
        display(todo_list)
    elif choice == "4":
        print("Thank you for using the program. Goodbye!")
        break
    else:
        print( "Invalid choice. Please try again.")





