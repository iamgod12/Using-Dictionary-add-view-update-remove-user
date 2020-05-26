choice='''
Press 1: To add user
Press 2: To view user
Press 3: To delete user
Press 4: To exit
'''
print(choice)
data=dict()
while True:
    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        name = input("Enter Name: ")
        rn = int(input("Enter Roll Number: "))
        if name in data:
            print("A user with this name already exist")
        else:
            data[name] = rn
            print('{} added Successfully.'.format(name))
    elif choice == 2:
        print("Total Users: {}".format(len(data)))
        for key,value in data.items():
            print('Name: {}'.format(key))
            print('Roll No: {}'.format(value))
    elif choice == 3:
        dele=input("Enter name You Wanr to delete: ")
        if dele in data:
            data.pop(dele)
            print('{} deleted'.format(dele))
        else:
            print("User doesn't exist")
    elif choice == 4:
        break
    else:
        print("Invalid Choice ")
