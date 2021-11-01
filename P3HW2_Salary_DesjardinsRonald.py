# CTI-110
# P3HW2 - Salary
# Ronald Desjardins
# 1NOV2021

#input users Name
employee_name = (input("Enter employee's name: "))

#input hours worked
payrate = float(input("Enter employee's pay rate: $"))

#input users hours worked
hrs_work = float(input("Enter number of hours worked: "))

#if statement to determine if there is overtime
if hrs_work > 40:
 overtime = hrs_work - 40
 overtime_pay = round(overtime * payrate) * 1.5
 reghour_pay = round(40 * payrate, 2)
 gross_pay = round(overtime_pay + reghour_pay, 2)
 #output
 print()
 print("Employee Name:", employee_name)
 print()
 print("Hours Worked: ",hrs_work, "Pay Rate: ",payrate,     "Overtime: ",overtime,   "Overtime Pay: ",overtime_pay,    "ReguHour Pay: ",reghour_pay,    "Gross Pay: ",gross_pay)

#if no overtime, calculate regular pay
else:
 gross_pay = round(payrate * hrs_work, 2)
 reghour_pay = round(40 * payrate, 2)

 #print employee_name
 print()
 print("Employee Name:", employee_name)
 print()
 #output for else statement overtime is 0 and overtime_pay is 0
 print("Hours Worked: ",hrs_work, "Pay Rate: ",payrate,     "Overtime: 0",   "Overtime Pay: 0 ",    "RegHour Pay: ",reghour_pay,    "Gross Pay: ",gross_pay)