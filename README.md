# To-do List Project

### Objective
In this project, our main goal is to create a project that combines control flow, functions, and lists, to make sure can pass the first part of Python 101.

### Problem
create a program that allows the user to manage a simple to-do list. It includes functions like adding, removing, and displaying tasks.


### Implementation
- Write a function `add_task` to add a task to the list. The function takes the list and the new task as input.
- Write a function `remove_task` to remove a task from the list. The function takes the list and the task as input، If the task is found and successfully removed, it should print "Task removed." If the task is not found in the list, it should print "Task not found."
- Write a function `display` to print all the tasks in the list. Using the for loop.
- Create an empty list called `todo_list`.
- Implement a `while` loop that continues until the user chooses to quit the program.
- Inside the loop, display a menu with the following options:
    - "1. Add task"
    - "2. Remove task"
    - "3. Display tasks"
    - "4. Quit"
- Based on the user's choice, perform the following actions:
    - If the choice is '1', ask the user to enter a task and call the `add_task()` function.
    - If the choice is '2', ask the user to enter a task to remove and call the `remove_task()` function.
    - If the choice is '3', call the `display()` function.
    - If the choice is '4', print "Thank you for using the program. Goodbye!" and break out of the loop.
    - If the user enters an invalid choice, print "Invalid choice. Please try again."

