#conditional statement with Booleans

a = 1 > 1
print(a)


b = 1 >= 1
print(b)


num_list = [1, 2, 4]
c = 2 in num_list
d = 5 in num_list

print(c)
print(d)

#combination of different conditionals

z = (1 == 1) or (2 == 3)
print(z)


y = (1 == 1) and (2 == 3)
print(y)

#Differnet conditional statement example
user_age = 25

if user_age >= 18 and user_age<30:
    print('You are an adult below 30')

print('End of program, below is diff. code')

#If else condition 
if user_age >= 18:
    print('Bingo you are voter')
else:
    print('Need to grow up')

#elif condition in below code, NOTE:pytho n is case sensative
month='Jun'

if month in ['Mar', 'Apr', 'May']:
    print('Summer Season')
elif month in ['Jun', 'Jul', 'Aug']:
    print('Rainy season')
elif month in ['Sep', 'Oct', 'Nov', 'Dec', 'Jan']:
    print('Winter season')
else:
    print('Spring Season')

