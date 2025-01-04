TASK_DATA = []

def add_task(task):
    TASK_DATA.append(task)

print ("*** TODO List ***")
print ("""Enter '1' to Add Task
Enter '2' to Remove Task
Enter '3' to Show Task
Enter '4' to Edit Task
Enter '5' to Exit
""")

while True:
    user_input = input("Enter input: ")
    if user_input == '1':
        Add_Task = input("Enter task to Add: ")
        add_task(Add_Task)
        print (f"'{Add_Task}'' Task added Successfully")
        
    elif user_input == '2':
        if not TASK_DATA:
            print ("First Add a Task")
        else:
            print (TASK_DATA)
            Remove_Task = input("Enter a Task To Remove")
    elif user_input == '3':
        print ("Show Task")
    elif user_input == '4':
        print ("Edit Task")
    else:
        print ("Enter a valid input.")
