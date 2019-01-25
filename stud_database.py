def stud_database():
    redstud = 0
    blustud = 0
    grestud = 0
    yelstud = 0
    stud_name = []
    house_name = []
    grade_no = []
    for i in range(0,10):
        name = input('ENTER NAME:')
        stud_name.append(name)
        house = input('ENTER HOUSE:')
        house_name.append(house)
        grade = int(input('ENTER GRADE:'))
        grade_no.append(grade)
        if grade_no[i] == 10:
            print(stud_name[i])
            print(house_name[i])
    for i in range(0,10):
        if house_name[i] == 'red':
            redstud += 1
        elif house_name[i] == 'blue':
            blustud += 1
        elif house_name[i] == 'yellow':
            yelstud += 1
        elif house_name[i] == 'green':
            grestud += 1           
stud_database()
