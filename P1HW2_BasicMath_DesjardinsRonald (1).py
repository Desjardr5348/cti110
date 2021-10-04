#This program will calculate any monthly/annually bill and to include 6% taxes
#04 OCT 2021
#CTI-110 P1HW2 - Basic Math
#Ronald Desjardins

tax = .06

print('Enter name of expense:', end=' ')
name_expense = (input())
print('Enter monthly charge:', end= ' ')
monthly_charge = int(input())
print()

print('Bill:', name_expense, end='       ')
print('Before Tax:', monthly_charge)

monthly_chargetax = monthly_charge * tax
annual_charge = (monthly_charge + monthly_chargetax) * 12
monthly_tax = tax * monthly_charge

print('Monthly Tax:', tax * monthly_charge) #displays the monthly tax by multiplying .06*monthly_charge input
print('Monthly Charge:', monthly_charge + monthly_tax)# displays the total monthly charge by adding the monthly_tax + monthly charge which equals the monthly payment
print('Annual Charge:', annual_charge)#displays the what you would pay annualy the formula is above
