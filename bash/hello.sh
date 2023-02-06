#! /bin/bash
#by above comment interpreter will come to know that it is bash file

echo "Hello World!" #this is also a comment

echo $bash
echo $bash_version
echo $HOME
echo $PWD

name=MArk
echo The name is $name

#Read User Input

echo "Enter Names: "
read name1 name2 name3 #whenever you need input from terminal use read command
echo "Entered name: $name1, $name2, $name3"

#Read User Input on same line
read -p 'username:' user_var #-p userinput for sameline
echo "username : $user_var"
read -sp 'password:' pass_var #-sp userinput for silent for password
echo "password : $pass_var"

#allow thhe user for multiple input and read an array
echo "Enter names:"
read -a names
echo "Names: ${names[0]}, ${names[1]}"

#built in variable called replay
echo "Enter name:"
read
echo "Name : $REPLAY"