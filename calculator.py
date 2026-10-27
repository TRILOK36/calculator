
# take user input and convert it to integer and store it in list "l"
num = input("enter no. with spaces\nfor following operations\n addition\n subtractio\n multiplication\n average\n")
l = [int(x) for x in num.split()]

#user defined function for "addition" of no. present in list
def add():
    if len(l) == 0:
        return None
    return sum(l)

#user defined function for "subtraction" of no. present in list
def sub():
    
    if len(l) == 0:
        return None
    
    
    result = l[0]
    for i in l[1:]:
        result -= i
        
    return(result)
        
#user defined function for "multiplication" of no. present in list
def multi():
    if len(l) == 0:
        return None

    result = l[0]
    for i in l[1:]:
        result *= i
    return(result)

#user defined function for to find "average" of no. present in list
def average():
    
    if len(l) == 0:
        return None
   
    s = add()
    return s/len(l)

#main program which run the all the functions
while True:    
    q = int(input("What you want to check( Enter no. only) \n 1.Addition\n 2.Average \n 3.Subtraction \n 4.Multiplication \n 5.For both Adition & Average"))
    if q == 1:
        print("Addition of all no. is ", add())
    elif q == 2:
        print("Average of all no. is ", average())
    elif q == 3:
        print("Subtraction of all no. is ", sub())
    elif q == 4:
        print("Multiplication of all no. is ", multi())
    elif q == 5:
        print("Addition of all no. is", add())
        print("Average of all no. is", average())
    else:
        print("Invalid option")
#asked the user wheter to continue on not        
    B = input("Do you want to continue?(Y/N)\n").upper()
    if B != "Y":
        print("\n" + "=" * 40)
        print("Thank you for using my program!")
        print("Thanks for visiting my GitHub project.")
        print("=" * 40)
        break
#give user chance to modify or use completely new list of values to perform operaton
    else:
        d = input("With Old no. or New  or Change the current values (O/N/C)\n").capitalize()
        if d == "Old" or d == "O":
            print(f"Continuing with old numbers: {l}")
            
        elif d == "N" or d == "New":
            num = input("Enter new numbers with spaces: \n")
            l = [int(x) for x in num.split()]
            
        elif d == "C":
            #user can delete or add no. in list
            w = int(input("What u want to Change(Enter no. only) \n1.Delete the Number\n2.Add a new Number\n"))
            
            if w == 1:
                n = int(input(f"which no. you want to delete\n {l}\n"))
                if n in l:
                    l.remove(n)
                    print("Current list:", l)
                    
                else:
                    print("Number not found in the list")
                    print(f"current list{l}")
                    
            elif w == 2:
                n = int(input(f"Enter no. which you want add\n current list{l}\n"))
                l.append(n)
                print(f"new values {l}")
                
            else:
                print("invalid option")
                
        else:
            print("invalid option")
            
            #   PROGRAM ENDED, THANK YOU! TO USE OR VISIT MY PROGRAM.