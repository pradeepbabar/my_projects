#Function, function is a reusable block of code that you can reuse later in your program as many times as you want

def say_hello():
    print('hello beta')

say_hello()  #to call the function we need to metnion name of the function with parentheses 
say_hello()

#Function with parameters using user_name as parameters in below code
def say_hi(user_name):
    print('hello beta' + user_name)

say_hi("Bob")  
say_hi("John")  

#Function with two parameters using user_name & user_age as parameters  in below code
def say_ho(user_name, user_age):
    print('hello beta' + user_name +", tumhara age hai " + str(user_age))

say_ho("Bob ", 10)  
say_ho("John ", 20)  


#Function with return statement
def do(num):
    return num * 2


number = do(3)
print(number)

#Below code we will call above 'num' function in another function
#any variable created in function will not be avilable outside the function in below code 'result' is variable
#variable created in function is called local variable, created outside is called global variable
def do_print(num):
    result = do(num)
    print("Double of " + str(num)+ " is " +str(result))

do_print(5)
