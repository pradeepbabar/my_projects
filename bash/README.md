##Introduction to BASH

## Writing first scripts in BASH
- `BASH`: On linux system BASH is default shell
- `bash version`: to know the bash version
- `vi [filename]`: to edit file in vi editor
- `pwd`: to print current working diretory
- `bash [filename]`: to run the bash file
- `ls`: list the files
- `cat`: to see the file content
- `ls -l [old_filename] {something weired} &> [new_filename]`: Here &> ampersign & greater then sign will print both the out put in new file.
- `Types of Files`: 
Regular Files (-):this contains programs, executables files & tst files
Directory Files(d): it is shown in blue color it contains list of files
Special Files(d): Block file (b), Character device fule (c), Named pipe file(p), Symbolic link file(l), Socket file (s)

centos#ls -l
-rwxr-xr-x. 1 centos centos 114 Feb 2 01:52 [filename]

- `First Column` − Represents the file type and the permission given on the file. Below is the description of all type of files.

- `Second Column` − Represents the number of memory blocks taken by the file or directory.

- `Third Column` − Represents the owner of the file. This is the user who created this file.

- `Fourth Column` − Represents the group of the owner. Every user will have an associated group.

- `Fifth Column` − Represents the file size in bytes.

- `Sixth Column` − Represents the date and the time when this file was created or modified for the last time.

- `Seventh Column` − Represents the file or the directory name.

https://cloud-and-devops.hashnode.dev/linux-for-beginners#heading-file-permissions

Modifying permission via chmod:
This is used to modify the file permission for Users, Groups and Others

Changing Owner via chown:
This is used to modify the owner of a file

chown <owner name> <file>

Changing Group via chgrp:
This is used to modify the group of the file.

chgrp <group name> file

Checking access control lists using getfaclL
The getfacl command is used on Linux to print a complete listing of all regular permissions and access control lists permissions on a file or directory.

getfacl <file/directory>

Setting access control lists using setfacl:
The setfacl command is used on Linux to create, modify and remove access control lists on a file or directory.

setfacl {-m, -x} {u, g}:<name>:[r, w, x] <file, directory>

setting

