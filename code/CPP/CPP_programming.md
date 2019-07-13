# C++ Programming

<!-- TOC -->

- [C++ Programming](#c-programming)
  - [Sources:](#sources)
  - [Sample C++ Program](#sample-c-program)
  - [Variables and basic arithmetic](#variables-and-basic-arithmetic)
  - [If Statement](#if-statement)

<!-- /TOC -->

## Sources:

* Bucky Roberts - thenewboston - YouTube channel

## Sample C++ Program

```C++
// This is a comment

// This is a pre-processor directive
// iostream is a "header file" having definitions of functions
// that would be useful in the program.
// we are including the header file iostream - input/output stream
#include <iostream>

// std = standard library. 
// This includes the stardard functions in the library of C++
using namespace std;

// This is the main function. This is MANDATORY for a program
// All executions are to be done through main fucntion because it is
// the first function to be executed by the program
// int = this function returns integers
// main is the fucntion name.
// the definition of a function are to be included inside {}
int main()
{
    //output stream object - for printing/writing data to the screen
    // << is the stream insertion operator
    // endl - end line or go to the next line
    // if not, then the next cout expression will print the statement
    // from where the previous statement stopped.
    // \n - escape sequence to jump to a new line
    // terminate statements with ;
    cout << "Hello World! \n" << endl;
    
    // functions calculate something and returns a value.
    // this line helps the function to return a value.
    // 0 means the program ran fine!
    return 0;
}
```

## Variables and basic arithmetic

```C++
// var_name is a variable of integer type.
// it stores the value 7 - assignment
int var_name = 7;

// variable declaration
int a, b;

// this prints the variable value
cout << var_name;

// entering a value from the user
cout << "Enter a value for a:";
// cin - input stream object 
// >> - stream extraction operator
cin >> a;

// assigning value manually
b = 5;

// basic arithmetic - ASMD
a + b
a - b
a * c
a / d

```

## If Statement

```C++
if(x<10)
{
    cout << "x is less than 10!";
}
else if(x<20 && x>=10)
{
    cout << "x is greater than 10 and less than 20!";
}
else if ****
........
.......
else
{
    cout << "Don't know what to do now!"
}
```
