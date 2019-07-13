# Java Programming

```Java

/* Program to print hello world in Java */

// In Java, everything begins with a class
class hello
{
    // method - function inside a class
    // main is the primary method! All other methods must run through
    // main method
    public static void main(String args[])
    {
        System.out.println("Hello World!");
        // A versatile print line statement. (can print in file/output)
        // print line has a return statement
        
        double x, y, z; // Double variables
        x = 7.8;
        y = 9.4;
        // simple initializations
        z = x + y; // addition
        
        // ASMD + - * /
        // modulus %
        // increment decrement ++a, a++, --a, a--,
        // assignment operators: a += 6, b -=5, c *= 1, d /=2, e %= 2
        
        // int a, b, c; // Integer variables
        
        System.out.print("The sum of x = ");
        // Prints a string or a variable as it is without any return
        System.out.print(x);
        System.out.print(" and y = ");
        System.out.print(y);
        System.out.print(" is z = ");
        System.out.println(z);
    }
    // to compile, use javac <filename.java>
    // to run, use java <classname.class>
}

```

```Java

/* Program for getting user input via scanner */

import java.util.Scanner;
// to import methods/classes/objects from library files
// This is used for getting user input.

class scan
{
    // method - function inside a class
    // main is the primary method! All other methods must run through
    // main method
    public static void main(String args[])
    {
        
        Scanner x = new Scanner(System.in);
        // prepares a scanner variable to get data from the user!
        
        System.out.println(x.nextLine());
        // x.nextLine() invokes the scanner call. The data is received
        // as a string due to nextLine() method
        // println method prints the result
        
    }
    // to compile, use javac <filename.java>
    // to run, use java <classname.class>
}


```

```Java

/* Calculator Program */

import java.util.Scanner;
// Scanner method for getting data from user

class calculator
{
    public static void main(String args[])
    {
        double num1, num2, ans;
        
        Scanner x = new Scanner(System.in);
        // Setting a Scanner variable to get data from user!
        
        System.out.println("Enter number 1:");
        // for user clarity
        num1 = x.nextDouble();
        // This invokes the scanner call to get a value
        // value of x gets converted into a double and assigned to num1
        
        System.out.println("Enter number 2:");
        // for user clarity
        num2 = x.nextDouble();
        // This invokes the scanner call to get a value
        // the old value is replaced by the new user value
        // value of x gets converted into a double and assigned to num2
        
        ans = num1 + num2;
        System.out.print("The answer is ");
        System.out.println(ans);
    }
}


```

```Java

/* Program to demonstrate if clause and switch case */

class constructs
{
    public static void main(String args[])
    {
        int test = 4;
        
        // Relational operators == > < >= <= !=
        // Logical operators && || !
        
        if (test == 9)
        {
            System.out.println("test is 9");
        }
        else if (test >= 9)
        {
            if (test > 9)
            {
                System.out.println("test is greater than 9");
            }
            else
            {
                System.out.println("test is 9");
            }
        }
        else if (test <= 9)
        {
            if (test < 9)
            {
                System.out.println("test is less than 9");
            }
            else
            {
                System.out.println("test is 9");
            }
        }
        else
        {
            System.out.println("test is not at all 9");
        }
        
        switch(test)
        {
            case 0:
                System.out.println("You got 0!");
            break;
            case 1:
                System.out.println("You got 1!");
            break;
            case 2:
                System.out.println("You got 2!");
            break;
            case 3:
                System.out.println("You got 3!");
            break;
            case 4:
                System.out.println("You got 4!");
            break;
            case 5:
                System.out.println("You got 5!");
            break;
            default:
                System.out.println("You got something else!");
            break;
        }
    }
}

```

Nesting is possible with if statements

```Java

/**
 * Created by arun on 17/07/2016.
 * program 15
 */

public class nested_if
{
    public static void main(String args[])
    {
        int age = 20;

        if(age < 10)
        {
            System.out.println("You are too young!");
        }
        else
        {
            System.out.println("You are of good age!");
            if(age > 75)
            {
                System.out.println("Hello Grandpa / Grandma!");
            }
            else
            {
                System.out.println("You're younger than 75");
            }
        }

        // if there is just a statement followed by if or else of or else, then
        // {} are not needed!
        if(age <= 10)
        {
            System.out.println("You are too young!");
        }
        else if(age >10 && age <= 18)
        {
            System.out.println("You are an adolescent teen!");
        }
        else if(age > 18 && age <= 50)
        {
            System.out.println("You are on your own!");
        }
        else
        {
            System.out.println("You're a senior citizen!");
        }
    }
}


```

```Java

/**
 * Created by arun on 17/07/2016.
 * program 10
 * This explains the while loop
 */

public class while_loop
{
    public static void main(String args[])
    {
        int counter = 0;

        // simple while loop explanation
        while(counter<10)
        {
            System.out.println(counter);
            counter++;
        }
    }
}

```

Using Multiple classes is easy

```Java

/**
 * Created by arun on 17/07/2016.
 * program 11 part 1
 * part 2 is classes2.java
 */

public class classes1
{
    public static void main(String args[])
    {
        // class name, object name = new class name
        classes2 classes2_obj = new classes2();

        classes2_obj.simple_message();
    }
}

/**
 * Created by arun on 17/07/2016.
 * program 11 part 2
 * part 1 is classes1.java
 */

public class classes2
{
   public void simple_message()
   {
       System.out.println("Hello from simple message method in class classes2");
   }
}

```

Methods can have arguments/parameters too ...

```Java

/**
 * Created by arun on 17/07/2016.
 * program 12 part 1
 * part 2 meth_params.java
 */

import java.util.Scanner;

public class methods_parameters
{
    public static void main(String args[])
    {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter your name");

        String name = input.nextLine();
        // simple_message(name); // this also works
        methods_parameters.simple_message(name);

        // creating a new class object
        meth_params params1 = new meth_params();

        params1.sim_mess(name);
    }

    // method with an argument
    public static void simple_message(String name)
    {
        System.out.println("Hello "+name);
    }
}

/**
 * Created by arun on 17/07/2016.
 * program 12 part 2
 * part 1 methods_parameters.java
 */

public class meth_params
{
    public void sim_mess(String name)
    {
        System.out.println("Hello "+name+"! Nice to meet you!");
    }
}

```

It is possible to have variables inside classes. These are instance variables. They are accessible to the methods inside the class.

```Java

/**
 * Created by arun on 17/07/2016.
 * program 13 part 2
 * part 1 methods_instances1.java
 */

public class methods_instances2
{
    // this is a private variable.
    // it is accessible to and can be modified only by the methods in the parent class!
    // Also, this is an instance variable: a variable used outside
    // methods and inside classes
    private String progname;

    public void setName(String name)
    {
        // this method sets the progname to be the specified name
        progname = name;
    }

    // this method returns a String
    public String getName()
    {
        return progname;
    }

    // printing method
    public void saying()
    {
        // this is a print statement with a format!
        // %s is for a string format
        System.out.printf("Your first programming language was %s", getName());
    }
}

/**
 * Created by arun on 17/07/2016.
 * program 13 part 1
 * part 2 methods_instances2.java
 */

import java.util.Scanner;

public class methods_instances1
{
    public static void main(String args[])
    {
        Scanner input = new Scanner(System.in);

        methods_instances2 mi_obj = new methods_instances2();

        System.out.println("Enter your first programming language:");
        String var = input.nextLine();

        mi_obj.setName(var);
        mi_obj.saying();
    }
}

```

Constructors are used for initializing the instance variables inside the objects during the time of creation. If these variables are used without prior initialization, then they would show "null" as output.

Constructor has the same name as that of the class.

```Java

/**
 * Created by arun on 17/07/2016.
 * program 14 part 2
 * part 1 constructor1.java
 */
public class constructor2
{
    // this is a private variable.
    // it is accessible to and can be modified only by the methods in the parent class!
    // Also, this is an instance variable: a variable used outside
    // methods and inside classes
    private String progname;

    // this is a constructor!
    // constructor is used for initializing instance variables
    // when the objects are immediately created.
    // constructor has the same name as that of the class
    public constructor2(String name)
    {
        progname = name;
    }

    public void setName(String name)
    {
        // this method sets the progname to be the specified name
        progname = name;
    }

    // this method returns a String
    public String getName()
    {
        return progname;
    }

    // printing method
    public void saying()
    {
        // this is a print statement with a format!
        // %s is for a string format. \n for new line
        System.out.printf("Your first programming language was %s\n", getName());
    }
}


/**
 * Created by arun on 17/07/2016.
 * program 14 part 1
 * part 2 constructor2.java
 */
public class constructor1
{
    public static void main(String args[])
    {
        // constructor is used for initializing instance variables
        // when the objects are immediately created.
        // Now, we are passing the value "C" for the instance variable
        // inside the class object
        constructor2 cons = new constructor2("C");

        cons.saying();

    }
}


```

You have conditional operator in Java. It is a short-hand if else statement.

```Java
public class conditional_ops
{
    public static void main(String args[])
    {
        int age = 61;

        // Conditional operator. condition? statement if yes: statement if no
        System.out.println(age>50?"You're old!":"You're young!");
    }
}
```

Simple for loop demonstration.

```Java
public static void main(String args[])
    {
        for(int i=0; i<10; i++) // i += 1
        {
            System.out.println("The value of i is "+i);
        }
    }
```

Simple do-while loop demonstration

```Java

    public static void main(String args[])
    {
        // do while loop executes the body, even without checking the
        // condition once.

        int counter = 12;

        do
        {
            System.out.println(counter);
            counter++;
        }
        while(counter<=10);

    }
```

Mathematical methods in Java

```Java
// random class for random number functions
import java.util.Random;

public class math_class
{
    public static void maths_1()
    {
        System.out.println(Math.abs(-26.7));
        System.out.println(Math.ceil(26.7));
        System.out.println(Math.floor(26.7));
        System.out.println(Math.max(8.6, 5.3));
        System.out.println(Math.min(8.6, 5.3));
        System.out.println(Math.pow(4.1, 5.3));
        System.out.println(Math.sqrt(4.1));

    }
    public static void maths_2()
    {
        Random dice = new Random();
        int number;

        for(int counter=1; counter<=10; counter+=1)
        {
            // generates a random integer between 0 and
            // n-1 inclusive of 0 and n-1 if option is n.
            // since result is between 0 and n-1, we add
            // 1 to them to set the limits between 1 and n
            number = 1 + dice.nextInt(6);
            System.out.println("Number = "+number);
        }
    }
    public static void main(String args[])
    {
        maths_1();
        maths_2();
    }
}
```

Arrays are available in Java

```Java

/**
 * Created by arun on 18/07/2016.
 * program 21
 */
public class arrays1
{
    public static void main(String args[])
    {
        // empty integer array with 10 entries
        int ar_var[] = new int[10];

        // declare and initialize the array and its size!
        // array initializer
        int var[] = {1, 2, 3, 4, 5, 6};

        // index starts from 0 and goes to n-1
        // uninitialised array entries are set to zero.
        ar_var[0] = 56;
        ar_var[1] = 5896;
        ar_var[9] = 5896;

        // display individual values
        System.out.println(var[3]);
        System.out.println(ar_var[9]);

        // printing in a standard array table manner.
        // \t creates a 4-6 space tab
        System.out.println("Index\tValue");

        // var.length is the array length
        for(int counter = 0; counter <var.length; counter++)
        {
            System.out.println(counter+"\t\t"+var[counter]);
        }

        // sum all the elements in an array
        int sum = 0;
        for(int counter = 0; counter <var.length; counter++)
        {
            sum += var[counter];
        }
        System.out.println("The sum of the array is: "+sum);
    }
}

public class arrays2
{
    public static void main(String args[])
    {
        int var[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

        System.out.println("Before change:");

        for(int y: var)
        {
            System.out.println(y);
        }

        // calling the method
        change(var);
        // alternate call
        // arrays2.change(var);

        System.out.println("After change:");

        for(int y: var)
        {
            System.out.println(y);
        }
    }
    // creating a new method with an integer array parameter
    public static void change(int x[])
    {
        // increment each entry of the array by 5
        for(int counter = 0; counter <x.length; counter++)
        {
            x[counter] += 5;
        }
    }
}

public class arrays3
{
    public static void main(String args[])
    {
        // creating a 2D array. first [] for row, the next for column
        // indices start from 1
        // 00,01,02,03,10,11,12,13 - index order
        int array1[][] = { {8,9,10,11}, {12,13,14,15} };
        // Arrays with uneven rows
        // 00,01,10,11,20,21,22,30 - index order
        int array2[][] = { {8,9}, {10,11}, {12,13,14}, {15} };

        System.out.println("This is array1:");
        display(array1);
        System.out.println("This is array2:");
        display(array2);

        System.out.println(average(45,67,78,24,12,34,56));
    }

    public static void display(int arr[][])
    {
        // row length
        for(int row = 0; row < arr.length; row++)
        {
            // column length = any row.length
            for(int column = 0; column < arr[row].length; column++)
            {
                System.out.print(arr[row][column]+"\t");
            }
            System.out.println();
        }
    }

    /// ... means many arguments
    public static double average(double ... numbers)
    {
        double total = 0;
        for(double x:numbers)
        {
            total += x;
        }
        return total/numbers.length;
    }
}

```

Java has enhanced for loops. These progress element-wise in arrays instead of using the indices.

```Java

public class enhanced_loop
{
    public static void main(String args[])
    {
        int var[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        int total = 0;

        // this is similar to "for x in var".
        // x will be one value during one iteration
        for(int x: var)
        {
            total += x;
        }

        System.out.println("The total of the array is: "+total);
    }
}

```

Examples for string formats and "this" keyword

```Java
/**
 * Created by arun on 20/07/2016.
 * program 26
 */
public class time_class
{
    // instance variables for the class
    // private keyword makes them exclusive to the this
    // class methods.
    private int hour  = 2;
    private int minute = 2;
    private int second = 2;

    public void setTime(int h, int m, int s)
    {
        // get the value of hour, minute and second from the
        // user and assign it to the instance variables.
        // If there is any error, then the instance variables
        // are set to zero
        hour   = ((h>=0 && h<24)?h:0);
        minute = ((m>=0 && m<60)?m:0);
        second = ((s>=0 && s<60)?s:0);
    }

    // used for explaining "this" keyword
    // If the constructor or the method uses variable names
    // identical to the instance variables, then the method
    // will refer to the instance variables.
    // to make sure that the local variables are used, use
    // "this" keyword
    public void setTime2(int hour, int minute, int second)
    {
        this.hour   = 4;
        this.minute = 20;
        this.second = 20;
    }

    public String military_fmt()
    {
        // prints time in military or 24 hour format.
        // the format method defines the format in which the data
        // should be placed inside the string
        // %d is for int. 02 means two spaces to print the integer
        return String.format("%02d:%02d:%02d",hour, minute, second);
    }

    public String normal_fmt()
    {
        // prints time in normal or 12 hour format.
        // the format method defines the format in which the data
        // should be placed inside the string
        // %d is for int. 02 means two spaces to print the integer
        return String.format("%02d:%02d:%02d %s",((hour==0||hour==12)?12:hour%12),
                minute, second, (hour<12?"AM":"PM"));
    }
}
```

There can be multiple constructors for a class. However, the constructors can be replicated on the basis of how many arguments they take.

```Java
/**
 * Created by arun on 20/07/2016.
 * program 28 part 2
 * part 1 multi_cons.java
 */
public class multiple_constructors
{
    private int hour;
    private int minute;
    private int second;

    // you can define multiple constructors having different
    // set of argument list. It is called as constructor overloading

    // a constructor with zero arguments
    // if the user entered no argument(s), then this constructor is used
    public multiple_constructors()
    {
        // this() means the same constructor with the full argument list!
        // so, for this example,
        // this(0,0,0) means multiple_constructors(int h, int m, int s)
        // with h = 0, m = 0 and s = 0
        this(0,0,0);
    }

    // a constructor with one arguments
    // if the user entered 1 argument(s), then this constructor is used
    public multiple_constructors(int h)
    {
        this(h,0,0);
    }

    // a constructor with two arguments
    // if the user entered 2 argument(s), then this constructor is used
    public multiple_constructors(int h, int m)
    {
        this(h,m,0);
    }

    // a constructor with three arguments
    // if the user entered 3 argument(s), then this constructor is used
    public multiple_constructors(int h, int m, int s)
    {
        setTime(h,m,s);
    }

    // this method will set the time
    public void setTime(int h, int m, int s)
    {
        setHour(h);
        setMinute(m);
        setSecond(s);
    }

    public void setHour(int h)
    {
        hour   = ((h>=0 && h<24)?h:0);
    }

    public void setMinute(int m)
    {
        minute   = ((m>=0 && m<60)?m:0);
    }

    public void setSecond(int s)
    {
        second   = ((s>=0 && s<60)?s:0);
    }

    public int getHour()
    {
        return hour;
    }

    public int getMinute()
    {
        return minute;
    }

    public int getSecond()
    {
        return second;
    }

    public String military_fmt()
    {
        // prints time in military or 24 hour format.
        // the format method defines the format in which the data
        // should be placed inside the string
        // %d is for int. 02 means two spaces to print the integer
        return String.format("%02d:%02d:%02d",getHour(), getMinute(), getSecond());
    }
}

public class multi_cons
{
    public static void main(String args[])
    {
        multiple_constructors mc1 = new multiple_constructors();
        multiple_constructors mc2 = new multiple_constructors(5);
        multiple_constructors mc3 = new multiple_constructors(5,13);
        multiple_constructors mc4 = new multiple_constructors(5,13,43);

        System.out.printf("%s\n", mc1.military_fmt());
        System.out.printf("%s\n", mc2.military_fmt());
        System.out.printf("%s\n", mc3.military_fmt());
        System.out.printf("%s\n", mc4.military_fmt());
    }
}
```

Composition, string description for the class

```Java

public class app3_1
{
    public static void main(String args[])
    {
        app3_3 obj1 = new app3_3(20,7,2016);

        // passing a string and an object
        // this is an example for composition:
        // passing objects as members
        app3_2 obj2 = new app3_2("Arun", obj1);

        System.out.println(obj2);
    }
}

public class app3_2
{
    private String name;

    // this is a composition: a reference or a link to the
    // objects of some other class
    private app3_3 day;

    public app3_2(String theName, app3_3 theDay)
    {
        name = theName;
        day = theDay;
    }

    public String toString()
    {
        return String.format("My name is %s, my birthday is %s", name, day);
        // since day is a reference to a value inside the object. Since, there is
        // no string inside the object, because of the toString method, the usage
        // "day" brings the string used in the toString method from the object and
        // uses it here.
    }
}

public class app3_3
{
    private int date;
    private int month;
    private int year;

    public app3_3(int d, int m, int y)
    {
        date = d;
        month = m;
        year = y;

        // here, the keyword "this" is a reference to the object built in this class
        // so, you need a method that returns a string for this object.
        System.out.printf("The constructor for this is %s\n", this);
    }

    // this returns the string for the constructor. This has to be named as mentioned
    public String toString()
    {
        return String.format("%d/%d/%d", date, month, year);
    }
}

```

Enumeration is a type of pre-defined constant objects in Java

```Java

// this is used for accessing the enum arrays
import java.util.EnumSet;

public class enum_example
{
    public static void main(String args[])
    {
        // .values() is a static method that gives an array
        // for the enum class
        for(enum_ex languages: enum_ex.values())
        {
            // using the methods, we get the language description, the age
            System.out.printf("%s\t\t%s\t\t%d\n",languages, languages.getDesc(), languages.getAge());
        }

        System.out.println("\n And now for the range of constants!!!\n");

        // get only a range between a starting and an ending point
        for(enum_ex languages: EnumSet.range(enum_ex.c, enum_ex.fortran))
        {
            // using the methods, we get the language description, the age
            System.out.printf("%s\t\t%s\t\t%d\n",languages, languages.getDesc(), languages.getAge());
        }
    }
}

// enum stands for enumeration and it is used for creating constants
// it is kind of like class
public enum enum_ex
{
    // these constants are objects of type enum and have their own
    // set of variables
    python("Awesome", 23),
    java("Procedures", 24),
    c("Challenging", 15),
    cpp("Confusing", 16),
    matlab("Mix_feelings", 18),
    fortran("Easy",23),
    shell("Powerful", 22);

    // final keyword sets the final value of the constants
    // these instance variables set the variable names
    // and variable type and attributes for the constants
    // desc is the description variable for the objects
    // age is the age variable for the objects

    private final String desc;
    private final int age;
    
    // Also, if you want to have constants inside classes
    // then add "final" keyword to the instance variables

    // creating an enumeration constructor
    enum_ex(String description, int start_age)
    {
        desc = description;
        age = start_age;
    }

    public String getDesc()
    {
        return desc;
    }

    public int getAge()
    {
        return age;
    }
}

```

#### Static Variables

```Java
public class static_var2
{
    public static void main(String args[])
    {
        // Able to get static variable data even without having objects
        // and directly from the class
        System.out.println(static_var1.getmember());

        // Creating a few objects
        static_var1 member1 = new static_var1("AR", "Rahman");
        static_var1 member2 = new static_var1("Abdul", "Kalam");
        static_var1 member3 = new static_var1("Albert", "Einstein");
        static_var1 member4 = new static_var1("Sachin", "Tendulkar");

        System.out.println();
        System.out.println(member1.getfirst_name());
        System.out.println(member1.getlast_name());
        System.out.println(member1.getmember());
        System.out.println();
        System.out.println(member2.getfirst_name());
        System.out.println(member2.getlast_name());
        System.out.println(member2.getmember());
        System.out.println();
        System.out.println(member3.getfirst_name());
        System.out.println(member3.getlast_name());
        System.out.println(member3.getmember());
        System.out.println();
        System.out.println(member4.getfirst_name());
        System.out.println(member4.getlast_name());
        System.out.println(member4.getmember());
    }
}


// static variables are used for updating common information for all objects under the same class.
// if certain information is common to all objects, then instead of creating a variable
// inside the class and updating all the objects one after the other, defining one
// static variable is sufficient. If done, then if one of the objects modify the value of this variable,
// then that change is reflected in all the objects.
// example: mathematical constants across mathematical class objects

public class static_var1
{
    // instance variables
    private String first_name;
    private String last_name;

    // defining a static variable with a pre-set value
    private static int member = 0;

    public static_var1(String fn, String ln)
    {
        first_name = fn;
        last_name = ln;
        member++;

        System.out.println("The new person in my wishlist is: "+first_name+" "+last_name);
        System.out.println("No. of persons in my wishlist is: "+member);
    }

    public String getfirst_name()
    {
        return first_name;
    }

    public String getlast_name()
    {
        return last_name;
    }

    public static int getmember()
    {
        return member;
    }
}

```

### Inheritance

If you want to include all the ``public`` methods and variables into a new class, then inheritance is useful. Instead of writing and replicating the same methods and variables into new classes, the new classes can "inherit" them.

To inherit them, the new class should be written with the keyword ``extends``

example:

```Java
public class children extends parents
{
    ...........
}
```

Here, all the public methods and variables of *_parents_* class is inherited by the children class. The **_parent_** class is the **_super_** Class or the **_parent_** because it is stand-alone. The **_children_** class is the **_sub-class_** or the **_child_** because it depends on the super class.

Inside the sub-class, you can over-write the definitions of the methods and variables inherited from the super class. However, this over-writing does not affect the super class.

Only ``public`` methods and variables can be inherited. Private methods and variables are not inheritable.

Also, chain/successive inheritance is possible, consistent with the above rules and conditions.

```Java
// intro to Graphical User Interfaces

// This class has a lot of GUI methods
import javax.swing.JOptionPane;

public class gui1
{
    public static void main(String args[])
    {
        // addition program
        String fn = JOptionPane.showInputDialog("Enter number1:");
        String sn = JOptionPane.showInputDialog("Enter number2:");
        // this dialog box gets the input value as strings!

        // converting string to int using explicit conversion
        int num1 = Integer.parseInt(fn);
        int num2 = Integer.parseInt(sn);

        int sum = num1 + num2;

        // Displays output on the screen
        // It takes 4 parameters: position parameter, the message to display
        // title of the window, a system icon message
        // null means no specific position for the GUI. So it will
        // be in the centre.
        // As of now, we are using no specific icon - hence plain message
        JOptionPane.showMessageDialog(null, "The answer is "+sum, "Addition Program", JOptionPane.PLAIN_MESSAGE);
    }
}

```

```Java
// this is a better, more enhanced and complex GUI example

// manages the "placement" of the icons and items. It places
// items to the right of the previous item and on the next line
// if space runs out in the current line
import java.awt.FlowLayout;

// inherits the feel, features and looks of the OS on which it is run on.
import javax.swing.JFrame;

// allows output of text and images on the screen.
import javax.swing.JLabel;

// inheriting all the methods from JFrame class
public class gui21 extends JFrame
{
    // a JLabel object for placing a label/image
    private JLabel item1;

    public gui21()
    {
        // title for the window
        super("Title of Window");
        // setting a layout for the window
        // new flowlayout sets a default layout for the window
        setLayout(new FlowLayout());

        // initializing the item
        item1 = new JLabel("This is a sentence");
        // this message shows up when the mouse pointer comes over
        // the label
        item1.setToolTipText("This will show on hover");
        // adding the item to the window
        add(item1);
    }
}

// inherits the feel, features and looks of the OS on which it is run on.
import javax.swing.JFrame;

public class gui22
{
    public static void main(String args[])
    {
        // creating a GUI object
        gui21 g1 = new gui21();
        // sets how the program has to terminate.
        // this tells that the program terminates by clicking the
        // close/exit button
        g1.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // set the size of the window width, height
        g1.setSize(275,180);
        // sets the visibility of the window.
        // if set false, then it appears and vanishes instantly
        g1.setVisible(true);
    }
}
```
