var = ["r", "x", "y", "z"]
var_complement = ["r̄" ,"x̄", "ȳ", "z̄"]

valuesPerVariable = {"r": [], "x": [], "y": [], "z":[]}

def SOP(DegreeOfFunction, table):
    arrayOfPositions = [] # stores the positions with output as one
    for row in arrayOfPositions:
        currentString = ""
        for col in range(DegreeOfFunction):
            if table[row][col] == 0:
                currentString += var_complement[col]
            else:
                currentString += var[col]
        currentString += " + "

def POS():
    pass

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