#THis is Python level 2 exercise from oreilly

#2.1
def nam():
    a = input('enter your name:')
    b = input('enter your age:')
   
    print('Your name is ' +a+ ' and you age is ' +b)
nam()


#2.2
def sam():
    a = input('enter your num1:')
    b = input('enter your nnum2:')
    c = int(a) + int(b)
    print('Your sum is ', c)

sam()

#2.3
def avg():
    list = [10.0, 12.5, 15.5, 15.0]
    a = sum(list)
    z = a / len(list)
    print('avg of your last ask', z)

avg()

#2.4
def celsuis_to_fehrenit(celsius_deg):
    return celsius_deg * 1.8 + 32

print("20^c" + str(celsuis_to_fehrenit(20)) +"^f")
