inp1 = input('Enter Hours: ')
inp2 = input('Enter Rate: ')

try:
    hours = int(inp1)
    rate = int(inp2)

    overRate = rate * 1.5

    if hours > 40:
        pay = hours * overRate
        print ('Pay: ' + str(pay))
    else:
        pay = hours * rate
        print ('Pay: ' + str(pay))

except:
    print ('Please Enter a Number')
