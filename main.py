def userIn(user):  # read users content file
    with open(f"users/{user}.txt", 'r') as userContent: x = userContent.read().split("*");userContent.close();return x

def find(content, user):
    if content == ['']: print("None")  # if user hasent saved anything (prob new user)
    inputIn = input("(1)Add, (2)Find or (3)Exit?\n> ")
    if inputIn == "1":  # if add
        catAdd = input("Add what catagory?\n> ")
        contAdd = input("Add what content?\n> ")
        with open(f"users/{user}.txt", 'a') as F:
            F.write(f"{"" if content == [''] else "*"}{catAdd}*{contAdd}"); F.close() # add content to file/need else?
        content = userIn(user)  # get newly appended user file
        print([i for val2, i in enumerate(content) if val2 % 2 == 0])  # print categories
        find(content,user)
    elif inputIn == "2":  # if find
        inp = input(f"{[i for val2, i in enumerate(content) if val2 % 2 == 0]}\nCatagory?\n> ")  # get input
        print(content[content.index(inp) + 1]) if inp in content else print("Not Found")  # look for input/FIX IF NO INPUT
        find(content,user)
    elif inputIn == "3":
        file()  # restart code
    else:
        find(content,user)  # if wrong input

def file():
    enterSelection = input("(1)Log In (2)Register\n> ") #Enter prompt
    if enterSelection == "2":   #if register
        newUserName = input("New Username:\n> ").lower()
        with open("users.txt", "r") as userCheck: users=userCheck.read();userCheck.close()#read all users from file
        if newUserName in users.split("*"):     #if user in saved
            print("Error: User already exists")
            file()     #restart
        with open("users.txt", "a") as us: us.write(f"*{newUserName}"); us.close()  #save new user
        with open(f"users/{newUserName}.txt", "w") as userFile: userFile.close()    #make content file for new user
        print("User Created")
        file()
    elif enterSelection == "1": pass    #if login, continue
    else: file()    #wrong input handling (restart code)

    user = input("Enter Your Username:\n> ").lower()
    with open("users.txt", "r") as userCheck: users = userCheck.read(); userCheck.close()   #read saved users

    if user in users.split("*"):    #if user valid
        print("User Found")
        content = userIn(user)     #get info from users file
    else:   #if user doesent exist
        print("User Not Found")
        file()  #restart code

    find(content,user)  #once logged in, search tool
file()

