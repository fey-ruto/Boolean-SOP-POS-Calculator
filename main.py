var = ["r", "x", "y", "z"]
var_complement = ["r̄" ,"x̄", "ȳ", "z̄"]

valuesPerVariable = {"r": [], "x": [], "y": [], "z":[]}

# user_Values = input("Enter your values for the function: ")

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
        currentString += " + "
    return currentString

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
