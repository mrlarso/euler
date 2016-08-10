year = 1901
days_of_week = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
months = [['Jan',31],['Feb',28],['Mar',31],['Apr',30],['May',31],['june',30],['July',31],['Aug',31],['Sept',30],['Oct',31],['Nov',30],['Dec',31]]
day_index = 1

sunday_firsts = 0
while year < 2001:
    if year%4 ==0:
        months[1] = ['Feb',29]
    else:
        months[1] = ['Feb',28]
    for month in months:
        print month[0]
        for day in range(1,month[1]+1):
            print days_of_week[day_index], str(day),month[0],year
            if day == 1 and day_index == 6:
                sunday_firsts += 1
            if day_index == 6:
                day_index = 0
            else:
                day_index +=1
    year += 1

print str(sunday_firsts)
