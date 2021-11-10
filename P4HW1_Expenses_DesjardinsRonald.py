#CTI-110
#P4HW1 - Expenses
#Ronald Desjardins
#10NOV2021

#Prompt user to enter amount in account where money will be withdrawn from
money_account = float(input('Enter the amount of money currently in account: $'))

#Blank line to mimic output example
print()

#Prompt user to enter amount of first expense
expense = float(input('Enter expense: '))

money_total = money_account - expense

#Set extra_expense valye as y
extra_expense = 'y'

#Define expense_total
expenses_total = 0

#While statement for extra_expense if value == y
while extra_expense == 'y':

#Ask user if he/she wants to enter another expense
 extra_expense = input('Do you want to enter another expense? (y/n): ')

#Blank line to mimic output example
 print()
#Expense total by iteration
 expenses_total += 1

#if statement if extra_expense value is y
 if extra_expense == 'y': 
  expense = float(input('Enter expense: ' ))

#Calculate money_total for final output
  money_total -= expense

#if statement is extra_expense value is n
 if extra_expense == 'n':

#Break from loop if extra_expense value is n
  break

#Black line to mimic example output
print() 

#Output of amount in account before expenses
print('Amount in account before expenses subtracted: $', money_account) 

#output of number of expenses entered
print('Number of expenses entered: ', expenses_total)

#Output of amount in account after expenses subtracted
print('Amount in account AFTER expenses subtracted is: $',money_total)

