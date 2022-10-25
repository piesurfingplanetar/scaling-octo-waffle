#Calculate tax
def caltax(grosspay, tax):
    return grosspay * tax

#Define rates
def pay(hours, rate):
     if hours <= 40:
        return hours * rate
     if hours > 40:
        return ((hours-40) * rate * 1.5) + rate * 40

print('Welcome to Payroll Calculator')

#Gather employee name
print("Enter recipient employee name")
employee_name = input()

#Gather employee hourly rate
while True:
    try:
        rate = float(input('What is the hourly rate for ' + employee_name+ '?'))
        break
    except ValueError:
        print('Invalid value, please enter a number')
print(rate)

#Gather employee number of hours
while True:
    try:
        hours = float(input('How many hours did ' + employee_name+ ' work?'))
        if hours < 168 and hours > 0:
            break
        else:
            continue
    except ValueError:
        print('Invalid value, please enter a number')

grosspay = pay(hours, rate)
fedtax = caltax(grosspay, .15)
stattax = caltax(grosspay, .1)
fica = caltax(grosspay, .02)
netpay = grosspay - fedtax - stattax - fica

#need to figure out how to make this conditional so it doesn't give negative if no OT
otpay = (hours - 40) * rate * 1.5

#this will only work when there is OT 
regpay = grosspay - otpay

#Print everything
print('Employee name: ' + employee_name)
print('Hourly rate: $' + str(rate))
print('Hours worked: ' + str(hours))
print('Regular pay: $' + str(regpay))
print('Overtime pay: $' + str(otpay))
print('Gross pay: $' + str(grosspay))
print('Federal tax: $' + str(fedtax))
print('State tax: $' + str(stattax))
print('FICA: $' + str(fica))
print('Net Pay: $' + str(netpay))
