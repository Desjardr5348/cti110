#CTI-110
#P4HW2 - Salary Calculator
#Ronald Desjardins
#15NOV2021

#Ask employee name
employee_name=str(input('Enter employees name or "None" to terminate: '))
user=0
#Create lists for overtime_pay, reg_pay, gross_pay
overtime_pay=[]
reg_pay=[]
gross_pay=[]

#Create while loop using "None" terminate the LookupError
while employee_name !='None':
  work_hours=int(input(f"How many hours did "+ employee_name +" work? "))
  payrate=float(input(f"What is "+ employee_name +" pay rate? "))

  #If statement for user payrate / overtime_pay / gross_pay appended values will populate empty lists
  if work_hours<=40:
    user+=1
    overtime=0
    overtime_hrs=0
    regular=payrate*work_hours
    gross=regular

    #Append lists with values
    overtime_pay.append(overtime)
    reg_pay.append(regular)
    gross_pay.append(gross)

    #output
    print('')
    print(f"Employee name: ",employee_name)
    print("------------------------------------")
    print(f"Hours worked",'{:.1f}'.format(work_hours))
    print(f"Payrate",'{:.1f}'.format(payrate))
    print(f"Overtime: ",'{:.1f}'.format(overtime_hrs))
    print(f"Overtime Pay: $",'{:.2f}'.format(overtime))
    print(f"Regular Hour Pay: $",'{:.2f}'.format(regular))
    print(f"Gross Pay: $",'{:.2f}'.format(gross))
    print('')
    employee_name=str(input('Enter employees name or "None" to terminate: '))

  else:
    user+=1
    work_hours>40
    overtime_hrs=work_hours-40
    overtime=(payrate*1.5) * overtime_hrs
    regular=payrate * 40
    gross=regular + overtime

    #Append values to empty lists
    overtime_pay.append(overtime)
    reg_pay.append(regular)
    gross_pay.append(gross)

    #Output
    print('')
    print(f"Employee name: ",employee_name)
    print("------------------------------------")
    print(f"Hours worked",'{:.1f}'.format(work_hours))
    print(f"Payrate",'{:.1f}'.format(payrate))
    print(f"Overtime: ",'{:.1f}'.format(overtime_hrs))
    print(f"Overtime Pay: $",'{:.2f}'.format(overtime))
    print(f"Regular Hour Pay: $",'{:.2f}'.format(regular))
    print(f"Gross Pay: $",'{:.2f}'.format(gross))
    print('')
    employee_name=str(input('Enter employees name or "None" to terminate: '))

#Print totals of employees / total amount payed for overtime/regular hours/and gross
print(f"Total number of employees: ", user)
print(f"Total amount paid for overtime: $",'{:.2f}'.format(sum(overtime_pay)))
print(f"Total amount paid for regular hours: $",'{:.2f}'.format(sum(reg_pay)))
print(f"Total amount paid in gross: $",'{:.2f}'.format(sum(gross_pay)))