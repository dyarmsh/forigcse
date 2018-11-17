# code to output employee's wage/day according to number of hours worked
# whilst simultaneously outputting best employee details and stats 
hour_range1 = 0 # hours worked are less than 5 hours
hour_range2 = 0 # hours worked are between 5 and 9 hours
hour_range3 = 0 # hours worked are between 10 and 14 hours
hour_range4 = 0 # hours worked are between 15 and 18 hours
hour_range5 = 0 # hours worked are greater than 18

best_employee = 0

for i in range(30):
    employee_name = input("Enter employee name ::")
    employee_no = int(input("Enter employee number ::"))
    hrs_worked = int(input("Enter number of hours worked ::"))

    if hrs_worked < 5:
        perhr_pay = 0
        hour_range1 += 1

    elif 5 <= hrs_worked <= 9:
        perhr_pay = 70
        hour_range2 += 1

    elif 10 <= hrs_worked <= 14:
        perhr_pay = 100
        hour_range3 += 1
    
    elif 15 <= hrs_worked <= 18:
        perhr_pay = 150
        hour_range4 += 1

    elif hrs_worked >= 19:
        perhr_pay = 200
        hour_range5 += 1
        
    total_payment = hrs_worked*perhr_pay
    print("$",total_payment, ":: is the total pay")

    # to determine which employee worked for the most hours
    if hrs_worked > best_employee:
        best_employee = hrs_worked
        new_name = employee_name
        new_no = employee_no
        best_perhr_pay = total_payment
        
# outputting stats
print(hour_range1, ":: employee/s worked less than 5 hours")
print(hour_range2, ":: employee/s worked between 5 and 9 hours")
print(hour_range3, ":: employee/s worked between 10 and 14 hours")
print(hour_range4, ":: employee/s worked between 15 and 18 hours")
print(hour_range5, ":: employee/s worked greater than 19 hours")

# adding 20% to best employee's pay and printing their details 
bestemp_pay = best_perhr_pay * 1.2
print("The best employee is ::", new_name)
print("With employee code ::", new_no)
print("For having worked ::", best_employee, "hours")
print("Thereby, recieving gross pay of :: $", bestemp_pay)
