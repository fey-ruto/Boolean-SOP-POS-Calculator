var = ["r", "x", "y", "z"]
var_complement = ["r̄" ,"x̄", "ȳ", "z̄"]

# user_Values = input("Enter your values for the function: ")

# construct table from a list of assigned values of 0s and 1s
def table(n):
    #a variable to store the degree since we will be manipulating it
    exp = (2**n)//2
    table = []
    #loop through the array and create an empty array so that it becomes multi-dimensional
    for _ in range(2**n):
        table.append([])
    #Populate the array for the different combinations 
        #Logic: We will use the for loop with a step which will step starting from 2**n/2 times and continuously divided by 2 until the resultt is 1, after each step the alternating variable will change from 0 to 1
        #After we will populate the spaces with the last element of the stop 
        #Loop n times to represent a cloumn for every variable
    for x in range(n):
        #Create a variable that will alternate between 0 and 1
        first_index = 0
        start = 0

        for i in range (0,len(table),exp):
            table[i].append(start)                
            if i != 0:
                for y in range(first_index+1,i):
                    table[y].append(previous)
                if (i + exp) > len(table)-1:
                    for z in range(i+1,len(table)):
                        table[z].append(1)
            previous = start
            if start == 0:
                start =1
            else:
                start = 0
            first_index = i
        exp = exp//2
    return table

def SOP(DegreeOfFunction, stringOfValues, table):
    currentString = ""
    arrayOfPositions = [] # stores the positions with output as one

    # get the positions of 1s in the table
    for index, x in enumerate(stringOfValues):
        if x == "1":
            arrayOfPositions.append(index)

    # determine values for each index
    for row in arrayOfPositions:
        for col in range(DegreeOfFunction):
            if table[row][col] == 0:
                currentString += var_complement[col]
            else:
                currentString += var[col]

        # if at last index do not add "+"
        if row != arrayOfPositions[len(arrayOfPositions)-1]:
            currentString += " + "

    return currentString

def POS(DegreeOfFunction, stringOfValues, table):
    arrayOfPositions = [] # stores the positions with output as one
    pos_expression = ""

    # get the positions of 1s in the table
    for index, x in enumerate(stringOfValues):
        if x == "0":
            arrayOfPositions.append(index)

    # determine values for each index
    for row in arrayOfPositions:
        currentString = ""
        for col in range(DegreeOfFunction):
            if table[row][col] == 1:
                currentString += var_complement[col] +  " + "
            else:
                currentString += var[col] + " + "
        pos_expression += "(" + currentString[:-3] + ")" # remove trailing "+"

    return pos_expression

def displayTable(DegreeOfFunction, user_table):
    functionDef = "F("
    # make reference to var list to get variables
    for i in range(DegreeOfFunction):
        print(var[i] , '\t', end='')
        if i == DegreeOfFunction - 1:
            functionDef += var[i] + ")"
            print(functionDef + "\t", end='')
            print()
        else:
            functionDef += var[i] + ","
    
    # values populate into display
    for x in range(len(user_table)):
        for y in range(len(user_table[x])):
            if y == DegreeOfFunction-1:
                space = 2
            print(user_table[x][y], "\t", end='')
        print()


def main():
    while True:
        # Ask user to enter the degree of the function
        DegreeOfFunction = int(input("Enter the degree of the function: "))

        # check if degree of function is greater than 4
        if DegreeOfFunction <= 4 and DegreeOfFunction > 0:
            break
        print("Invalid Input. Try again. Enter a number between 0 and 5. Not Inclusive.")

        
    # Create the empty table with pre-filled values of variables
    user_table = table(DegreeOfFunction)
    displayTable(DegreeOfFunction, user_table)

    # make sure user values are equal to the number of values required
    while True:
        # Ask user to input the values of the function in a string format
        user_Values = input("Enter your values in single line, for example, 0011\nYour Values: ")
        if len(user_Values) == 2**DegreeOfFunction:
            break
        print(f"Invalid Input. Enter {2**DegreeOfFunction} values.")

    # append user values into array table
    for x in range(len(user_table)):
        user_table[x].append(user_Values[x])
    
    displayTable(DegreeOfFunction, user_table)

    # Display POS or SOP calculations
    print("SOP Expression:", SOP(DegreeOfFunction, user_Values, user_table))
    print("POS Expression:", POS(DegreeOfFunction, user_Values, user_table))

count = 0
while True:
    print("Welcome to the sum of product and product of sum calculator. Enter")
    choice = input("1: Run Calculator \n2: Enter <space>\nYour Choice: ")
    if choice == "1":
        count += 1
        main()
    else:
        if count >= 1:
            print("Thanks for using me!!")
        else:
            print("Bye!!")
        break