import colorCode

def main():
    while True:
        user = int(input("--MENU--\nWhat would you like to do?\n1. Organize and Color code planner\n2. Add a task\n3. Delete a task\n4. Complete a task\n"))
        if user == 1:
            colorCode.organize()
        elif user == 2:
            while True:
                time = input("Please enter a date: ")
                section = input("Please enter a class section: ")
                info = input ("Please enter the description: ")
                print("\nDate:",time,"Class:",section,"\nDescription:",info)
                print() 
                verify = input("Is this information correct? (y/n) ")
                if verify.capitalize() == "Y":
                    colorCode.addTask(time,section,info)

                    attempt = input("Would you like to add another task? (y/n) ")
                    if attempt.capitalize() == "Y":
                        continue
                    else:
                        break
                else:
                    print("Let's try again")

        elif user == 3:
            while True:
                try:
                    row = int(input("Please enter in a row: "))
                except:
                    print("Please enter a valid number")
                    continue
                colorCode.showInfo(row)
                verify = input("Is this information correct? (y/n) ")
                if verify.capitalize() == "Y":
                    colorCode.deleteTask(row)
                    attempt = input("Would you like to delete another task? (y/n) ")
                    if attempt.capitalize() == "Y":
                        continue
                    else:
                        break
                else:
                    print("Let's try again")
        elif user == 4:
            while True:
                try:
                    row = int(input("Please enter in a row: "))
                except:
                    print("Please enter a valid number")

                colorCode.showInfo(row)
                verify = input("Is this information correct? (y/n) ")
                if verify.capitalize() == "Y":
                    colorCode.complete(row)
                    attempt = input("Would you like to complete another task? (y/n) ")
                    if attempt.capitalize() == "Y":
                        continue
                    else:
                        break
        elif user == "q":
            break

main()

