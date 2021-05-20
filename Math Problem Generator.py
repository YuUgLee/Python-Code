#Newton Bao
#CECS Project 2 3-12-19
#CECS 100
#ID:018286708
'''Use functions for organizing the programs.
Possible functions are:
1. Interface with user can be a function
2. The number generator may be a function
    a.) How many digits the numbers have
3. The problems may be functions
    a.) Addition, Subtraction, Division, Multiplication
4. Scoring their results
5. Exiting the game'''
def main():
    def interface():
        i=2
        print('This is a Math quiz.\
You will be asked questions to make choices about\
 the type \
 of problems you will do.')
        print('You will be asked the difficulty of the numbers.')
        print('Type Level 1 if you want numbers from 0 to 10. If you want\
 numbers from 0 to 100 choose Level 2. If you want numbers from 0 to 1000 choose Level 3.\r')
        try:
            level=int(input("Type in '1' for Level 1, '2' for Level 2, and '3' for Level 3: "))
            if level=='1' or '2' or '3':        #use or to allow multiple conditions to be accepted
                return level
            else:
                print("Please type in a correct level.")
        except ValueError:                              #Use try and except to allow string errors from user input
            print("\n\nPlease type in a correct level.\n\n")
            h=interface()                   #assign a variable to the definition of interface() to return its value to the next defintion
            return h
            
    def numbers(s):
        if s == 1:
            N = 10
        elif s == 2:
            N = 100
        elif s == 3:
            N = 1000
        import random
        L = []#empty list
        for i in range(11):
            r=random.randint(0,N)
            L.append(r)
        num1=L[0]                       #Using empty list to input random numbers in which each number counts for a separate random value
        num2=L[1]

        print(num1, 'and', num2)
        return L
    def operation():
        i=2
        op=input("Enter the operation by entering '+', '-', '*', or '/': ")
        if op == '+':
            print("You have chosen addition.")
            d = '+'
            return d
        else:
            if op == '-':
                print("You have chosen subtraction.")
                return op
            else:
                if op== '*':
                    print ("You have chosen multiplication.")
                    return op
                else:
                    if op== '/':
                        print("You have chosen division")
                        return op
                    else:
                        print("Please enter a valid operation.")        #assigning a variable to the definition of operation() to be able to return the value of the second operation() instead of the first                                  
                        z=operation()
                        return z
                        
                        

    def quiz(g,h):
        score=0                     #sets like a base value
        i=0
        for i in range(10):         #Decides the number of questions
            num1=g[i]
            num2=g[i+1]             #adding 1 to change to a different random number for every question
            if h == '+':
                answer=num1+num2
            elif h== '-':
                answer=num1-num2
            elif h=='*':
                answer=num1*num2
            elif h=='/':
                answer=num1/num2
            print("What is",num1,h,num2, "?")               #'h' replaces whatever operator is desired by the user
            try:                                            #Use try and except to accept incorrect inputs that are not numbers, like strings, and continue the script instead of ending it.
                response =int(input("Enter your answer: "))
                if response == answer:
                    print('Correct.')
                    score=score+1
                else:
                    print('That is incorrect.')
            except ValueError:
                print('That is incorrect.')
        return score

    def score(t):
        print("Your score is", t)
        if t < 10:
            print("Wow, you didn't get a perfect score. That's pathetic.\n")
        elif t == 10:
            print("That's what I expect from you.\n")
        
        chance=input("Would you like to try again?\nType 'Yes' to try again. Type 'No' to exit: ")
        c=chance.capitalize()               #.capitalize()=Capitalizes the user input so that 'yes' and 'Yes" are both accepted as an answer.
        if c == 'Yes':                      #Restarts the entire program if the user wishes to try again.
            x= interface()
            y= numbers(x)
            z=operation()
            f=quiz(y,z)
            score(f)
        else:       
            input("Press 'Enter' to exit")  #Exits the program
        

    x= interface()
    y= numbers(x)
    z=operation()
    f=quiz(y,z)
    score(f)
    
    
main()

