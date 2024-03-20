var = ["r", "x", "y", "z"]
var_complement = ["r̄" ,"x̄", "ȳ", "z̄"]

valuesPerVariable = {"r": [], "x": [], "y": [], "z":[]}

# user_Values = input("Enter your values for the function: ")

# construct table from a list of assigned values of 0s and 1s
def table(n):
    #a variable to store the degree since we will be manipulating it
    exp = 2**n/2
    # Instantiate an empty table to start the multi-dimensional list
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
                    for y in range(first_index,i):
                        table[y]=start
                    if (i + exp) > len(table)-1:
                        for z in range(i,len(table)):
                            table[z] = 1
                if start == 0:
                    start =1
                else:
                    start = 0
                first_index = i
            exp = exp/2

def SOP(DegreeOfFunction, stringOfValues):
    currentString = ""
    arrayOfPositions = [] # stores the positions with output as one

    # get the positions of 1s in the table
    for x, index in enumerate(stringOfValues):
        if x == 1:
            arrayOfPositions.append(index)

    # determine values for each index
    for row in arrayOfPositions:
        for col in range(DegreeOfFunction):
            if table[row][col] == 0:
                currentString += var_complement[col]
            else:
                currentString += var[col]
        if row == len(arrayOfPositions)-1:
            return currentString
        else:
            currentString += " + "

def POS(DegreeOfFunction, table):
    arrayOfPositions =[]
    for i, row in enumerate(table):
        if 0 in row:
            arrayOfPositions.append(i)

    pos_expression = ""
    for row_index in arrayOfPositions:
        current_string = ""
        for col in range(DegreeOfFunction):
            if table[row_index][col] == 1:
                current_string += var_complement[col]
            else:
                current_string += var[col]
                if col < DegreeOfFunction - 1:
                     current_string += " + "
        pos_expression += "(" + current_string + ")" + " . "
    
    pos_expression = pos_expression[:-3]

    return pos_expression

# construct table from a list of assigned values of 0s and 1s
def table():
    pass

def main():
    pass

# Ask user to enter the degree of the function
# make reference to var list to get variables

# Use degree of the function to find the number of values per variable

# Create the empty table with pre-filled values of variables
# Ask user to input the values of the function in a string format with delimiters: " "
# Display the values in the table
# Ask the user if they want to do POS or SOP calculation	

# ask for user input
