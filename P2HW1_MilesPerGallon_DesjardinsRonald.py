#This program will calculate your miles per gallon, total gass cost, and per mile cost. 
#11 OCT 2021
#CTI-110 P2HW1 - Miles Per Gallon 
#Ronald Desjardins
#

#Define miles per gallon using float / input 
miles_driven = float(input("Enter miles driven:    "))

#Define gallons used using float / input 
gas_used_gallons = float(input("Enter gallons used:    "))

#Define cost per gallon using float / input
cost_gallon = float(input("Enter cost per gallon:    "))

#Output space line
print()

#Calculation for miles per cost_gallon 
mpg = miles_driven / gas_used_gallons
round(mpg, 2)

#Calculation for gas total
gas_total_cost = cost_gallon * gas_used_gallons
round(gas_total_cost, 2)

#Calculation for cost per miles_driven 
cpm = gas_total_cost/miles_driven
round(cpm, 2)

#Output for miles per gallon (MPG) 
print("Miles Per Gallon:", mpg)

#Output for Total Gas Cost gas_total_cost
print("Total Gas Cost:", gas_total_cost)

#Output for Cost Per Mile (cpm)
print("Cost Per Mile:", cpm)