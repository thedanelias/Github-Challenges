import decimal
costoftile = float(input("Please enter the cost of tiles per square metre: "))
width = float(input("Please enter the width of the area you would like to tile in square metres: "))
length = float(input("Please enter the length of the area you would like to tile in square metres: "))
area = (width * length)
totalcost = (area * costoftile)
print("The cost of the area you'd like to tile is ", totalcost)