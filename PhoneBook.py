def main():
    def ContactSet():
        ans = 'Y'
        i = 0
        while (ans != 'N'):
            ans =input("Would you like to add a new contact? \
                                           Type 'Y' for yes or 'N' for no. [Y/N]: ")
            ans = ans.upper()
            i = i + 1
            return ans
    def addContact(s):
        if s== 'Y':
            firstName =input("Enter first name: ")
            lastName =input("Enter last name: ")
            phoneNo = input("Enter phone number: ")
            f = open("phonebook.txt", 'a') # create a new or open an existing file
            f.write(firstName + ":")
            f.write(lastName + ":")
            f.write(phoneNo + ":\n")
            f.close()
            ans=1
            return ans
        else:
            print('You answered No or that is an invalid input.')
    def showContact(f):
        if f==1:
            print("You have the following records:")
            f = open("phonebook.txt", 'r'); #open for reading only
            print(f.read())
            f.close()
        else:
            input("Press 'Enter' to exit and try again: ")
    t=ContactSet()
    d=addContact(t)
    showContact(d)
main()

