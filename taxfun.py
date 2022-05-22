#write a function to calculate the annual salary and income tax of an employee by accepting monthly salary

def yearly_sal(sal):
    ysal = sal * 12
    return ysal


def income_tax(ysal):
    if ysal<=400000:
        tax=0

    else:
        tax=ysal*10/100
    return tax

msal = float(input('enter monthly salary: '))
ysal = yearly_sal(msal)
print('your yearly salary = %.2f' % ysal)

itax = income_tax(ysal)
print('your income tax = %.2f' % itax)
