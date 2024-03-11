# Ask user to enter the degree of the function
# Create the empty table with pre-filled values
# Ask user to input the values of the function in a string format with delimiters: " "
# Display the values in the table
# Ask the user if they want to do POS or SOP calculation

# POS: create an array that stores the positions of the values of 0
# SOP: create an array that stores the positions of the values of 1

# Use the index of the position to find the respective row in the table and return each value
# for example: "x: 0" will return NOT(x) if the output is 1 SOP
#              "x: 1" will return NOT(x) if output is 0 POS

# 2 loops: Outer Loop (Index of 0 or 1) and Inner Loop (Degree of the function)

# SOP 
# arrayOfPositions = [2,4,8]
# currentString = ""
# finalString = ""
# for x in range(len(arrayOfPositions)):
#   for y in range(2):
#       if table[x][y] == 0:
#           currentString += "." + NOT(table[x][y]))
#       else:
#           currentString += " . " + table[x][y]  
#   finalString += " + " + currentString

# POS
# arrayOfPositions = [2,4,8]
# currentString = ""
# finalString = ""
# for x in range(len(arrayOfPositions)):
#   for y in range(2):
#       if table[x][y] == 0:
#           currentString += "+" + NOT(table[x][y]))
#       else:
#           currentString += " + " + table[x][y]  
#   finalString += " . " + currentString