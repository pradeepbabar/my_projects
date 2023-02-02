#Object oriented programming with python
#OOP is everywhere in Python.
#what is OOP. 
# So object oriented programming is a way of organizing your code into what we call classes. 
# A class is basically a structure you can use to then create an object in your code. 
# And what do you put inside the class? Well, two kinds of things. Variables and functions

# Creating a class doesn't add any functionality or special behavior. 
# It's just a different way to organize and write the code. 
#                                     
#Robot's attributies:                -> Robot            -> Class Name
#-Name                               -> Name            |
#-Version Number                     -> Version_number  | -> Attrubutes
#-Temprature                         -> temprature      |
#-Etc

#Robot's functionalities:
#-Say hi                             -> say_hi()        |
#-Print internal info                -> print_info()    | -> Methods
#-initialize its hardware            -> init_hardware() |
#-Etc

#Create a Python Class
#For example, to create a class it is very simple, you use the class keyword, and then the name of the class and then colon. 
# So class keyword name of the class, colon, and for the name of the class, we are going to use a different convention than before
#Here, you are going to use an uppercase letter, , for each new word, 

#everything that is indented is inside the class, everything that is not indented after that is outside of the class. 
# And well, the first thing we have to do in this Python class is to create a constructor. The constructor is a method.

#Remember, a class is just a structure, it does nothing by itself. You will need to create some objects, 
# so you can use the functionalities of the class. And when you create an object from the class, the first thing that is called is the constructor.
#So the constructor will always be the same def. So you create def, like you just create a function, and then __init__, and then you open parentheses, 

#- `Constructor`

class Robot:
    def __init__(self, name, version_number):
        self.name = name
        self.version_number = version_number
        self.internal_temprature = 25.0

#So the function, so the method here is indented inside the class Robot, and then we have yet another indentation here. 
# And I' have initialize the attributes by using self.name is equal to name, and then self.version_number is equal to version_number. 
# And then I have add self.internal_temperature is equal to 25, as a float.
#So when you use self, this actually refers to the object, related to class Robot. 
# how to make the difference between a simple variable and an attribute of the class? Well for an attribute of the class you're simply going to use that self and to self., 
# then for e.g., name. So here, the name is the parameter. So this is a local variable inside this method, , if you remember from the scope. self.name, is actually in the class.

#Add Class Methods
#Now that we have the structure of the class, we have the constructor and the attributes, let's implement the methods of the class or in other words, the functionalities of the class. 
#we have already actually our first method, which is the constructor. 
# Now we can add any number of methods we want in the class, so still with the indentation to stay inside of the class.

#- `Methods`

    def say_hi(self):
        print('Hello my name is' + self.name + 'ready, for help')

    def init_hardware(self):
        print('init hardware')

    def print_info(self):
        self.say_hi()
        print('version number' + str(self.version_number))
        print('Temprature' + str(self.internal_temprature))

#so in this method, you can see we've got another method and we use the different attributes. 
# so self, and the attributes. If you want, you can also modify the attributes, . You just do self.version_number is equal to and they just change it

# now we have a constructor, we have three attributes, and we also have three methods inside the class. All right, 
# we have successfully written all the functionalities of the class inside different methods.
        

# If you executed the class, well, nothing happened. So just as we have seen with a function, well, 
# a function is just a bunch of code that you need to call in your program, otherwise, it won't do anything

my_robot = Robot('R2D2', 2)
my_robot.say_hi()
my_robot.init_hardware()
my_robot.print_info()

my_robot2 = Robot('C3P0', 1)
print(my_robot.name)
my_robot2.print_info()


#CONCLUSION:
#So to recap, in order to create an object from a class, you need to write the name of the class first, to call the constructor and pass the required parameters to initialize attributes. 
# Then from that object, you can call the class methods. You can also create multiple objects from the same class, and each object will have its own internal mechanism and attributes independent from the other objects.

#Inheritance - Derive a Class from Another Class

#This class is actually a Robot, but with more functionalities, okay that are specific to robotic arm. 
# So to create the robotic arm class, you will need to rewrite most of the Robot class code here, and there is a way to avoid doing that and directly create the robotic arm class on top of this Robot class. This is called inheritance
#So basically, if I just write this, and then if I do pass, which is basically the Python keyword, to do nothing
#And here, if a class inherits from another class, what you can do inside the method is called a super function. And this super function is simply going to call a method that is from the, what we can call the mother class,


#Composition - Use a Class Inside Another Class


#one last thing I want to show you about Python OOP is the concept of composition. 
# Let's say that now you have to work with a packaging solution. This packaging solution is nothing more than two robotic arms assembled together to work on an assembly line. 
# What you can do here is to create a class, create a new class here, class PackagingSolution, and inside this class, you're going to keep and use two instances of the RoboticArm class. This is what we call composition. Basically, when you use an object, okay, from another class, inside of a class
