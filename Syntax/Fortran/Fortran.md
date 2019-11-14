# Fortran Programming

**_Updated till Fortran Programming Tutorial (Revised) : 017_**

## Introduction

Fortran stands for FORmula TRANslation.

It is been available from 1950's

Prior to Fortran, machine level or assembly level languages were used for coding.

This was a hectic job and in 1950's, John Backus of IBM gave the idea of "Speed Coding", wherein you have a simple programming language, where the methods are simple and easy to understand. The lines of code are very easy to interpret and follow. And at the back, you have subroutines to convert the statements into equivalent machine level language and execute it.

And thus came Fortran, the first ever proper compiled language ever.

Versions are as follows,

### Fortran 1


This is the first proper development in Fortran. It was quite difficult, but much better off than assembly level codes.

## Fortran 2 and 3


These were developed version of Fortran. A lot of companies and universities started to use them and because of which, multiple versions and different syntactics came into existence. 
     
### Fortran 66 or Fortran 4


This was the first proper standardized version of Fortran made in 1966, that made everything move much easier. The codes became more easy to follow and work with. This eradicated the existence of multiple versions and syntactics.
     
### Fortran 77

This is the most widely used and common standard made in 1977. It had a very large number of changes and improvements made into it. It is being used till date. This is the first in the series of the most easy to follow codes in Fortran ever. It was nearly a full fledged language. The program has a fixed format, wherein, each line cannot be more than 72 columns long and if they have to be, they have to be continues in multiple lines, executable statements mush start from a certain column number, labels from column 1 to 6 and so on.. This holds good for other statements as well. This was rather, an imitation of the IBM punch card designs used for programming at that time. A program will have 100s or 1000s of these cards, each card for each line of the program. Each card has instructions built into it by making holes/punches in specific places to denote the binary representation of each character, as per ASCII notations. Punches indicate 1 and the rest indicate zeros. Before that, tapes were used for programming and those were even more frustrating than punch cards.
   
The extension is .f77 or .f

### Fortran 90

This is a full fledge upgrade of F77, released in 1990 with more features and more freedom in-terms of syntax and operations. Have a lot of difference in syntax when compared to F77. It has free format, meaning, you do not have to stick to the ground rules of F77 for writing codes. Each line can be more that 72 characters long and will not be ignored as in F77 if the 72 count crosses.
   
The extension is .f90
     
### Fortran 95 Fortran 2003 Fortran 2008 Fortran 2015

The above three are marginal additions to F90 added in 1995, 2003, 2008 etc., They are not that prominent. F95 has minor changes. F03 and F08 have more features, but those have not been completely incorporated into the compilers yet. F15 is under construction and will be released by 2015/2016.
   
The extensions are .f95, .f03, .f08
     
Apparently, the older versions are the fastest and subsequent releases are slower and slower. This is a compromise for making more features and ease of programming for the users. The more higher level the instructions become, the harder it is for the compiler to optimize the memory for performing it faster.

Fortran was so heavily used in Industry and scientific community, that it created a software inertia. When new programming languages were created, instead of getting wiped out of existence, Fortran remained strong and firm and still being used. Surprisingly, fortran is still active and becoming more and more modern.

Fortran can be said as the pioneer example of modern programming languages. It gave inspiration for the birth of new programming languages.

---

## Data Sources

### Books:

* Any Fortran book of convenience
* tutorialspoint.com notes on Fortran

### Video Lectures:

* Youtube Lectures by Reimber
* Youtube Lectures by hexafoil
* Coursera - HPC course by Prof. Randall J LeVeque, University of Washington
* Youtube Lectures by Self
* Fortran.com, The fortran company.
* fortrantutorial.com notes

A lot of information has been covered in the Fortran (Basic and Advanced) Tutorials that are not in the notes. Have a look.

---

## Requirements

The software requirements are

* Compilers
* Editors

Compilers or the basic code for fortran, are available in several formats:

* GNU gfortran is ideal and most suited. This is highly recommended for general purpose usage. It compiles F77, F90 and F95.

* Intel ifortran is also available, but may be commercial. Not recommended for normal use, primarily because of cost issues, but can be used for Super Computing facilities.

* Several other compilers exist, with each one having their own advantages and facilities.


**For Linux/Unix** : They come pre-built with a GNU compiler (possibly) and regular periodic checks/updates will do. If not available, a command prompt execution for installation will take care of it.


**For Windows**: This is a bit complex. By default, windows do not have the compilers built into it. To incorporate them, there are, in contrast to the complexity, many ways:


* **Cygwin**: This is a collection of software with a bash terminal. To get the compiler, invoke a cygwin installer and install gnu gcc compilers. Cygwin provides a vast variety of software, so it is sufficient to install the essential ones.

* **Mingw**: This is similar to cygwin. It is a big bundle having GNU compilers for fortran, c and c++. Possibly with OpenMP modules.

* **Equation solutions** company in their website, Equation.com provides a small bundle of essential GNU compilers.

* **Silver force FTN95** is another option. Comes along with **Plato IDE**

 
There are multiple sources.

 
Editors:


* **Geany** : Light weight, needs a compiler to be installed separately,

* **Netbeans** : Multi-purpose editor, needs C/C++ plugin installed and a compiler installed, either cygwin or mingw. Sometimes, the fortran plugin may not be available, so you have to install one, which is quite easy.

* **Eclipse**: Multi-purpose editor, thinking that it will be similar to netbeans. There are many versions of eclipse. The "parallel application developers" version is preferred. It has features to run C/C++, fortran and can implement OpenMP/MPI features. If other versions are used, then a Fortran plugin has to be installed.


**Note**: If Eclipse or Net beans is used in Windows, then you have to ensure the path of java is registered. Install a **JDK** package, copy the address of the bin folder, right click the computer icon, go to properties, go to advanced system settings>environment variables, add a new user variable, set the variable to be "path" and the address to be the address you copied from the jdk folder. Save and quit. Open cmd and type javac and enter. If you get a big bunch of usage instructions, then it is working. If it shows an error/not found message, the it has to be done properly. Check the link for step-by-step explanation. Also, follow the video for a full explanation.
https://www.youtube.com/watch?v=GfCmiEbGtpE&list=UUOF2qXeo1xhmxqt_25yEB9Q

 
For Netbeans in ubuntu or any other linux versions, go to
https://www.youtube.com/watch?v=OK6GSvpGZfk&list=UUOF2qXeo1xhmxqt_25yEB9Q&index=8

The above are free, cross platform and semi-dedicated editors. They can be used to edit and execute the programs easily.

If a normal editor is used such as gedit in ubuntu or notepad in windows, you need to execute them from command line prompt.


**Dedicated Editors**: can be used to edit programs, compile and execute them. They come with the compilers in-built with them. So, they take care of the compiler issue.

**Code blocks**: Has a lot of features, has both project and normal execution based modes. Recommended for starters and even advanced users. But not suitable for creating flag-based compilation.

**Plato** : Specifically for Fortran

There are many more dedicated editors.

## Installation

### Mac and Linux - gfortran installation


* Go to the terminal and type the line below for Debian/Ubuntu. (Instead of ``apt-get`` use the proper keyword based on the distro)

```bash
    sudo apt-get install gfortran
```    
    
* Make sure that the internet is connected
* Proceed as per instructions - easy and straight forward

### Windows, Mac and Linux - Code Blocks/geany installation

To install code blocks(geany), go to the website, download the latest version of code blocks+mingw consolidated setup (geany setup) and proceed. It is very straight forward and simple.

### Windows - gfortran installation via cygwin

Follow the instructions given in https://www.youtube.com/watch?v=GfCmiEbGtpE&list=UUOF2qXeo1xhmxqt_25yEB9Q . This should work fine!

## Caution!

* Do not mix and match compilers! (Intel C + gnu fortran) Operations may not work!
* Different compilers can give different answers for advanced problems - due to optimizations, flag usage, change of data types etc., So check the code and flags!
* GNU Fortran is free, simple, opensource, almost all features, mostly sufficient for a large quantity of jobs.
* Only has standard features. Good for beginners and learners. Makes learning advanced versions much easy!
* Commercial compilers like Intel, PGI, Cray, NAG, HP are much advanced and have non-standard features. They are hardware manufacturers (a lot of them) and so, they take the advantages of the system architecture to make more efficient programs and flags.
* Use Commercial compilers for heavy duty applications. They are both free and priced!
* Commercial compilers have much advanced OpenMP and MPI implementations
* Programs written keeping one compiler in mind, may cause warning or do not work in other compilers - due to flags and optimizations - Be cautious!

## Hello World Program!


```Fortran
! This program is a hello world program
! This is a comment. Start a comment with an ! mark
! Intendation is optional, use it for enhanced readability!

program hello
! This is the program starting. program is a key word, followed by the program name

    implicit none
    ! It has a meaning
    
    print *, "Hello World! My Name is Arun!"
    ! This is the print statement. * means unformatted!

! The line below is the program ending. end is sufficient, but for clarity, write end program prog_name
end program hello
```

## Basic Concepts


### Implicit none and Datatypes


```Fortran
    implicit none
    ! Without it,
    ! Variables beginning with l, m, n .... are termed as integers by the compiler by default
    ! Variables beginning with a, b, c, x, y, z, ..... are real/float!
    ! If not used, then there can be data type troubles and limitation in variable names!
    ! implicit none tells the compiler "Not to assume the data type of any variable implicitly! Let the user define the data type explicitly"
```

```Fortran
    integer :: i1, i2
    ! Integers are positive and negative whole numbers
    integer i3, i4
    ! This notation without :: is also fine! :: is used for separation - that is it!
    real :: r1, r2
    ! Reals are positive and negative float numbers (numbers having decimal places)
    double :: d1, d2
    ! Reals having 8 bytes of memory! 15 digits precision
    complex :: c1, c2
    ! Complex numbers. By default, both the real and imaginary parts are floats
    character :: ch1, ch2
    ! Used for storing symbols
    logical :: l1, l2
    ! Used for storing Boolean/Logical Values "True" or "False"
```

### Implicit None


This statement is given before variable declarations. The purpose is to tell the program that all the variables that will be used in the program will be user defined. It also says that no variable will be defined just like that.

If this statement is avoided, you can arbitrarily define variables anywhere in the code/script and the compiler will not cause a warning. Also, the data type of the variable is decided by the compiler based on some in-built rules. Also, these rules mention what type the memory location should be, should it be a constant or a variable?

If the statement is included, you have to define all the variables explicitly with a data type. You also have to mention whether they are constants or variables.

Why this Statement?

In the days of F77 and may be before, there was a general rule of thumb to differentiate variables and constants that is loosely associated with algebraic terms.
It was a convention that all the variables starting with i,j,k,l,m,n are integers, and all other variables are 4-byte real values. Ironically, even today, some of these conventions are still being followed. If you want some other formats, you have to explicitly declare them.

With increase in complicated algorithms, this rule became pointless, because certain variables starting with i to n have to be floating point numbers, and other variables may have to be integers. So, because of this rule, a lot of complications arose in the future.

Instead of removing this convention, they added this command that overrides the convention. Thereby, the convention can be followed if required, avoided if needed.

### Operations and Operator Precedence


Code for hero's formulae : Area of a triangle

```Fortran
real :: a, b, c, s, p, Area

! + - * / Standard ASMD (Add, Subtract, Multiply, Divide)
! ** exponent or power eg: 2^3 = 8 is written as 2**3
! ^ not available!
! mod(5,3) = 2. Returns the reminder of 5/3. Works for both
! integers and real numbers

! Operator precedence: 
! Operators have an order in which the operation occurs
! Avoids multiple representation of an expression
! Tells which operation to occur first, which next ...
! PEMDAS = Parenthesis Exponent Multiplication Division Addition Subtraction
! Please Excuse My Dear Aunt Sally (Acronym to remember the above)

a = 3
b = 4
c = 5

! 3x10^8 scientific notation is given by 3E8. decimals allowed.
! e stands for a single precision number
! 3d1, 6d-2 is also allowed. 
! These are another type of scientific notation.
! d stands for double precision number

p = a+b+c
s = p/2 ! 0.5*p

Area = (s*(s-a)*(s-b)*(s-c))**0.5
! Parenthesis takes first preference! making s, s-a, s-b, s-c occurring separately.
! Then, these results are multiplied and finally, the result is powered!

print *, "The perimeter of the Triangle is:", Area
print *, "The area of the triangle is:", p
```

The output is:
```
The perimeter of the Triangle is: 12.00000
The area of the triangle is : 6.00000
```

### Type Casting and Truncation


```fortran
integer :: d, e
real :: f, g
! Proper integers and proper real numbers

d = 4
f = 6.7
! Valid assignments based on data type

g = d
e = f
! Not a proper assignment

print *, "d = ",d , "e = ", e
print *, "f = ",f , "g = ", g
```

The output is:

```
d = 4 e = 6
f = 6.6999 g = 4.0000
```
Note that 'e' value is truncated and you have extra zeros in 'g'

Why the variation in output?

* d is an integer. When d's value is assigned to g, integer data type is type casted to real. Integers can be represented by reals by adding trailing zeros. Hence, extra zeros come in. Also, real > integer.
* f is a real. When f's value is assigned to e, float data type is type casted to integer. You cannot represent real numbers using integers because integers do not have decimal parts. Hence, the decimal part is truncated!

### Case Insensitivity


Variables, keywords etc., in fortran are case insensitive! for example

Code for hero's formulae : Area of a triangle

```Fortran
! Note that throughout this code, capitalization is used
! in a crazy manner!

Real :: a, b, c, s, p, Area

A = 3
b = 4
c = 5

P = a+b+c
s = p/2 ! 0.5*p

AREA = (s*(s-a)*(s-b)*(s-c))**0.5

Print *, "The perimeter of the Triangle is:", AreA
prInt *, "The area of the triangle is:", p
```

The output is:
```
The perimeter of the Triangle is: 12.00000
The area of the triangle is : 6.00000
```

The result is the same and not a problem!

Note that this can be an advantage/disadvantage based on the case! Use caution!

### Explicit type casting and Read Statement

```fortran
g = real(f) ! Explicit type casting for real numbers
e = int(f)  ! Explicit type casting for integer numbers
```

To get the data from the user, use ``` read ``` command!
```fortran
print *, "Enter the sides of the triangle!"
read *, a, b, c
! * means unformatted input
! While execution, after printing the message, the compiler waits.
! Give data one by one and press enter.
! Data has to be entered based on the data order mentioned in the read statement.
! Sometimes, ',' and space between the data are also used for entering the data. Use carefully!
! Use asterix properly for entering a common data to multiple consecutive variables!
! eg: 3*5 = 5 is repeated thrice!
```

### Parameter keyword and Built-in Functions

Use parameter keyword for making constants.

```fortran
real, parameter :: pi = 4*atan(1.0)
! This way, pi becomes a constant. 
! To get the value of pi, we are using the built in inverse tan function (arctan).
real, parameter :: v = 1.0
! v is also a constant
real, parameter :: p 
! This line will throw an error. While defining constants, one should enter the value as well
```

Since $tan(\frac{\pi}{4}) = 1.0$ , the function usage gives pi value properly!

Now, if we equate or modify the value of pi somewhere in the program, then it will throw an error!

Like the above tan functions, you have a lot of default functions available in fortran, called as **intrinsic functions!**. You have an entire list! You can check it out in books, internet etc..,

eg:
```fortran
l = sqrt(x**2 + y**2) ! square root function
a = sin(y/x)          ! sine function!
```

## Relational and Logical Operators

``` fortran
    ! A simple demonstration of Logical and Relational Operators
    ! Comment/Uncomment the lines to check the relational and logical expression!
    ! Also, change the values of m and n to verify the table below 

program rel_logic

    implicit none
    !integer :: a, b
    logical :: m,n
    
    !a = 5
    !b = 4
    m = .true.
    n = .true.
    
!    print *, "A = ",a,", B = ",b
!    print *, "A == B? :", a==b
!    print *, "A > B? :", a>b
!    print *, "A < B? :", a<b
!    print *, "A >= B? :", a>=b
!    print *, "A <= B? :", a<=b
!    print *, "A /= B? :", a/=b
    
    print *, "M = ",m," N = ",n
    !print *, ".not.M = ", .not.m
    !print *, "M or N? :", m.or.N
    !print *, "M and N? :", m.and.n
    print *, "M eqv N? :", m.eqv.n
    print *, "M neqv N? :", m.neqv.n
    
    ! == .eq. equal to
    ! > .gt. greater than
    ! < .lt. less than
    ! >= .ge. greater than or equal to
    ! <= .le. less than or equal to
    ! /= .ne. not equal to

    ! .true. or .false.
    ! .not.(exp1)
    ! (exp1).and.(exp2)
    ! (exp1).or.(exp2)
    ! (exp1).eqv.(exp2)
    ! (exp1).neqv.(exp2)
    
    ! U PEMDAS REL_OP LOG_OP
    ! This is a full fledged operator precedence
    ! Unary PEMDAS Relative operators Logical Operators
    ! Unary +5, -7 ! N/A: ++ --
    
    ! a    .not.a   0 = .false.
    ! 1     0       1 = .true.
    ! 0     1
    
    !____________________________________________________________
    !    |      |          |           |            |            |
    ! a  |   b  | a.and.b  |  a.or.b   |   a.eqv.b  |   a.neqv.b |
    !____|______|__________|___________|____________|____________|
    !    |      |          |           |            |            |
    ! 0  |   0  |     0    |     0     |      1     |     0      |
    ! 0  |   1  |     0    |     1     |      0     |     1      |
    ! 1  |   0  |     0    |     1     |      0     |     1      |
    ! 1  |   1  |     1    |     1     |      1     |     0      |
    !____|______|__________|___________|____________|____________|

end program rel_logic
```

## Characters and Strings

This program explains the concept nicely!

```fortran

! Program for defining and printing strings

program strings

    implicit none

    !character :: a ! a can store just one character = symbol or a 1 digit 
                   ! number or a single alphabet
    !character (len=5) :: b ! b is a 5 character long string

    !character(5) :: b
    !character*5 :: b
    !character :: b*5

    !character :: c*6, d*10, e*3
    
    !array of strings declarations
    
    !character (len=6), dimension(2) :: str1 ! str1 will have two 
    !strings each of 6 characters in length
    
    !character (6), dimension(2) :: str1
    !character*6, dimension(2) :: str1  
    !character, dimension(2) :: str1*6!, str2*7, str3*10 

!    a = 'X'
!    !a = "X" ! Alternate expression
!    b = 'white'
!    c = "456321"
!    d = "asd567jk^%"
!    e = "_ _"

!    print *, "a = ",a
!    print *, "b = ",b
!    print *, "c = ",c
!    print *, "d = ",d
!    print *, "e = ",e

    print *, "My name is Arun, written in double quotes"
    print *, 'My name is Arun, written in single quotes'
    print *, "He is my friend's teacher"
    print *, 'He is my friend"s teacher'
    print *, 'My friend said, "I am fine!", and I moved on!'
    print *, "My friend said, 'I am fine!', and I moved on!"
    print *, "My friend said, ""I am fine!"", and I moved on!"
    print *, 'My friend said, ''I am fine!'', and I moved on!'

!    str1(1) = "Carrom"
!    str1(2) = 'Cod ng'
    
!    ! read *, str1(1), str1(2)
    
!    print *, "First string: ", str1(1), " Second string: ", str1(2) 
    

end program strings

```

## Modulus Operation

Modulus operation returns the remainder of a division. This function works for both integers and real numbers.

```fortran
d = 51
e = 10
q = d/e      ! Quotient is 5
m = mod(d,e) ! Reminder is 1

a = 51.04
b = 10.0
qr = a/b      ! Quotient is 5.104
mr = mod(a,b) ! Reminder is 1.04
```

## Exectution from Terminal

To execute the file in Unix/Linux prompt with bash,

* Compile and link the file first to get the objects

```bash
gfortran filename.ext
```

For example:

```bash
gfortran triangle.f95
```

This will create object files, link them and creates a default executable file a.out

* Run the file by

```bash
./a.out
```

the executable file's name is a historic practice. The executable is machine specific. You cannot use the a.out in some other machines. It is resolved by compiling and then executing the file.

To have a different executable file name, use -o flag while compiling and linking.

```bash
gfortran filename.ext -o exec_filename.ext (this extension can be .exe also)
```

To compile alone, use -c flag

```bash
gfortran -c filename.ext
```

To link it, use -o flag with the .o files

```bash
gfortran filename.o -o exec_filename.ext 
```

To save the output of the executed file, use,

```bash
./exec_filename.ext > result_filename.ext
```

eg:
```bash
./main.exe > output.txt
```

## Conditional Statements and Loops


### If statement

Code segment to find the quadrant of a point (x,y) using the magnitudes of x and y

```fortran
if ( x >= 0 .and. y >= 0) then ! First condition
   q = 1 ! Statements to be executed if condition is true
else if (x<=0 .and. y>=0) then ! Condition to check if all above conditions are false
   q = 2 ! Statements to be executed if condition is true
else if (x<=0 .and. y<=0) then ! Condition to check if all above conditions are false
   q = 3 ! Statements to be executed if condition is true
else
   q = 4 ! Statements to be executed if all the above conditions are false
end if   !this line is necessary

! else if and else statements are optional
```

### do statement

syntax:

```fortran
do serial=1,k,increment 
!serial is an integer variable that varies from 1 to k. if increment is absent, the default value is 1.
   ! Set of statements 1
    if (condition-x) cycle  
    !the presence of keyword cycle transfers control back to do statement if condition-x is satisfied.
       ! Set of statements 2
    !the presence of keyword cycle avoids statement-2 if condition-x is satisfied.
end do
```

The iterating variable increases till end+increment and then checks the condition. Since the condition will break, the loop for end+increment will not happen.

code to generate geometric sequences

```fortran
a = 1.0 ! First term
r = 2.0 ! Common ratio

do i=0, n !i = 0, 1, 2, 3, ...., n
   print *, "The value ", i, " of the series is: ", a*(r**i)
end do

```

``exit`` command is used to quit the loop and come out. Exit command is used explicitly inside do loop with if statement.

Code for n successive factorials using labels:

```fortran
outer_do_loop: do i=1,n
        
    !print *, "Inside the loop, i = ",i
    fact = 1
    ! j can be modified and used here!
    ! i can be only used here!
    inner_do_loop: do j=1,i
        
        ! i and j cannot be modified here!
        ! i and j can be used here!
        fact = fact*j

    end do inner_do_loop
    ! j can be modified and used here!
    ! i can be only used here!
    print *, "The factorial of ", i, " is:", fact

end do outer_do_loop
```


### Cautions in do loop

* do loops must be sandwitched! Loops cannot overlap!
* loops can be within the other or nested!
* use labels for clarity - if you need
* if a label is used to name a do loop, then the end do statement must also have the label name
* The iterating variable cannot be modified inside the loop.

### Do while

This do loop is actually a while loop.

syntax:

```fortran
do while (condition)
    !set of statements
    !one condition breaking statement
end do
```

## Labels


This looping is also possible using labels.

eg:

```fortran
do label_name: serial=1,k
     statements
label_name continue

```

Here, the do statement starts first and executes the statement set once, and goes to the continue
statement. Now, the do loop does not knows what to do. So it continues, because of the instruction
given by the continue statement. Now, since it already finished the iteration with the first value of
the iteration variable, it goes to the next value of the iteration variable and proceeds further.

The colon (:) is necessary!

The label_name is the place, where the continue has to be placed. That label is being referred in
the do statement. This makes sure that the do statement gets the information/call from the continue
statement instead of some other statement. If some other label is used, then the do loop might not work.

You do not need a continue statement. The label can be placed pointing some other statement also.
So, the do statement, does the statements, goes to the statement where the label is pointed at,
then goes to the statements inside it, goes to the label attached statement and repeats till the indices
are over.

This label has no specific format. It is an F77 convention.
 
you can label loops.
 
```fortran
outer_do: do
         statement1
inner_do: do
         statement2
end do inner_do
         statement3
end do outer_do
```

## Select case
 
```fortran
select case(variable)                  
         case (value1)                            
statements1                      
         case (value2)
                 statements2
         case (value3)
                 statements3
         .
         .
         .
         case default
                 statement final
end select
```
eg: assume statements for each case. note that multiple values can be fed into the case analysis as shown. case values can be .TRUE. or .FALSE. as well. default case is not mandatory.

```fortran
select case(variable)
         case(1)
         case(2,3,7,8,10)
         case(4:6)
         case(11:)
         case default
```

## forall loop

Fortran also has a for loop implemented as a forall. This loop can be used like any other for loop except for one condition. Each iterative loop should be independent of each other. Therefore, the loop can be done in any order instead of a serial order. **So, in this strict sense, it is not a for traditional for loop**. So, if one wants a **strict** for loop implementation, use a **do** loop.

The format is:

```fortran
forall (i=1:n)
 statements
end forall
```

When executed, the compiler gets freedom to do the job in any order of i, thereby can make some optimizations to the programs. This is useful even in serial processing.

Nested forall is also possible, provided all the loop index can be acted together. Also, it can have masks. 
eg:

```fortran
forall (i=1:n, j=1:m, b(i,j).n.e.0 ) 
    !the mask here is that ignore or do not calculate an expression if b(i,j) is zero
    a(i,j) = 2*i*j
    c(i,j) = 1/b(i,j)
end forall
```

## Kind attribute

Kind command is used for setting the storage memory of the data type. It is useful for variables and functions. This is also used to make the variables to store a large range of numbers.

```fortran
    integer(kind=8) :: a
    integer*8 :: a ! Alternate statement
    ! variable a is an integer variable that takes 8 bytes of memory
    real(kind=4) :: r
    real*8 :: r ! Alternate statement
    ! variable r is a real variable that takes 4 bytes of memory
```

Integers have kind = 2, 4(default), 8, 16

## Limit of Integers and Real numbers

The integers and real numbers are stored in a particular manner in the memory. Each value takes some memory. The more memory a value takes, the higher the magnitude of the value can be stored.

For details : https://en.wikipedia.org/wiki/Integer_(computer_science)

So, if a proper kind statement is not used, then the values will overflow, corrupting the values finally. Precaution has to be taken to ensure that such issue does not take place. Use the kind statement properly to avoid this issue.

## Arrays

declaration example:
```fortran
real :: array_name(size)
```
 
sometimes it can be defined using dimension function namely

```fortran
real, dimension(size1,size2,size3,...) :: array_name
```
**Here, the index is not mentioned. By default its from 1 to the given size.**
 
The index is superb in fortran. It can be negative or positive. some definitions are
```fortran
a(-1:3) !5 values of a from a(-1), a(0), a(1), a(2), a(3)
a(-6:-4) !3 values similarly.
dimension(0:20) :: a 
!has 21 values from a(0) to a(20)        
dimension(0:20,0:20) :: a 
!has 441 values from a(0,0) to a(20,20)
```
Based on these definitions, you can modify the indexing as per your requirement.
 
for array to be filled one-by-one, the order, taking a 5x5 array, is,

```
(1,1), (2,1), (3,1), ... (5,1),

(1,2), (2,2), (3,2), ... (5,2), and so on!
```

**Yes the order flips! unlike other programming languages!**

This is the manner in which the values get stored in the memory as well!

**This is called as Column Contiguous Memory Storage**. In normal convention, the successive elements in the memory happen to be row-wise. In Fortran, they are column-wise!

* This is something to be considered. 
* Also, when trying to optimize the code, it is necessary to know/have an idea of how the values are stored in the memory of the computer. 
* Because, the retrieval of these data from memory takes several orders more time than moving these values into the cache and register memory and doing the operations in ALU combined.

This is a big problem when you are trying to pass arrays between different programming languages like Python or C, where the memory allocation is row based.

array initialisations using constructors. ``/values/`` is a constructor for the array.
```fortran
b=(/1,2,3,4,5/)
d=(/(i, i=1,50, increment)/) !d = 1,2,3,....50 if increment =1 !USE OF INCREMENT IS DOUBTFUL
c=(/5,8,(2*i, i=1,20,increment),9/) !d = 5,8,2,4,6,......40, 9 if increment =1 !USE OF INCREMENT IS DOUBTFUL
```

multiple statements like the above two within the constructor are allowed.
```fortran
real, dimension(20) :: a=0 
!assigns all 20 values of a to 0.
```
```fortran
a(5,6,7) 
```
has 

```fortran
rank=3 
extent1=5, 
extent2=6, 
extent3=7 
size =5*6*7=210 
shape =(5,6,7)
```
```fortran
rank(), shape(), size() 
```
The above functions return the rank, shape and size of the arrays.

Arrays can be dynamic in Fortran.

## Array Operations

Array operations can be done without the need for loops.

eg:

For three arrays of size n, with indices from 1 to n,

```fortran
do i=1,n
     c(i) = a(i) + b(i)
end do
```

This can be done by the line
```fortran
c = a + b !(available from F90 onwards)
```

If x and y are arrays, then 

```fortran
y = x**2 
```
is an example of a component-wise operation.
This operation holds good for - / * also.

even ``` sqrt() ```works component-wise.

```fortran
dot_product(x,y) !calculates the dot product of x,y namely = sum of all xi*yi from i=1,n
array2 = reshape(array1, shape) !reshapes a given 1D array into a 2D array of the given shape.
```
eg:

```fortran
A = reshape((/1,2,3,4,5,6/), (/3,2/))
```

This will produce a three row, two column matrix. **All the entries get filled COLUMNWISE instead of ROWWISE!**

Array slices can be made.

eg: 
```fortran
print *, a(i,:)  !this will print out the ith row.
```

```fortran
transpose(array) !transposes the matrix/array
C = matmul(a,b) !does the matrix multiplication of a,b. Applicable to vectors also.
```

## Array Memory Allocations

Fortran needs to know the size of the arrays beforehand for allocating memory. But usually, the size of the array is not known until it is run/executed.

F77 has two ways to resolve this:

1. Allocate a very large array for any application
2. Use "Work arrays" and partition it into pieces.

The second approach is used in LAPACK as well. Work arrays are very large arrays allocated initially. Later, when the size of the variable arrays are known, the work array is broken (to be precise, partitioned) to have a small piece of memory out of it to fit the variable array. The starting address as well as the data of the array are sent into it and they get stored.

Similar process happens for other arrays. They get allocated in some other portion of this big Work array. This is a crude method.

Dynamic allocation is the solution to it. This started from F90 and extends in all future versions. This avoids the need for F77 protocols for storing array data.

The arrays get dynamically allocated.

dynamic arrays are to be declared as below

```fortran
allocatable, dimension(:) :: a 
!This tells the compiler that array a's memory is dynamic
! get a value n and allocate a as,
allocate (a(n)) 
!a value ranges from a(1) to a(n)

allocatable, dimension(:,:) :: b
! get values for m and n and allocate b as,

allocate(b(m,n))
```
This can be extended to multi-dimensional arrays also.

To deallocate them, use the deallocate command.

```fortran
deallocate(a), deallocate(b)
```

To ensure that you do not run out of space, use the optional stat argument.
eg:

```fortran
allocate(a(n), stat=alloc_error)
```
```
if alloc_error /= 0, 
```
then you have an insufficient memory. Otherwise, it is fine.

**Caution:
Be careful while passing arrays and scalars into subroutines. If a scalar is passed, and it is treated as an array inside the subroutine, it will change the values of the other variables! Vice-Versa also happens. In older versions, not even a warning will appear and the program will be executed. In newer versions, the program will be executed with warnings. Because, when you pass an element into a subroutine, the variable address is passes into it. Sometimes you get a SEGMENTATION FAULT, meaning, the program is trying to write values in certain parts of the memory that it has no access or permission to. To check these, use -fbounds-check flags while compiling the code. (these are gfortran flags)**

## Fortran Flags and gdb

These are optional checks or conditions to look for when you are compiling the code or executing it.

check: http://gcc.gnu.org/onlinedocs//gcc-3.4.5/gcc/Optimize-Options.html for a detailed list of gcc compiler flags and explanations.
  
* -c is for compile only

* -o is for linking object files to make an executable

* -fbounds-check is for checking the bound limits of arrays and for checking the size limits of variables

* -g is the debugger flag to indicate (if possible) where things went wrong.

* -o2 is for compiling the codes with level 2 optimization.

* -o3 is for compiling the codes with level 3 optimization.

* -fgcse (global common sub-expression elimination) is for translating the code into an optimized machine code by collecting the common expressions that are occurring repeatedly in the code, makes it a variable, and then uses it. Saves execution time by reducing the number of operations to be done. This is kind of taken care in -o2 or -o3 optimizations.

* -finline-functions is for compiling the code, by replacing the function calls with a direct in-line representation of the function. Wherever the function call happens, instead of going to the function, the statements of the function are brought to the code having the function call directly. This avoids the need for creating dummy variables, switching between programs etc., This makes a big difference when an array is processed by the functions, or the function is being called within a loop.

If there is a problem in the file while using the -g flag there will be indications.
Then type,

    gdb executable_filename.ext
    
to have a full pass at the file and you will get a gdb prompt. Type run to get an indication as to where the problem is.

gdb is similar to Python Debugger (pdb)
use help in gdb prompt to get all the available commands.

## Goto statement

Go to statement is used for force shifting the line of execution to some other part of the program.

syntax:
```fortran
  go to <LABEL>
```

eg:
```fortran
if (some condition) go to 99
! lot of lines of code in between!
99 continue
    set of statements
! continue statement is used to continue the execution. That is all.
```

## Functions -- Simple

Functions in fortran are similar to other functional definitions in other languages.

Functions can take one or more arguments and return a value.

eg:

```
y = f(x) or z = f(x,y)
```

Usage in fortran:

```fortran
real (kind=8), external :: f
```

"External" is used to tell that the definition is available elsewhere.

Within the program script, but outside program, end program lines, the definition of the function should be mentioned.

See the example below for clarification.

Sample Program:

```fortran
! Program to experiment with functions
! The function is the implementation of hero's formulae
! For calculating the area of a triangle

program functions_example

    implicit none
    real (kind=8) :: a,b,c,s,Area
    real (kind=8), external :: tri_area_ssa, semi

    ! External indicates that the definitions for them are given
    ! Outside the program.

    a = 5
    b = 12
    c = (a**2 + b**2)**0.5

    s = semi(a,b,c) 
    ! Invoking one function

    Area = tri_area_ssa(a,b,c,s)
    ! Invoking another function

    print *, "The semi-perimeter of the triangle is :",s
    print *, "Area of the triangle using Hero's Formula is :",Area

end program functions_example

real (kind=8) function semi(a,b,c)
! Note that the data type definition is needed for the return value

    implicit none
    real (kind=8), intent(in) :: a,b,c
    ! intent() is a built-in-function that indicates whether the variables
    ! are passed into or passed out of the function or both.
    ! Here, these variables are being passed into the function and
    ! hence the argument "in".

    semi = 0.5*(a+b+c)

end function semi

real (kind=8) function tri_area_ssa(a,b,c,s)

    implicit none
    real (kind=8), intent(in) :: a,b,c,s
    real (kind=8) :: x,y,z

    x = s-a
    y = s-b
    z = s-c

    tri_area_ssa = (s*x*y*z)**0.5

end function tri_area_ssa

```

## Intent functions

Intent is a built-in-function used inside other functions and subroutines to indicate the nature of the variables involved.

```fortran
 intent(in) : !This means that the variable is passed into the function/subroutine/module and it's values should not be changed inside it.
 intent(out) : !This means that the variable is passed into the function/subroutine/module may not have a value, and thereby can be assigned a value and passed out of it.
 intent(inout) : !This means that the variable is passed into the function/subroutine/module and it can be altered and can be passed out of the function.
```

These are not necessary sometimes, but it is a good practice to follow their usage.

## Subroutine

A subroutine is similar to a function. It is not invoked, but rather called in.

Subroutine is an extended and advanced version of a function. It can have multiple arguments passed into it. It can also pass out multiple arguments.

Also, it can pass out the variables passed into it by making changes to them.

This is very essential for complicated programming algorithms.

How to call it?

```fortran
call subroutine_name(args)
```

Subroutines can modify and pass arrays. Functions cannot! They follow the same procedure as that of other variables, the "dimension" type has to be mentioned to in inside the subroutine as well as outside the subroutine. Also, you may have to pass the size of the arrays is needed.


Subroutines can be defined within the script or outside in a new script.

This is an example:

Sample Program:

```fortran
! Program to experiment with subroutine
! The subroutine is the implementation of hero's formulae
! For calculating the area of a triangle

program subroutines_example

    implicit none
    real (kind=8) :: a,b,c,s,Area

    a = 5
    b = 12
    c = (a**2 + b**2)**0.5
    s = 0
    ! s is intentionally set to 0 so that it gets modified inside
    ! the sub-routine call. Area is not set any value. This is
    ! to see that the subroutine assigns a value to it.

    print *, "A=",a,"B=",b,"C=",c
    print *, "S=",s

    call tri_area_ssa(a,b,c,s,Area)
    ! This is the subroutine call !

    print *, "A=",a,"B=",b,"C=",c
    print *, "The semi-perimeter of the triangle is :",s
    print *, "Area of the triangle using Hero's Formula is :",Area

end program subroutines_example

subroutine tri_area_ssa(a,b,c,s,Area)

    implicit none
    real (kind=8), intent(in) :: a,b,c
    real (kind=8), intent(out) :: Area
    ! This is for making an assignment to Area, as Area has no value
    real (kind=8), intent(inout) :: s
    ! This is for altering s, as s has a value to it.
    real (kind=8) :: x,y,z

    s = 0.5*(a+b+c)

    x = s-a
    y = s-b
    z = s-c

    Area = (s*x*y*z)**0.5

end subroutine tri_area_ssa
```

## Modules

Modules are big chunks of programs written separately. It can have it's own variables, functions and subroutines.
Modules are like header files in C or like import file modules in Python.
 

Format of a module goes like this:

```fortran
module <module name>
     !variables and statements
contains
     !definitions for subroutines/functions
end module <module name>
```

To use the module in a program/subroutine/function:

```fortran
program program_name
     use <module-name> !This has to come before using other variables/statements
     !variable declarations and statements for program
end program_name
```

To import only a function/part of a module, use only command

```fortran
     use <module-name>, only: <var or function or subroutine>
```

Modules can be used to define global variables that can be used in several programs. But this is not recommended.
Modules generate interface information when their variables and functions/subroutines are used. These are links to determine which variables came from which file. This helps to see whether proper arguments have been passed or not.
Modules also help to create derived data type.

NOTE: Modules must be compiled before compiling the programs using the module! On compiling a module, it produces a .mod file and a .o file. Then, the file using the module has to be used. When compiling the program and module file together, put the module file first and then the program file.

eg: 

```
gfortran module_file.f90 prog.f90
```

You cannot put variables inside module. Only parameters are allowed. Variables are allowed inside the functions and subroutines of a module. To make a variable, use the "save" keyword after the variable declarations. This command makes sure that any value that gets assigned to the variable is available in all the programs using the module. Like a global variable. While calling the module, use "call another_subroutine()" subroutine to set it's value. This subroutine should have the variables defined and set with a value.
eg:

```fortran
implicit none
real :: pi
save
```



## Pure Keyword

This keyword is used for making subroutines, modules and functions free from global variables and alterations. To declare them, use

pure function/module/subroutine name and that is all.

pure keyword can be used if the function/module/subroutine is incapable of or does not
1. altering global variables
2. altering input variables in case of functions.
3. making local variables global with save command
4. having I/O

pure keyword makes them thread safe during parallelizing processes. So, this can be used for both parallel and serial runs.
This is beneficial even for serial runs, as it helps the compiler to make some more optimizations during compilation and execution.

## Getting Excess Precision

The registers and ALU of a PC are designed for more precision than the memory storage. So, you can force the results to be more consistent and precise by compiling and executing the files with the flags,
-ffloat - store

This causes the variables to be written out of the registers, back into the cache, before the same value can be used again.

Usually, when a value is taken by the cache, it gets modified in the CPU and then goes to the memory via cache. They do not get altered in the cache. The cache changes the values directly in the memory. So, the values in the cache remains unaffected till the cache line cycle is over.

The above flags, manipulate the registers to change the value in the cache (which does not happen in normal times). So, when the same value is used somewhere else, instead of the older value, the updated value gets used.

The problem is, during the intermediate operations, these additional precision digits may stay or may not get properly written in the cache. This varies between systems, programs, compilers and even the algorithms/routines and the way they are used.

You can try this for fun, but do not anticipate the same answer in other machines or while doing the execution in some other way. This trick is recommended to try when you implement the same code, in a normal usual way, in different machines but get different results, with one reason possibly because of dilemma in truncations.
Sometimes, this is good, but some times, it destroys reproducibility. Because, this tweaking works differently in different systems and architecture.

This is one of the several kind of a problems that used to happen in olden days when many people made computer systems, because each manufacturer used to make their own way of doing computer arithmetic. After standardization, the problems got mitigated very much. But some issues still pop-up.

## Timing Code in Fortran

There is a subroutine named system clock to measure the time taken for a code to be executed completely.
To use it,

```fortran
call system_clock(var1, var2) !both variables are to be integers
```
Variable 1 will have the elapsed clock cycles of the system from the point where the code is executed to the current line. The unit will be cycles.

Variable 2 will have the clock rate or the rate at which the system/cpu is operating. The unit will be cycles per second.

eg:

```fortran
call system_clock(tclock1)
 ! <code to be executed>
call system_clock(tclock2, rate)

elapsed_time = float(tclock2 - tclock1)/float(rate)
```

To look at the cpu time, use ```cpu_time subroutine ```

eg:
```fortran
call cpu_time(time1) !the variable is a float with time in seconds.
  ! <code to be executed>
call cpu_time(time2)

elapsed_time = time2 - time1
```

## BLAS LAPACK

BLAS (Basic Linear Algebra Subroutines) and LAPACK (LA Pack or Linear Algebra Package) are linear algebra and scientific packages used by Fortran, Matlab, Python, Scilab and many other programs. LAPACK kind of depends on BLAS for some of it's functions.

They provide functions and sub-routine definitions for performing the above mentioned operations. They are made in both C and Fortran.

Fortran does not have an equivalent of Matlab's A\b linear algebra operation. This is done using LAPACK.
Under the hood, Matlab and Numpy also need LAPACK to do these!
