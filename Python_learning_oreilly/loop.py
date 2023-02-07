#Loops & iternation
#we can tell them to do it a millions times
#loops (repetaed steps) have iternation variables that change each time through a loop.
# here while will run exactly like an if statement
#  An below infinite loop this will drained out resources since condition is true
# while loops are called indefinite loops because they keep going until a logical condition becomes False
n = 0
while n > 0 :
    print('ruuning')
    print('again running')
print('drained out')

#break a loop
while True:
    line = input('> ')
    if line == 'done':
        break   # it will break a loop if input is done statement
    print(line)
print('Done !')


#continue a loop, continue says go back at top of the loop (it ends current iteration)
while True:
    line = input('> ')
    if line[0] == '#':
        continue   # it will go back to top of the loop
    if line[0] == 'done':
        break   # it will break a loop if input is done statement
    print(line)
print('Done !')

#Below loops are for loop
#An  definite loop are used for loops
# it is called 'definite loops' because they execute an exact number of times

friends = ['ram', 'rama', 'rahima']
for friend in friends:
    print('Happy new year:', friend)
print('Done!')

#loop idioms: wat we do in loops

