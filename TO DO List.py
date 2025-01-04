TASK_DATA = []

def add_task(task):
    TASK_DATA.append(task)
    print (f"'{task}'' Task added Successfully\n")

def remove_task(task):
    TASK_DATA.remove(task)
    print (f"'{task}'' Task removed Successfully\n")

def show_task(task):
    for i, item in enumerate(task, start=1):
        print (f"{i} - {item}")
    print ("\n")
    
print ("*** TODO List ***")
print ("""Enter '1' to Add Task
Enter '2' to Remove Task
Enter '3' to Show Task
Enter '4' to Exit
""")

def TODO_Function():
    while True:
        user_input = input("Enter input: ")
        
        if user_input == '1':
            Add_Task = input("Enter task to Add: ")
            add_task(Add_Task)
            
        elif user_input == '2':
            if not TASK_DATA:
                print ("No task. Enter '1' to Add Task.\n")
            else:
                show_task(TASK_DATA)
                Remove_Task = int(input("Enter the number of the task to remove: "))
                remove_task(TASK_DATA[Remove_Task-1])
    
        elif user_input == '3':
            if not TASK_DATA:
                print ("No task. Enter '1' to Add Task.\n")
            else:
                show_task(TASK_DATA)
        
        elif user_input == '4':
            print ("Exiting TODO List. Thank You for Using")
            break
                
        else:
            print ("Enter a valid input.")

if __name__ == "__main__":
    TODO_Function()
