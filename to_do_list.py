def menu():
    task=load_task()
    print("*"*10+"\twelcome to to-do list application\t"+"*"*10+"\n")
    while True:
        print("1. Add the task")
        print("2. View the task")
        print("3. Mark as done")
        print("4. Exit\n")

        choice= int (input("enter the choice:\t"))
        if choice==1:
            add_task(task)
        elif choice==2:
            view_task(task)
        elif choice==3:
            mark_done(task)

        elif choice ==4:
            save_task(task)
            print("exiting")
            break

def add_task(task):
    t=input("\nEnter the description of the task:\t")
    task.append(t)
    print("\nThe task is added succesfully")

def view_task(task):
    print("\n tasks: \n")
    for i in range(len(task)):
        print(f"{i+1}.{task[i]}")
    print("\n")

def mark_done(task):
    if not task:
        print("no task to mark as done")
    view_task(task)
    index=int(input("enter the index of task to mark as done:\t"))-1
    if 0<=index<=len(task):
        removed_task=task.pop(index)
        print(f"task {removed_task} is marks as done")
    else:
        print("invalid index")

def load_task():
    try:
        with open("task.txt",'r')as f :
            return f.read().splitlines()
    except:
        return []
def save_task(task):
    print("saving you task as task.txt")
    with  open ("task.txt",'w') as f:
        for i in task :
            f.write(i+'\n')

menu()
