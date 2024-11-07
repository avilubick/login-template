def file():
    enterSelection = input("(1)Log In (2)Register\n> ")
    if enterSelection == "2":
        newUserName = input("New Username:\n> ").lower()
        with open("users.txt", "r") as userCheck: users = userCheck.read(); userCheck.close()
        if newUserName in users.split("*"):
            print("Error: User already exists")
            file()
        with open("users.txt", "a") as us: us.write(f"*{newUserName}"); us.close()
        with open(f"users/{newUserName}.txt", "w") as userFile: userFile.close()
        print("User Created")
        file()

    elif enterSelection == "1": pass
    else: file()

    user = input("Enter Your Username:\n> ").lower()

    with open("users.txt", "r") as userCheck: users = userCheck.read(); userCheck.close()

    def userIn(user):
        with open(f"users/{user}.txt", 'r') as userContent: content = userContent.read().split("*"); userContent.close()
        return [i for val2, i in enumerate(content) if val2 % 2 == 0], content

    if user in users.split("*"):
        print("User Found")
        contentList, content = userIn(user)
    else:
        print("User Not Found")
        file()

    def find(contentList,content):
        if contentList == []: print("None")
        inputIn = input("(1)Add, (2)Find or (3)Exit?\n> ")
        if inputIn == "1":
            catAdd = input("Add what catagory?\n> ")
            contAdd = input("Add what content?\n> ")
            with open(f"users/{user}.txt", 'a') as F: F.write(f"*{catAdd}*{contAdd}"); F.close()
            content, contentList = userIn(user)
            print(contentList)
            find(contentList, content)
        elif inputIn == "2":
            inp = input(f"{contentList}\nCatagory?\n> ")
            print(content[content.index(inp)+1]) if inp in content else print("Not Found")
            find(contentList, content)
        elif inputIn == "3": file()
        else: find(contentList, content)

    find(contentList, content)
file()

