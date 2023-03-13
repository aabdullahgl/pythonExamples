

# added student
def addStudent(count):
    for i in range(count):
        firstName=input("\n enter your name : ")
        lastName=input("\n enter your last name : ")
        studentNameAndSurname=firstName+" "+lastName
        students.append(studentNameAndSurname)
        print("\n registration successful")          
    showScreen()

# deleted student
def deleteStudent(count):
    for i in range(count):
        firstName=input("\n enter your name : ")
        lastName=input("\n enter your last name : ")
        studentNameAndSurname=firstName+" "+lastName
        students.remove(studentNameAndSurname)

    showScreen()

# multi student added
def multiStudentAdd():
    count=int(input("\n number of students to add : "))
    
    for i in range(count):
        addStudent(count)
    showScreen()

# multi student deleted
def multiStudentDeleted():
    count=int(input("\n number of students to deleted : "))
    for i in range(count):
        deleteStudent(count)
    showScreen()    

# action list
def actionList():
    actions=["added student","deleted student","multi student added","multi student deleted","list student","exit"]   
    i=0
    while(i<len(actions)):
        print(f"{i} - {actions[i]}")
        i+=1 
    
    

# student list
def listStudent():
    print("------------- Student List -------------------")
    for i in range(len(students)):
        print("*****************************")
        print(f"\n No {i} Name : {students[i]} \n")
    print("------------------------------------------")
    showScreen()

#list students
students= []

# first screen and action selection
def showScreen():
    actionList()
    selectItem= int(input("\n please select your action : "))
    if selectItem==0:
        addStudent(1)
    elif selectItem==1:
        deleteStudent(1)
    elif selectItem==2:
        multiStudentAdd()        
    elif selectItem==3:
        multiStudentDeleted()
    elif selectItem==4:
        listStudent()
    elif selectItem==5:
        exit() 

showScreen()