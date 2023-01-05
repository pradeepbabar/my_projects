#Python Level 3: Exercises

#3.1
def comp():
    list = [10, 5, 4, 2, 12, 5]
    x = max(list)
    print(x)

comp()


#3.2

num_list = []

for i in range(5):
    x = int(input('enter number:'))
    num_list.append(x)

y = sum(num_list)
z = len(num_list)
avg = y / z  

print('average is:', avg)

#3.3
number_list = []
ask_usr = True

while ask_usr:
    usr_input = float(input('Enter number: '))
    if usr_input == 0.0:
        ask_usr = False
    else:
        number_list.append(usr_input)

d = sum(number_list)
e = len(number_list)

average = d / e

print('while loop avg: ', average)


