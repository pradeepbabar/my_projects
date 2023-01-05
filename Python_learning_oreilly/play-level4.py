#Use a python level 4

#Read from a file
with open("file_test.txt", "r") as f:   #here function open will open the file "r" means read permission & f is variable
    print(f.read())                     #read function here will read txt file

#\n for new line
#write to file

with open('write_file', 'w') as d:  #here file created by mentioning name & 'w' to write file NOTE:this will not append
    d.write('hello world')          #write to write the operation, if 

#append to file
with open('write_file', 'a') as e:  #here 'a' use to append it will not replace word but add it
    e.write('kem choe \n majama \n ha bapu \n moj')

#NOTE: 'w+' in this mode you can write & read to the file
#NOTE: 'a+' in this mode you can append & read to the file
