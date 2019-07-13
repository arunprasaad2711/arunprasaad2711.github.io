
# Shell Programming

## Source
* Shell Scripting Tutorials - "The Bad Tutorials" - YouTube channel.
* Unix and Shell Programming - "Fuzicast" - YouTube channel.

Basic programming language for Unix. Applicable for Linux as well. Shell is the interface between the linux kernel and the user. The kernel makes the hardware do the job!

There are different types of shell.

* Bash
* sh
* csh
* tcsh
* ksh

All of them are similar and have some small differences.

To access a shell, start a terminal.

## Inside the terminal

On opening the terminal, there will be a line like below.

```
arun@hpdv6:~$
```

It stands for username followed by machine name. The ~ sign shows the path and ```$``` is the command prompt. All commands are in lowercase.

## Basic commands

**clear** - clears the terminal screen

**who am i** - Prints the username, terminal id and the time/date of logging in

**pwd** - prints the present working directory

**mkdir** - make a directory.

```bash
mkdir folder1 folder2
mkdir path/of/folder/folder_name
```

**rmdir** - delete a directory.

```bash
rmdir folder1 folder2
rmdir path/of/folder/folder_name
```

**ls** - list the contents of the present working directory

**cal** - prints the calendar month and highlights the current day. To print the calendar of some other month and year, use 

```bash
cal month_number year
cal month_name(short/long) year
```

**date** - prints the day, month, date, year, full 24-hour time and time zone. To custom represent time, use the format.

```bash
date +'DATE:%m-%y%nTIME:%H:%M%S'
```

m - month, y - year, n - new line, H - hour, M - minute, S- seconds

**touch** - used to create empty text files.

```bash
touch test1 test2 test3
```

**cd** - change directory

```bash
cd new/path
```

**cat** - used to write contents inside the text files. Also used to read the contents.

```bash
cat > filename #Press enter
# write contents # terminate using CTRL+D

cat < filename #press enter. 
#This will display the cotents of the file. 
#The lesser than symbol is optional, but use it as a practice.

cat file1 file2 > file3
# merges file1 and file2 into file3
```

**mv** - move file/folder. Also, used for renaming file/folder

```bash
mv path/to/filename1 path/to/filename2
```

**rm** - removes file/folder. Use -r flag to remove folders.

```bash
rm file
```

**cp** - copy files

```bash
cp path/to/source path/to/destination
```

**ln** - link files

```bash
ln source_file target_file.
# now, if any modification is done to "source_file", then the 
# modifications are reflected in "target_file" - hard link
# Now, if the source file is deleted, then the target file will
# be intact.
ln -s source_file target_file
# This creates a short-cut.
```

## Comments

Use **#** to start a single line comment.

```bash
# this is a single-line comment
<<COMMENT
This is a multi-line
comment. It extends for several lines.
This is one way using manual delimiters.
COMMENT
<<!
This is another multi-line
comment. It extends for several lines.
This is another way using manual delimiters.
!
```

## File permissions

Files and folders have certain permissions: read, write and execute. The permissions have numerical values: read-4, write-2, execute-1. Based on the permissions, a file that is created or modified has a numerical value which is the sum of the numerical values associated with the permissions. A file will have the numeric values 4(read-only), 5(read and execute), 6(read and write), 7(read,write,execute).

And there are three categories of users: owner(the one who created the file), group(the group of users in the system/network) and others(users outside the system/network). And depending on the category of the users, the permission privileges vary.

The command **``` umask ```** tells what kind of permissions exist for the files and folders when created.

On typing the command **``` umask ```**, a 4 digit number like **0022** or **0002** might show up. The first zero on the left is for indicating Octal numbers. The second digit is for the owner, the third digit for group and the fourth digit for others.

Whenever a file/folder is created, the Linux/Unix OS subtracts the **umask** value from **0777** for the files and **0666** for the folders. So, for a file, if the resulting number turns out to be **0755**, it means the owner has all three premissions, while others and group can only read and execute.

**Folders need execution permission! Otherwise, they cannot be accessed!**

## ls command

**ls** lists all the files and folders in the folder.
```bash
ls path/to/folder 
# lists all the files and folders in the path specified.

ls -l             # l - long listing flag
# lists all the files and folders with permissions
# , user details, date/time of modifications
```

On typing ``` ls -l ```, one might get an output like this:

```bash
total 100
drwxrwxrwx  8 arun arun  4096 Sep 28 21:55 Academic_Stuff
drwxrwxr-x 18 arun arun  4096 Oct 10 05:50 anaconda3
drwxr-xr-x  9 arun arun  4096 Oct  7 03:49 Desktop
drwxr-xr-x  2 arun arun  4096 Sep  3 19:26 Documents
drwxr-xr-x  5 arun arun  4096 Oct 15 11:47 Downloads
drwxrwxrwx  3 arun arun  4096 Jul  3 00:21 Drive
drwx------ 22 arun arun  4096 Oct 15 08:22 Dropbox
-rwxrwxrwx  1 arun arun  8980 Jul  9 19:37 examples.desktop
drwxrwxrwx  4 arun arun  4096 Jul  9 23:39 Google_Drive
drwxrwxrwx  4 arun arun  4096 May  6 16:25 hp_usb
drwxr-xr-x  2 arun arun  4096 Aug 21 03:31 Music
drwxrwxrwx  2 arun arun  4096 Jun 29 15:56 pen_drive
drwxr-xr-x  3 arun arun  4096 Sep 29 00:15 Pictures
drwxrwxrwx 29 arun arun  4096 Aug 22 01:09 Program_Workspace
drwxr-xr-x  2 arun arun  4096 Aug 21 03:31 Public
-rw-rw-r--  1 arun arun 11221 Sep 28 14:25 simrad_transp_sw_opaq_lw.m
drwxrwxrwx  8 arun arun  4096 Aug 21 21:27 Software
drwxr-xr-x  2 arun arun  4096 Aug 21 03:31 Templates
drwxr-xr-x  3 arun arun  4096 Oct 15 16:09 Videos
drwxrwxr-x  3 arun arun  4096 Oct 16 14:45 VirtualBox VMs
```
The value ``` total 100``` indicates the total number of blocks occupied by all the files and folders in the directory. Here, it is 100 blocks. 1 block is a unit of memory for file allocation in unix/linux which is equal to a certain amount of bytes.

The first column is a 10 units long string. For a file, the first unit of the string is a **-**, whereas for a folder, it is **d** indicating that it is a directory.

Units 2-4, 5-7 and 8-10 indicate the permissions for the owner, group and others. **r** means read, **w** means write and **x** means execute. Here, **-** means that permission is absent.

Column 2 (i guess) indicates the number of blocks occupied by the file or folder.

Column 3 and 4 indicated the owner and the group name.

Column 5 indicates the size of the file in bytes. For folders, it indicates the size of the parent folder alone without any of the contents inside it.

Column 6-8 indicate the date and time of creation/last modification/access of the file or folder.

Column 9 indicates the file/folder name.

### Creating hidden files

Put a dot infront of the file name to hide it.

Use ``ls -a`` to list ALL files, including hidden files.

## chmod command

Changes the file/folder permissions manually.

```bash
chmod 777 filename
# makes the permission string for the file as -rwxrwxrwx
chmod 444 filename
# makes the permission string for the file as -r--r--r--
chmod 755 filename
# makes the permission string for the file as -rwxrw-rw-
chmod -w filename
# Removes write permissions for the file
chmod +x filename
# Adds write permissions for the file
```

Minus sign **-** is used to remove a permission. Plus sign **+** is used to add permission. The permissions are read, write and execute **r,w,x**.

Executable files are displayed in **green** colour inside the terminal.

## uname command

Prints the kernel and some system details of the OS.

```bash
uname
uname -a # list all details
```
The output is:
```
Linux
Linux hpdv6 4.4.0-42-generic #62-Ubuntu SMP Fri Oct 7 23:11:45 UTC 2016
x86_64 x86_64 x86_64 GNU/Linux
```
The details are in order: Kernel name, device name, Kernel version, OS name with some specification, Memory Architecture - SMP means Shared memory Processor, Date and time of installing/updating the kernel, Assembly language of the system for owner(x86_64 - assembly language for 64 bit systems), group and others, Kind of Unix/Linux.

## File and wc command

File command mentions the file type/directory in a given path.

```bash
arun@hpdv6:~/Desktop/Python_Session/main$ file *
demo.ipynb:                 ASCII text, with very long lines
eVSes.png:                  PNG image data, 1200 x 800, 8-bit/color RGBA, 
                            non-interlaced
eVsZ.png:                   PNG image data, 1200 x 800, 8-bit/color RGBA, 
                            non-interlaced
IISc_logo.jpg:              JPEG image data, JFIF standard 1.01, resolution
                            (DPI), density 150x150, segment length 16, 
                            comment: "Software: Microsoft Office", baseline, 
                            precision 8, 555x523, frames 1
IQ_hist.png:                PNG image data, 1200 x 800, 8-bit/color RGBA, 
                            non-interlaced
iris_ex01.py~:              Python script, ASCII text executable
ncfile1.nc:                 NetCDF Data Format data
ncfile2.nc:                 NetCDF Data Format data
python.png:                 PNG image data, 518 x 588, 8-bit grayscale, 
                            on-interlaced
Python_Session.html:        HTML document, ASCII text, with very long lines
Python_Session.ipynb:       ASCII text, with very long lines
Python_Session.slides.html: HTML document, ASCII text, with very long lines
rain_data2.txt:             ASCII text
rain_data.txt:              ASCII text
sample.ipynb:               ASCII text, with very long lines
sample.slides.html:         HTML document, ASCII text, with very long lines
swiss_knife.jpg:            JPEG image data, Exif standard: [TIFF image 
                            data, little-endian, direntries=0], baseline, 
                            precision 8, 2908x2248, frames 3
```

**wc** shows the number of lines, words and characters in a file.

```bash
arun@hpdv6:~/Desktop$ wc simulation_group.txt # use -l, -w, -c to display
                                         # only lines, words or characters
 31  76 468 simulation_group.txt
```

## Sort command

Extracts all the words and sorts the contents in a file.

```bash
sort filename.ext
```
Typing plain sort opens the terminal to write words. When pressing Ctrl+D, the words are sorted and displayed.

## Cut command

Used to cut the contents in the file and separates them.

```bash
cut -d"-" -f 1,3 filename
# -d means explaining other characters are used to separate the data.
# "-" is used for specifying the separator here
# -f means the fields
# 1, 3 column numbers in the file
# filename
```

## dd command

Used to convert and copy files from one format to another.

```bash
dd if="test" of="out" conv=ucase
## if = input file
## of = output file
## conv = type of conversion, here, the contents become uppercase.
dd if="test" of="out" conv=ebcdic
## here, the contents get converted into European format.
```

dd is used for formatting drives, extracting data from drives, copy files to drives, convert files from/to drives.

## man command

Used for displaying the manual for a command.

```bash
man command-name
```

Opens a reference manual with all flags, syntax, options, details etc.,
Press **q** to quit the manual.

## Banner command

Creates a banner

```bash
arun@hpdv6:~$ banner text # can use "" for using a single string

  #####  ######  #    #   #####
    #    #        #  #      #
    #    #####     ##       #
    #    #         ##       #
    #    #        #  #      #
    #    ######  #    #     #

arun@hpdv6:~$ 
```
Only 10 characters (including whitespaces) will be displayed per line.

## Compress command

Used to compress files.

```bash
compress -v filename
# output will be filename.Z
```

To read the compressed file inside terminal, use **zcat**

```bash
zcat filename.Z
```

To uncompress the file, use **uncompress** command.

```bash
uncompress filename.Z
```

## echo command

Used to print contents in the terminal. Echo automatically puts a newline character at the end.

```bash
echo "Hello World!"
```

## Running shell scripts

* Create shell scripts with the extension \*.sh
* Write the code inside the shell script one after the other
* Run them in the terminal using the command

```bash
sh filename.sh
bash filename.sh
```

## Creating Variables

Variables are case sensitive. They can't start with numbers. Only underscores are allowed. Variables can start with an underscore.

**Shell stores the values as strings by default! So, we need to specify the data type to the variables for mathematical computation.**

```bash
# local variable - available only in the file
a=25
# global/environment variable - available as long as the terminal is active
export b=50
```
**There should be no _space_ between the variable, the equal sign and value**

## Read command

Used to read variable data from the user.

```bash
echo "Please enter a name:"
read my_name # this is a variable to read the user data
echo "Hello $my_name! How are you?"
# To use the variable data, put a dollar infront of the variable.
# Also, the info is taken as a string in this context.
```

## Assigning variables and values in the terminal.

When you open the terminal, if you create an assignment expression like ** a = 25**, or ** b = "hello"**, then the variables are created with the values assigned to them. On typing **echo \$a ** or ** echo \$b**, it is going to display the values. Variables can be re-assigned with new values.

## Position Parameters.

Position parameters are run-time data provided by the user while running the file.

```bash
# program name : ssh5.sh
mv $1 $2
cat $2
```

This file is executed as follows.

```bash
:~$ ssh5.sh filename1.txt filename2.txt
```

Here, **filename1.txt** is taken as the first position parameter, while **filename2.txt** is taken as the positional parameter 2. So, this file ** ssh5.sh**, in this line will rename filename1.txt as filename2.txt and shows the contents of filename2.txt in the terminal.

Using the **set** command, multiple positional parameters can be set!

```bash
:~$ set Hello there everyone!
:~$ echo $1
Hello
:~$ echo $2
there
:~$ echo $3
everyone
:~$ echo $* # Prints all the positional parameter values
Hello there everyone!
:~$ echo $# # Prints the number of positional parameter values
3
```

## Reverse quotes/Accent graves

Used for writing/passing a command as an argument/positional parameter/data to another command. **If you want the output of a command or a statement to be passed to some other command or variable, then use reverse quotes**

```bash
:~$ set `cat filename`
```

In this example, because of the reverse quote, the contents of the filename are passed as data to the set command to create positional parameters.

**Reverse quotes are useful for creating subshells with output return**

## Subshells

Subshell is like a shell within a shell. Used for executing statements and get their results passed to some other command or variable. Subshells inherit all the enivironment/global variables from the parent shell.

```bash
# Creating a subshell and executing ls command inside it.
filename=(ls -ltr)

# Creating a subshell and executing ls command inside it.
# Also, using the dollar sign, we extract the output from
# the subshell
filename=$(ls -ltr)

# Same as above!
filename=`ls -ltr`
```

## Arithmetic Operations

The command **expr** is used for doing arithmetic calculations/operations using the values. Use **echo** keyword and reverse quote to print the results. **expr works only for integers!** Another way is the usage of square brackets and circular brackets.

```bash
a=20 b=30  # Creating two variables
echo `expr $a + $b`    # Addition
echo $[ $a + $b ]      # Addition
echo `expr $a - $b`    # Subtraction
echo $[ $a - $b ]      # Subtraction
echo `expr $a \* $b`   # Multiplication
echo $[ $a \* $b ]     # Multiplication
echo `expr $a / $b`    # Division
echo $[ $a / $b ]      # Division
echo `expr $a % $b`    # Modulus
echo $[ $a % $b ]      # Modulus
echo `expr $a \* \( $b + $c \) / $d`    # A mathematical expression.
echo $[ $a * $(( $b + $c )) / $d ]  # Alternate safe way 1
echo $[ $a * (( $b + $c )) / $d ]   # Alternate safe way 2

# Completely different approach
let "c=$a+$b"
echo $c
((c=$a+$b))
echo $c
```
Parenthesis and asterix are reserved symbols. So, you need to escape them out using escape sequences!. But, when using square brackets, you do not have to escape them out! When circular brackets are used, then the comparison operators are escaped out!

**While evaluating with \$[] or ((...)), space is not a problem around brackets**

Operator precedence : Parenthesis, Division, Multiplication, Modulus operation, Addition, Subtraction.

For working with floating point numbers/operations, we need to use the **bc** command/program. Use the pipe symbol, **|** to re-direct the output of the mathematical expression to the command/program **bc**.

```bash
a=20.5 b=30.4  # Creating two variables
c=`echo $a + $b  | bc`   # Addition
d=`echo $a - $b  | bc`  # Subtraction
e=`echo $a \* $b | bc`  # Multiplication
f=`echo $a / $b  | bc`  # Division
```

## Escape Sequence

```
\n - newline
\r - carriage return - overwrites the previous line.
\t - tab character
\b - backspace - clears one previous printed character
\c - continue - cancels newline escape sequence
\033[1m ....... \033[0m- To make the printed text bold
\033[7m ....... \033[0m- To make the printed text have reverse fg and bg colours.
```

## tput command

**tput** is used for doing a wide variety of operations.

```bash
tput clear # clear terminal
tput lines # prints the number of rows/lines in terminal
tput cols # prints the number of columns in terminal
tput cup 15 20 # Move the cursor to line 15, column 20
tput bold # prints the next lines bold
# use echo \033[0m ..... to deactivate the bold effect from tput.
```

## Exit status

Whenever a command is executed, a value is associated. If the command is successful, then the value is 0, else it is 1. These values are exit status values. To see if the command is successful check the status variable **?**. If an illegal condition is given, then the exit status is 2.

```bash
arun@hpdv6:~$ mkdir sample
arun@hpdv6:~$ echo $?
0
arun@hpdv6:~$ mkdir sample
mkdir: cannot create directory ‘sample’: File exists
arun@hpdv6:~$ echo $?
1
```

## If else statements

```bash
if <condition1/command1> 
then
    statement_set1
else
    statements_set_final
fi
```

Example
```bash
# space after the starting square bracket and 
# before the  closing square bracket
# is necessary
# -gt - greater than
# -lt - less than
# -ge - greater than or equal to
# -le - less than or equal to
# -eq - equals
# -ne - not equals
# then keyword has to be in the next line
if [ $num -lt 10 ]
then
    echo "Number less than 10"
elif [ $num -gt 20 ]
then
    echo "Number greater than 10"
else
    echo "Number between 10 and 20"
fi

if [ $num -lt 10 ]; then
    echo "Number less than 10"
elif [ $num -gt 20 ]; then
    echo "Number greater than 10"
else
    echo "Number between 10 and 20"
fi

if [ $[ $num1 + $num2 ] -lt 10 ]; then
    echo "Number less than 10"
elif (( $[ $num1 + $num2 ] > 20 )); then
    echo "Number greater than 10"
else
    echo "Number between 10 and 20"
fi
```

Use the keyword **exit** to terminate programs. Use **exit** to terminate any program anywhere abruptly. Use **exit 0** to indicate successful termination to get a **0** exit status.

Use the keyword **break** to terminate loops.

Use the keyword **continue** to skip the current loop.

## Meta characters

Semi-colon **;** is used for displaying multiple commands in a single line.

```bash
ls ; cal ; banner "hello"
```

Avoiding if else in some cases. Here, if the word was found in the file, then the lines would be copied to a new file. And if the entire process is successful, it will print the **echo** statement. For that, use **&&**. If the first statement fails, then the **echo** statement does not work. If the second command has to work irrespective of the outcome of the first statement, use **||** operator.

```bash
grep -i word filename > patterns && echo "The task was completed"
grep -i word filename > patterns || echo "The task may be completed"
```

**&&** and **||** are logical **and** and logical **or** operators for multiple expressions. ***They can be used with if else constructs***

## File types

There are a few types of files

* Character special files - normal character files
* Block special files - have binary code - eg: images, videos, special files
* Directory special files - folders
* Empty files - zero byte file

Program to check if a specified file exists or not

```bash
echo " Enter a file name:\c"
read fname
if [ -f $fname ] # if the file exists
then
    echo "This file exists"
elif [ -d $fname ] # if the name is a directory name
then
    echo "This is a directory"
elif [ -c $fname ] # if the name is a character special file
then
    echo "This is a character file"
elif [ -b $fname ] # if the name is a block special file
then
    echo "This is a block file"
else
    echo "This is something else"
fi

if [ -r $fname ] # if the file has read permission
then
    echo "This file has read permission"
fi

if [ -w $fname ] # if the file has write permission
then
    echo "This file has write permission"
fi

if [ -x $fname ] # if the file has execute permission
then
    echo "This file has execute permission"
fi

if [ -s $fname ] # if the file has non-zero size
then
    echo "This file has non-zero size"
fi
```

## String comparisons

```bash

str1="Hey there!"
str2="What is up?"
str3=
#str4=""
# str3 and str4 are null variables

# If condition is true, then exit staus is 0, if false, then exit status is 1
# compare the two strings for equality as a command and get an exit status
[ "$str1" = "$str2" ]
echo $?

# compare the two strings for inequality as a command and get an exit status
[ "$str1" != "$str2" ]
echo $?

# check the length of a string is non-zero
[ -n "$str1" ]
echo $?

# check the length of a string is zero
[ -z "$str3" ]
echo $?

```

## Logical Operators

```bash

! not operator
-a and operator
-o or operator

# Checks if a number is between 50 and 100
if [ $num -le 100 -a $num -ge 50 ]
```

## User inputs

The user input has one additional character than what is entered by the user, namely the return key.

**So, if the user enters just _one_ character/symbol, then the return key gets attached to it like an EOL character**

## A counting program

```bash

echo "Enter a file name:\c"
read var
# Prints Variable var. The result is pipelined to wc command which
# counts the number of characters and -eq (equality) operator checks
# if it is equal to 2
if [ `echo $var | wc -c` -eq 2 ]
then
    echo "You entered a character"
else
    echo "You entered something else"
fi
```

## Case statement

This program gets a variable and checks its type

```bash
echo "Enter a variable:\c"
read var
case $var in
[a-z]) # Checks if the character lies between a and z
    echo "You entered a lowercase character";; # End of a case
[A-Z])
    echo "You entered an uppercase character"
    ;;
[0-9])
    echo "You entered a digit"
    ;;
?)     # Substitution for one character
    echo "You entered a special symbol"
    ;;
*)     # Substitution for more than one character
    echo "You entered multiple characters"
    ;;
esac
```

```bash
echo "Enter a word:\c"
read word
case $word in
[aeiou]* | [AEIOU]* ) # Checks if the first letter of the word is a Vowel
    echo "Word starts with a vowel"
    ;;
[0-9]*) # Checks if the first letter of the word is a number
    echo "Word starts with a number"
    ;;
*[0-9]) # Checks if the last letter of the word is a number
    echo "Word ends with a number"
    ;;
???)     # Checks if it is a three character word
    echo "You entered a three character"
    ;;
*)     # Some other condition
    echo "Some other n/a word"
    ;;
esac
```

## While loop

While loop executes instruction till the condition becomes false.
```bash

count=1
while [ $count -le 10]
do
    echo $count
    count=`expr $count + 1`
done

```

## Until loop

Untill loop executes instruction till the condition becomes true.

```bash

count=1
until [ $count -ge 10]
do
    echo $count
    count=`expr $count + 1`
done

```

## For loop

This program scans the folders/files in the present working directory and display the name of the folders only.

```bash

# item takes one value in each iteration
for item in *
do
    if [ -d $item]
    then
        echo $item
    fi
done
```

## Command line arguments

``@`` is useful for extracting command line arguments.

```bash
# filename is args1.sh
for args in $@
do
    echo $args
done
```

```
arun@hpdv6:~$ bash args1.sh hello there i am arun
hello
there
i
am
arun
```

## grep command

grep = globally search a regular expression and print.

Used to search for patterns in text files.

```bash
# searches for the word "money" in the file "filename"
grep money filename

# searches for the word "money" in the file "filename"
# -i means case insensitive
grep -i money filename

# searches for the word "money" in the file "filename"
# -i means case insensitive
# -n means line numbers
grep -i -n money filename

# searches for the word "money" in the file "filename"
# -i means case insensitive
# -n means line numbers
# -c prints the number of lines having the pattern
grep -i -n -c money filename

# searches for the word "money" in the file "filename"
# -i means case insensitive
# -n means line numbers
# -c prints the number of lines having the pattern
# -v prints the number of lines not having the pattern if -c is present
grep -i -n -c -v money filename

# searches for the word "money" in the file "filename"
# -i means case insensitive
# -n means line numbers
# -v prints the lines not having the pattern
grep -i -n -v money filename
```

## passwd file

This file is present in **/etc/** folder. It has many useful and vital info about the users and account details. You have read permissions, but you cannot modify it. **DO NOT MESS WITH THIS FILE**. The system uses this file for many operations. If tampered or deleted, then depending on the level of tampering, the system programs may stop working or the OS might not boot up.

It has user information and information about system programs and other special programs that have vital functions. This is an example of how a passwd file looks like.

```bash
arun@hpdv6:~$ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-timesync:x:100:102:systemd Time Synchronization,,,:/run/systemd:/bin/false
systemd-network:x:101:103:systemd Network Management,,,:/run/systemd/netif:/bin/false
systemd-resolve:x:102:104:systemd Resolver,,,:/run/systemd/resolve:/bin/false
systemd-bus-proxy:x:103:105:systemd Bus Proxy,,,:/run/systemd:/bin/false
syslog:x:104:108::/home/syslog:/bin/false
_apt:x:105:65534::/nonexistent:/bin/false
messagebus:x:106:110::/var/run/dbus:/bin/false
uuidd:x:107:111::/run/uuidd:/bin/false
lightdm:x:108:114:Light Display Manager:/var/lib/lightdm:/bin/false
whoopsie:x:109:116::/nonexistent:/bin/false
avahi-autoipd:x:110:119:Avahi autoip daemon,,,:/var/lib/avahi-autoipd:/bin/false
avahi:x:111:120:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/bin/false
dnsmasq:x:112:65534:dnsmasq,,,:/var/lib/misc:/bin/false
colord:x:113:123:colord colour management daemon,,,:/var/lib/colord:/bin/false
speech-dispatcher:x:114:29:Speech Dispatcher,,,:/var/run/speech-dispatcher:/bin/false
hplip:x:115:7:HPLIP system user,,,:/var/run/hplip:/bin/false
kernoops:x:116:65534:Kernel Oops Tracking Daemon,,,:/:/bin/false
pulse:x:117:124:PulseAudio daemon,,,:/var/run/pulse:/bin/false
rtkit:x:118:126:RealtimeKit,,,:/proc:/bin/false
saned:x:119:127::/var/lib/saned:/bin/false
usbmux:x:120:46:usbmux daemon,,,:/var/lib/usbmux:/bin/false
arun:x:1000:1000:Arun,,,:/home/arun:/bin/bash
sddm:x:122:130:Simple Desktop Display Manager:/var/lib/sddm:/bin/false
nvidia-persistenced:x:121:129:NVIDIA Persistence Daemon,,,:/:/sbin/nologin
```

Taking one entry and dissecting the 7 fields (separated by :),

```bash
root:x:0:0:root:/root:/bin/bash
```

First field is the user name or the program name.

Second field is the password. If there is a **x**, then it means that the information is encrypted. Passwords are stored in the **shadow** file in the same folder and we do not have permissions to open/read that file.

Third field is the User ID or UID. For root user, it is 0. UID 1-99 are pre-defined/reserved for system accounts that were created at the time of installation of OS. Beyond 99, the UIDs are defined for system accounts created afterwards.

Fourth field is the group ID. Name ID notations as above.

Fifth field is the name of the program/pc/user name etc., Also known as comment field.

sixth field is the home folder or the folder where the program is present

Seventh field is the default binary file (or shell) for doing stuff with the program/user

## Internal file separator

If there are multiple parameters in a command, the internal file separator is used by the shell to differentiate the parameters. Usually the IFS is **space** and **return**. IFS can be modified manually. If modified, it presists till the terminal is active.

```bash
IFS=: # modifies the IFS with :
```

## Read and display info from passwd file

```bash

echo "Enter user name:\c"
read logname
IFS=:
line=`grep $logname /etc/passwd`
set $line
echo "Username = $1"
echo "Password = $2"
echo "User ID = $3"
echo "Group ID = $4"
echo "Comment = $5"
echo "Home folder = $6"
echo "Shell folder = $7"
```

## Read from a file / Use file as input

```bash

echo "enter a file name:\c"
read filename

if [ -z "$filename" ] # checks if the file is empty
then
    exit
fi

# Setting up a variable/filename so that the keyboard input stream
# is stored separately

terminal=`tty`

# Executing the filename - getting the inputs from the file
exec < $filename

count=1

# read lines one by one and print them
while read line
do
    echo $count.$line
    count=`expr $count + 1`
done

# Return the input stream to the keyboard

exec < $terminal
```

## Sleep command

Used to produce time delay in seconds.

```bash
sleep 5 # 5 second delay
```

## Program to count the number of words and lines in a file

```bash

echo "Enter the filename:\c"
read fname

terminal=`tty`

exec < $fname

nol=0
now=0

while read line
do
    nol=`expr $nol + 1`
    set $line
    now=`expr $now + $#`+
done

echo "Number of lines:$nol"
echo "Number of words:$now"

exec < $terminal

```

## Device null

If a command returns a lot of output and the output has to be suppressed without losing or modifying the exit status, then device null is useful. The output of the command can be redirected to this file. This file will take the output and removes it and helps the command execute successfully.

```bash
who | grep "$logname" > /dev/null
# the output of command who is pipelined to grep.
# the output of grep is sent to the null file.
# the output of grep file gets deleted by the null file and
# grep terminates safely without any error.
```

## Log in another user

If there are multiple users in the system, then one user can login through another using the login command.

```bash
sudo login
[sudo] password for mainuser
<OS> login: newuser_name
password: password_newuser
```

For the user to logout, use the keyword **logout/exit**.

## Send / Receive messages to user(s)

Users can send/receive messages via terminal.

To enable users sending/receiving messages, use the keyword **mesg**. To write a message to the user, use the **write** command.

```bash
mesg y # enable message
mesg n # disable message

write user2
[write contents]
[Terminate with Ctrl+D]
```
On pressing **Enter** key, the information is sent to user2 and the message gets displayed on the terminal of user2 with a timestamp. When user1 types **Ctrl+D**, the message to user2 terminates with an **EOF**, indicating the end of message and user2 can press **Ctrl+D** to close the message.

Command **finger** is useful for displaying the users who have enabled/disabled messages. Those who have disabled the service have an asterix \* on the **Tty**.

## Functions

One can create own commands using functions.

```bash
function_name()
{
    # commands
}
```
Create a file with all the functions you need. Make that file executable (using **chmod**) and run that file first. When successful, the functions can be called in the terminal or any other shell script afterwards. The functions are available as long as the terminal is open.

```bash
chmod +x func_file.sh
. func_file.sh # execute the file
./func_file.sh # execute the file, Alternate way
```

To remove a particular function from the terminal in that instant, use **unset** command.

```bash
unset function_name
```

## Running Multiple Shell Files

Use the line **bash filename.sh** inside another shell file.
