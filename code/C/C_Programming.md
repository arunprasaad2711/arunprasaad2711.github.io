# C Programming

<!-- TOC -->

- [C Programming](#c-programming)
	- [Sources:](#sources)
	- [Installation](#installation)
	- [Basics of C](#basics-of-c)
	- [Header Files](#header-files)
	- [Built-in Commands and Functions](#built-in-commands-and-functions)
	- [Data types and Symbols](#data-types-and-symbols)
- [C](#c)

<!-- /TOC -->

C is a compiled programming language Developed by Dennis Ritche in 1970's.

It is a programming language next to fortran in terms of speed and flexibility.

C has more options and features than fortran and for this reason, the C is preferred over fortran.

C has give rise to so many derived programming languages like

1. C++
2. Visual C, C++
3. C#
4. Objective C
5. CUDA C


All of them are based on C and are built/made using them.

C is also a part of other interpreted programming languages, games, operating systems, applications etc.,

## Sources:

* http://www.cprogramming.com/tutorial/c-tutorial.html
* http://www.physics.drexel.edu/courses/Comp_Phys/General/C_basics/
* http://gd.tuwien.ac.at/languages/c/cref-mleslie/CONTRIB/SAWTELL/intro.html
* http://en.wikibooks.org/wiki/C_Programming
* http://www.cprogramming.com/
* http://www.tutorialspoint.com
* http://www.codingunit.com/

Youtube Video lectures on C by

1. Bucky Roberts
2. Adam
3. Madhur Bhatia


Install Code Blocks as mentioned in Fortran tutorials.

If wanted to work in Linux/Unix environment, install a gcc/icc or any equivalent compiler and proceed.

## Installation

Installing C, C++ is fairly easy. In a Linux operating system like Ubuntu, just type the command in the terminal.
 
```bash
sudo apt install gcc g++
```

## Basics of C

The extension of c files is .c

There are main compilers for C Programs. The ideal choice of compiler is gcc in case of linux and unix.

The program start with pre-processing statements like

```C
#include<somefilename.h>
```

These are header files required to give definitions for commands and built-in functions used in C

```C
# is used for making an explicit definition to the compiler.

/*  contents  is used for a block comment. */
// contents is used for a single line comment.
```

There are quite a few changes between Borland C and GCC.

The entire program is written inside the main function

```C
main()
{
contents;
}
```

By default, the c compiler will first look for this function first. Only then, other functions will be handled/read. The main function can have a return statement if it returns a value. To make so, you need to assign it a return value

eg:  ``` int main or float main. ```

To make it return a value, use return statement.

eg:  ``` return 1, return 0 etc., ```

simple main (eg: main) or a main with no return type (eg: void main) is also allowed.

Any line of code written below return command will be ignored safely without any error.

All the lines in c are to be separated by ;

The entire program is written in terms of functions.

All the variables and commands are case sensitive!

Use \ command at the end of a statement to continue the statement into the next line.

Variable declarations can happen anywhere in the program, but it should be defined before it is used.

## Header Files

Header files have an extension ``.h``

Header files give explicit definitions to each and every command used in the program.

``stdio.h`` standard input and output. Has explanations to the basic keywords and statements in C.

``math.h`` has definitions for mathematical operations.

**Usually, Header files have "declarations" for the functions and commands. The actual contents are available in a separate C file. Header files pull the contents of the C file of the same name, except the extension into the C file**

## Built-in Commands and Functions
 
```C
printf("strings", vars);
```
This is used for printing and displaying contents on screen.
eg:
 
```C
printf("Simple Interest is: %f", si);
```

You can also print the variable's address. Use ``` %d ``` for the type specifier and & infront of the variable to indicate the address.
 
```C
scanf("type specifiers", &vars);
```

This is used for retrieving varaible values from the console. 

The variable addresses are sent as the arguments for scanf

eg:
 
```C
scanf("%d", &years);
```

The & is used for indicating the address of the variable.

While entering the values in the console, press enter or tab key after every value entry.
 
```C
sizeof(var)
```

This function returns in integer, the number of bytes occupied by the variable in memory.

* int occupies 4 bytes, 
* short int (or just short) occupies 2 bytes, 
* long int (or just long) occupies 4 bytes, 
* long long int (or just long long) occupies 8 bytes, 
* char occupies 1 byte, 
* float occupies 4 bytes, 
* double occupies 8 bytes, 
* long float occupies 8 bytes. 

This storage depends on the bit-technology of the compiler and OS.

But 
 
```C
	sizeof(char)=<sizeof(short)=<sizeof(int)=<sizeof(long)=<sizeof(long long);
```
 
```
break;
```

This is a command used for breaking a loop structure or a case structure. If a certain loop breaking condition is reached, use break to come out of the loop.
 
```C
continue;
```

This is a command used for skipping a particular iteration of a loop or a case structure without breaking out of the loop. To make this happen, use a condition or use this where a certain thing happens.
 
```C
goto
```

This is a statement used for shifting the line of execution from one point to another. It can also break loops and decision statements.

To make a goto statement work, you need a label along with it. The label is case sensitive.

eg:
 
```C
...
goto label1;
....

label1:
    ......
```

``goto`` is not preferred because it can complicate the programming by jumping the execution here and there. Also, if not done properly, you might end up with an infinite loop. goto with line numbers is worse because you may modify the code later and line numbers may change, thus ending with a confusing code. One has to be cautious while using this code.

## Data types and Symbols

There are 4 basic data types

int for integers. There are several types of integers,


* int occupies 4 bytes, 
* short int (or just short) occupies 2 bytes, 
* long int (or just long) occupies 4 bytes, 
* long long int (or just long long) occupies 8 bytes, 
* char occupies 1 byte, 
* float occupies 4 bytes, 
* double occupies 8 bytes, 
* long float occupies 8 bytes.


This storage depends on the bit-technology of the compiler and OS.

But in any system, 
 
```C
sizeof(char)=<sizeof(short)=<sizeof(int)=<sizeof(long)=<sizeof(long long)
```

float for real numbers (single precision numbers or precise upto 6-8 digits)

char for short numbers and characters.

strings are also available under char but in a different manner.

There is a double also (double precision numbers or precise upto 15-16 digits). It occupies 8 bytes.

Long double exists and it occupies 12 bytes (triple precision numbers 17-18 digits)

All the above integer number types fall in two categories - signed and unsigned. 

Signed numbers have half the range of the unsigned numbers, but they go into both positive and negative.

Unsigned values are always positive and include zero. By default the values are signed. 

To make them unsigned, use "unsigned" keyword infront of them.

In general, the range of signed integers is ``` -2^(8*n -1) to 2^(8*n -1) -1 ``` (n stands for the number of bytes)

In general, the range of unsigned integers is ``` 0 to 2^(8*n) -1```

``` void ``` is used for indicating that the variable/function will not return any value.

``` const ``` is used for making a constant in the program

eg:
 
```C
const int AREA = 4;
```

(constants, by practice have to be in upper case. they need not be in caps. Used to differentiate them from variables)


To place the variables inside strings (as in the case of print statements) or to get the values (in case of scan statements,) type specifiers or format specifiers are needed.

``%d`` or ``%i`` for integers/ number part of characters/short integers

``%li`` for long int

``%lli`` for long long int

``%c`` for character

``%f`` for float/double

``%llf`` for long double

``%s`` for string.

``%e`` for printing numbers in scientific notation.

``%u`` for unsigned integers/characters/short integers

``%lu`` for unsigned long int

``%llu`` for unsigned long long int

``%o`` for octal numbers

``%x`` for hexa-decimal numbers lower case

``%X`` for hexa-decimal numbers upper case

``%%`` to print the percentage sign.

use ``%lf`` in the scanf function to get double numbers.

use ``%f`` for printing them.

No type specifier for binary.

This can be edited also.

``%5.3f`` indicates that in a field of 5 spaces, allocate 3 spaces for digits to the right of the period, 1 for the point and the rest for the digits to the left of the period (with or without sign)

Both the whole number and decimal number part are optional, but good to add them for specific output formats. Some examples are:
 
```C
	printf("%d\n",b);
	printf("%3d\n",b);
	printf("%03d\n",b);
	printf("%3.2f\n",d);
```

   The outputs are
 
```
   7   70075.10
```

Other examples are:
   
``%d`` (print as a decimal integer)
``
%6d`` (print as a decimal integer with a width of at least 6 wide)

``%f`` (print as a floating point)

``%4f`` (print as a floating point with a width of at least 4 wide)

``%.4f`` (print as a floating point with a precision of four characters after the decimal point)

``%3.2f`` (print as a floating point at least 3 wide and a precision of 2)

``` +, - , *, / ``` stand for the basic ASMD operations.

``^`` stands for a bit-wise XOR binary operation. Look at bitwise operations for details.

``&`` infront of the variable returns the address of the variable in an integer format.

``&`` is also used as a bitwise AND operator.

``++``, ``--`` are 1 unit increment and decrement operators. They operate only on integers.

``++i`` is a pre-increment (before i is accessed, it is incremented)

``i++`` is a post-increment (after i is accesses, it is incremented)

The decrement works the same way but decreases the value.

for a full list of operators, visit,

http://en.wikipedia.org/wiki/Operators_in_C_and_C%2B%2B

``()`` parenthesis is used for wrapping contents

``{}`` is used for wrapping definitions

``[]`` is used for wrapping indices.

exponent is given by the ``pow(a,b)`` (=a^b) function in ``math.h``

Modulus operation is given by ``%``

``5%2 = 1`` Modulus is applicable only for integers here.

**PEMDAS** operation scheme is followed.

In case of operators having equal precedence, left to right precedence is followed.

Meaning, to the left and right of the operator, the sub-expressions are noticed as to whether they are involved in any other sub-expressions.

If they are, then that expression is not done. If it is not, then it is done.

eg:
 
```C
10/5*2
```

The ``/`` operator is executed first, because 10(sub-expression on the left of ``/``) is not involved in any other operation. 

Whereas ``` * ``` is done second because 5(left of ``` * ``` ) is involved in ``/`` operation.

This is also called as operator associativity.

If the expression goes complicated or for the ease of avoiding operator associativity or operator precedence, use paranthesis.

Division operation applied on integers truncate the result. 

To avoid that, wrap the segment within ``float()``.

type conversion is always from lower to higher.  So, it is a one way.

ie. Lower type data can become a higher type data. Also, if a lower type data is assigned to a higher variable, then it becomes a higher type value.

The opposite (higher type data to a lower type variable) is not possible. When done so, the data get's truncated.

eg: ``integer`` (lower)  data can be promoted to a ``float``(higher) data but a ``float`` data can not be demoted to an ``integer``.
Implicit type conversion occurs when integers are assigned to floats etc., and the variables take care of the conversion.

Explicit type conversion occurs when intentional conversions are introduced, using float() or int() etc.,

``""`` is used for string input.

``''`` is used for character input.

eg:
 
```C
c = 'A';
option = 'Y';
name = "Arun";
```

Characters can also be added.

Characters carry an ASCII value. So, if characters are added, a new character is created that is equal to the sum of the characters' ASCII value.

strings are available and are given as a part of char.

When character variables are operated and assigned to another character variable, a new symbol or character is stored in the new character variable.

If the assignment is to an integer, the result of the ASCII value operation of the characters is stored.


Relational operators are
 
```C
==
>
<
>=
<=
!=
```

``=`` is a normal equal sign.

Logical operators are
 
```C
&& for AND
|| for OR
! for NOT
```

Escape Sequences are used for re-arranging/formatting the output properly. They are also used for placing key symbols inside strings. 

They have to be placed within string quotes.

``\`` symbol is for escaping a reserved symbol and using it in print statement or other places.

eg: ```C \' \\ \" \& ``` etc., 

The default escape sequences are
 
```C
\n (newline)
\t (tab)
\v (vertical tab)
\f (new page)
\b (backspace)
\r (carriage return)
\n (newline)
\a (alert, invokes a beep sound)
```

## Storage Classes

Storage classes are ways of storing variables in memory locations. C offers 4 storage classes namely,

1. Static
2. Extern
3. Auto
4. Register

To make a variable stored in the class, use their name during declariation.

eg:
 
```C
static int i; auto int j
```

auto:

auto is used for making the variable defined only within the function it is defined in. Outside the function, the variables do not exist. So, when they are accessed, it shows an error. By default, auto is the storage class for all the variables in any function in C.

register:

register is for storing variables in the "register" of a computer. These variables do not have an address in the memory. These variables tend to be fastest in execution or calls.

## Hash Sequences

Hash sequences explicitly define certain job to the compiler. Hence they are also termed as compiler directives.

To define a global constant, use
 
```C
#define VAR_NAME <value>
```
eg:
 
```C
#define PI 3.141596
```

These variables have a special data type. So, they adjust accordingly to the variable type of the expression involved. These variables have to be in caps. Also, variables cannot change in the program. Hence they are constants.

The constants are in capital letters. They need not be. It is a notation or a practice to do so, so that they are differentiated from variables.

## Variable Formatting With Example
 
```C
#include<stdio.h>
//http://www.codingunit.com/printf-format-specifiers-format-conversions-and-formatted-output
main()
{
	printf("The color: %s\n", "blue");
	printf("First number: %d\n", 12345);
	printf("Second number: %04d\n", 25);
	printf("Third number: %i\n", 1234);
	printf("Float number: %3.2f\n", 3.14159);
	printf("Hexadecimal: %x\n", 255);
	printf("Octal: %o\n", 255);
	printf("Unsigned value: %u\n", 150);
	printf("Just print the percentage sign %%\n", 10);
}

```

The output is
 
```
The color: blue
First number: 12345
Second number: 0025
Third number: 1234
Float number: 3.14
Hexadecimal: ff
Octal: 377
Unsigned value: 150
Just print the percentage sign %

```
 
```C

#include<stdio.h>
//http://www.codingunit.com/printf-format-specifiers-format-conversions-and-formatted-output
main()
{
	printf(":%s:\n", "Hello, world!");
	printf(":%15s:\n", "Hello, world!");
	printf(":%.10s:\n", "Hello, world!");
	printf(":%-10s:\n", "Hello, world!");
	printf(":%-15s:\n", "Hello, world!");
	printf(":%.15s:\n", "Hello, world!");
	printf(":%15.10s:\n", "Hello, world!");
	printf(":%-15.10s:\n", "Hello, world!");
}

```

The output is
 
```C
:Hello, world!:
:  Hello, world!:
:Hello, wor:
:Hello, world!:
:Hello, world!  :
:Hello, world!:
:     Hello, wor:
:Hello, wor     :
```

## Condition and Loop Statements

### if statement:
 
```C
if(condition 1)
{
    Set of commands;
}
else if(condition 2)
{
    Set of commands 2;
}
....
else
{
    Final set of commands;
}
```

The condition expression should evaluate to a logical value 1 or 0 (True or false.).

if the condition returns a value that is != 0, then the condition is termed as True. Else, it is termed as false.

Nested if-else statements (if-else statement inside another if-else statement) is possible.

### Switch case structure/construct
 
```C
switch(varname)
{
    case value1 || value a || value b:
          {
              statement set1;
              break;
          }
    case value2 || value c || value d:
          {
              statement set2;
              break;
          }
.....
    default:
          {
             statement set final;
              break; 
           }
}
```

If the variable value matches any of the case, then that corresponding case statement set is executed.
break is necessary to break out the switch case. otherwise, all the codes inside all the cases will be done and then the decision statement terminates.

### while loop
 
```C
while(condition)
{
    set of statements;
    one condition breaker statement;
}
```
In the absence of the condition breaker statement, the while loop will run forever.

### do while loop
 
```C
do
{
    set of statements;
    one condition breaker statement;
}
while(condition)
```

There is a small difference. while loop checks condition every time before it executes the set of statements. So, for executing and terminating the set of statements 'n' times, it checks the condition 'n+1' times. Whereas the do-while loop executes the statements before checking the condition. So for doing 'n+1' times the set of statements, it checks the condition 'n' times. So, while loop does not even allow executing the code once when the condition fails, whereas do loop allows executing the code atleast once before the condition fails.

### for loop
 
```C
for(i = initial_value; increment/decrement break or normal condition; increment/decrement)
{
    set of statements;
    condition breaking statement (if a normal condition)
} 
```
explanation:
for loop needs 4 components along with an iterating integer variable.
1. Iterating integer variable
2. Initial value for iterating variable
3. condition statement
    a. increment/decrement based condition
          This condition fails after a finite number of iterations when the iterating variable because it is incremented/decremented hits a limiting value. This limiting value is given as the condition
    b. normal condition
          This condition fails after a finite number of iterations when the codes inside the loop bring about a case where the condition fails.
4. Increment/decrement
    This can be given using ++ or -- operator or by other forced increments/decrements like i + = 3 etc.,
eg:
 
```C
for (i = 1; i<10; i++ or i += 1)
{ statements; }
```

working
1. initialization
2. condition
3. statements
4. increment
5. condition
6. statements
7. increment
8. condition
9. statements
10. increment and so on.....

 
```C
for(;;)
{
    set of statements;
}
```

This is an infinte loop!. Unless manually terminated or crashed by the system, the program will run perpetually. This is used with manual loop breaks. It is required for some programming applications where till a certain condition is reached, the iterations have to proceed.
