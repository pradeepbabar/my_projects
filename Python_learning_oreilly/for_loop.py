#There are two types of loop for & while loop
#For loop condition

for i in range(10):
    print('kem cho' + str(i)) #Note: only print under for loop is repeted i times but outside for loop is not repeted
print('Majama')


#while loop with exact behaviour with above for loop
i = 0
while i < 10:
    print('A Hallo')
    i += 1  #We can also write i = i + 1 or i +=1 oth are same
    

#Use Loops to Iterate on Python Lists
number_list = [10, 12, 20, -3, -5, -4]

for number in number_list:
    print(number)
    if number < 0:
        print('number is negative')
    