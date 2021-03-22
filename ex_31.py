hours = int(input('Enter Hours: '))
rate = int(input('Enter Rate: '))
overRate = rate * 1.5

if hours > 40:
    pay = hours * overRate
    print ('Pay: ' + str(pay))
else:
    pay = hours * rate
    print ('Pay: ' + str(pay))

    
