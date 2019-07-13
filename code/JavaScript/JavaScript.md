# JavaScript

It is a scripting language used for programming webpages and doing arithmetic in webpages and for including interactions!.

There are several scripting languages for the purpose, like PHP. JavaScript is one of them!

## Prerequisites

Before picking up JavaScript, it is required to know,

* Knowledge in HTML
* Knowledge in CSS

If these are missing, then picking up JavaScript becomes difficult!

As far as softwares are concerned, you need

* One nice text editor
    * Notepad, Notepad++, geany, gedit, textmate, Eclipse, Webstorm, Netbeans, Aptana, etc.,
* One or more web browser
    * Google Chrome, Mozilla Firefox, Opera, Safari, Internet Explorer etc.,

## Writing JavaScript code inside HTML pages

You can include the javascript code inside HTML pages via the ``` <script> ``` tag or by including the javascript using some inclusion tags.

To write a javascript command inside html page, use the ``` <script> ``` tag as below. The type attribute defines the scripting language used.

```HTML

    <script type="text/javascript">
    // This is a single line comment
    /* This is a multi-line comment */
    <!--
        document.write("Hey There!");
    //-->
    // This is a print statement!
    </script>
```

``` document.write(); ``` is a print statement! The ``` <!-- ``` and ``` //--> ``` is just a safety check!

## Safety Check!

Some older browsers may not work nicely with javascript. Instead of executing the code, they might just print them. A safety check is used, so that the code is either ignored (in case of older browsers) or execute them (in the case of newer browsers.). Enclose the javascript code inside the code as above!

## Comments

To include comments, use ``` // ``` for a single line of comment. Use ``` /* ``` and ``` */ ``` for multi-line comments.

## Variables

To include a variable, use the syntax.
```JavaScript
    var var_name = value
```
eg:

```HTML
<script type="text/javascript">

    var v1 = 45;        // Integer
    var v2 = 45.28;     // Decimal
    var v3 = -45.8;     // Negative
    var str1 = "String" // Strings
    var str2 = " Jon said \" Be Brave man! \" to Sam";
    var str3 = " Jon said ' Be Brave man! ' to Sam";
    // Escape Sequences. Use \ for beginning an Escape Sequence!
    var bool = true;    // Boolean
    var bool1 = false;  // Boolean
    var v4 = null;      // Null or empty variable!
    // No value is assigned to v4

// Quotation marks are not needed, but it is needed for clarity and differentiation.

    document.write(str2 + " Is he not write? He has proved it " + v1 + " times!");
    // Will join strings and numbers, and print them in a line!
    
    document.write(v1+v2);
    // If plain numbers are used, then they are added normally!

</script>
```

** Variables are case sensitive! **

## Functions

It is a mini-program!

```HTML

<body>

    <script type="text/javascript">
    // Functions!

    // This is the function definition!
    function func_name()
    {
        alert("This is an alert!");
        // This will put a pop-up on the screen!
    }

    function func_name1(x)
    {
        // It takes an argument X and uses it!
        alert("This is an alert! by "+ x);
        // This will put a pop-up on the screen!
    }

    func_name();
    /* This is the function call!  When called, there will be a 
    pop-up indicating the message!*/

    func_name1("Arun");
    /* This is also a function call */

    </script>

    <form>
        <input type="button" value="Alert!" onclick=func_name() />
        <!-- This will create an button with the name Alert!.
        On clicking the button, the function will be invoked and 
        the pop-up will display! -->
    </form>

</body>

```

## Advanced function operations

**Functions with multiple input arguments**

**Functions with return values**

**Function called inside another function**

```HTML
<body>

    <script type="text/javascript">

        function power(x, y)
        {
            document.write("We are inside power function! "+"<br />");
            document.write("The received values are :" + "<br />" + x + " and " + y +"<br />");
            // This function receives 2 arguments/parameters
            // using <br /> inside quotes serves as a line break!
            var p = Math.pow(x,y); // Power function in JavaScript!
            document.write("The value of "+x+" ^ "+y+" is: "+p+"<br />");
        }

        function fahren_2_cel(f)
        {
            document.write("We are inside fahren_2_cel function! "+"<br />");
            var c = (f-32.0)*(5.0/9.0);
            return c;
            // Function that returns a value!
        }

        function print(f)
        {
            document.write("The value of " + f + " degree Fahrenheit is " + fahren_2_cel(f) + " degree Celsius!"+"<br />");
            // Calling functions inside another functions!
            document.write("We are inside print function! <br />");
        }

        function start()
        {
            document.write("We are inside start function! <br />");
            power(5.01, 1.20);
            print(212.0);
            document.write("We are back to start function! <br />");
        }

    </script>

    <form>
        <input type="button" value="start" onclick="start()" />
    </form>

</body>
```

The output on pressing the button is:

```

We are inside start function! 
We are inside power function! 
The received values are :
5.01 and 1.2
The value of 5.01 ^ 1.2 is: 6.915208372830329
We are inside fahren_2_cel function! 
The value of 212 degree Fahrenheit is 100 degree Celsius!
We are inside print function! 
We are back to start function! 

```

## Global and Local Variables

```HTML
<script type="text/javascript">
            
    var var1 = "global "; // Global variable!

    function print1()
    {
        var var1 = "local ";  // Local Variable!
        document.write(var1); // Local usage!
    }

    function print2()
    {
        document.write(var1); // Global usage
    }

    print1();
    print2();

    document.write(var1); // Global usage

</script>
```

The output is

```
local global global
```

## Mathematical Operations

```HTML
<script type="text/javascript">
            
    var a = 5+6;            //Addition
    var b = 8-9;            //Subtraction
    var c = 8*9;            //Multiplication
    var d = 8/9;            //Division
    var e = 25%9;           //Modulus Operation
    var f = Math.pow(2,3);  //Power Operation
    var g = 10;
    g++;                    // Increment Operation
    document.write(g + "<br />");
    g--;                    // Decrement Operation
    document.write(g + "<br />");
    g = 10;
    g += 10;                // Add and assign operator
    document.write(g + "<br />");
    g = 10;
    g -= 10;                // Subtract and assign operator
    document.write(g + "<br />");
    g = 10;
    g *= 10;                // Multiply and assign operator
    document.write(g + "<br />");
    g = 10;
    g /= 10;                // Divide and assign operator
    document.write(g + "<br />");
    g = 10;
    g %= 10;                // Modulus and assign operator
    document.write(g + "<br />");
    document.write("The calculated values are <br />");
    document.write(a + "<br />" + b + "<br />" + c + "<br />" + d + "<br />" + e + "<br />")

</script>
```

The output is:

```
11
10
20
0
100
1
0
The calculated values are 
11
-1
72
0.8888888888888888
7

```

## If statement and Relational Operators

```HTML
<script type="text/javascript">

    var a = 7;
    var b = 7;

    if( a > b)
    {
        document.write(a + " is greater than " + b + "<br />");
    }
    else if( a < b)
    {
        document.write(a + " is less than " + b + "<br />");
    }
    else
    {
        document.write(a + " is equal to " + b + "<br />");
    }

    // Relational Operators
    // >    Greater than,
    // <    Less than,
    // ==   equals,
    // >=   Greater than or equal to
    // <=   Less than or equal to
    // !=   Not Equal to
    
    // Logical Operators
    // &&   AND
    // ||   OR

</script>
```

The output is :

```
7 is equal to 7
```

**Nesting is possible!**

## Switch Case:

It is given as follows:

```HTML

<script type="text/javascript">
            
    var a = 7;

    switch(a)
    {
        case 0:
        case 1:     // Multiple common cases!
            document.write("a is 0 or 1");
            break; // break to stop checking the next cases.
        case 2:
        case 3:
        case 4:
            document.write("a is 2 or 3 or 4");
            break;
        case 5:
        case 6:
        case 7:
            document.write("a is 5 or 6 or 7");
            break;
        case 8:
        case 9:
            document.write("a is 8 or 9");
            break;
        default:
            document.write("a is something else!");
            // break; // break not needed!
    }

</script>

```

## For  and While loops

```HTML
<script type="text/javascript">

    // This is a for loop!
    // initialization, ending condition, increment/decrement
    for(i=0; i<10; i++)
    {
        document.write("The value of i is "+i+" <br />");
    }

    // This is a while loop condition variable
    var x = 1;

    // This is a while loop
    while(x<10) // This is the condition
    {
        // Set of statements to be executed
        document.write("The value of x is "+x+" <br />");
        // This is a condition breaker statement!
        x++;
    }

    // This is a do while loop condition variable now!
    x = 1;

    // This is a do while loop
    // Run the code (regardless of the condition) and then check the condition!
    do
    {
        // Set of statements to be executed
        document.write("The value of x is "+x+" <br />");
        // This is a condition breaker statement!
        x++;
    }
    while(x<10); // This is the condition!

</script>
```

## Event Handlers

These are used for doing a specific job when a certain **event** happens, like press of a button, entering a value, etc.,

Event handler codes need not be written inside ``` <script> ``` tags!.

```HTML
<body onload="alert('Loading complete!');" onUnload="alert('See you!');">
        
     <!-- This is an On Load and On Unload Event handlers. When the webpage is loaded, the onload event happens. When the wepage is closed, refreshed or terminated, the onUnload event happens. Use either one, not both!-->
        
    <!-- On click Event handler! -->
    <form>
        <input type="button" value="Press" onClick="alert('Nice!');alert('Nice again!')"/>
        <!-- You have a button, with the name "Press". On clicking
        the button, the javascript code alert('Nice!'); is executed.
        Single quotes are used for user convenience and to avoid 
        string termination. -->

        <!-- You can add multiple statements! After alert('Nice!'),
        alert('Nice again!'); is executed. So, if you have a function,
        you can execute a series of statements. -->
    </form>

    <!-- on mouse over even handler! -->

    <a HrEf="http://google.com" onmouseover="alert('Going to Google!');"> Click to go to Google! </a>

    <!-- Note that the attributes are case-insensitive! -->

    <!-- When the mouse cursor comes on top of the link, an alert
    box is displayed. This can be annoying!-->

    <br />

    <!-- on mouse out even handler! -->

    <a href="http://google.com" onmouseout="alert('Going to Google!');"> Click to go to Google! </a>

    <!-- When the mouse cursor moves to the link, and then leaves
    away, an alert box pops up! This can be annoying!-->

</body>
```

## Objects in JavaScript

```HTML

<body>

    <!-- Object is a peculiar datatype which has a few properties and methods associated with it!

    Eg: Book

    A book has various properties that can be quantified:
    * Title
    * No. of Pages
    * Price
    * Topic
    * Publisher
    * Authors

    A book has several functions or methods that can be done:
    * Reading
    * Pillow?!
    * Get a degree
    * Teach a class

    These properties are like variables. These functions that are
    done by and using the object and it's properties are methods!

    Usage:

    object.method();
    object.variable;
    -->

    <script type="text/javascript">

        var t = "hey there!";
        // t itself is an object!
        document.write(t.length+"<br />"); // This is a property of t!
        document.write("Hey!");   // This is a "method" of the object "document"!
    </script>

</body>

```

## Creating Objects Using Constructor Functions

There are different methods! This is one long way!

```HTML

<head>

    <title>Object Creation!</title>

    <!-- To make an object, create a constructor function in the head tag.-->

    <script type="text/javascript">

        // This is a constructor function. This function is 
        // a blueprint of what an object has! This function
        // assigns values to objects.
        function person(name, age)
        {
            this.name = name;
            this.age = age;
            // This is a syntax for passing object details
        }

        // Creating an object or creating a new instance of an object!
        /* Syntax:
            var object_name = new object_constructor_function(values); */
        var obj1 = new person("Arun Prasaad", 24);
        var obj2 = new person("ChetanKumar", 23);

    </script>

</head>

<body>

    <script type="text/javascript">
        document.write(obj1.name);
        // Using an object variable or property!
    </script>

</body>

```

## Object Creation Using Object Initializers

```HTML
<head>

    <title>Object Initializers!</title>

    <!-- This is a faster way to create an object -->
    <!-- Used for creating just one or more objects -->
    <!-- Constructor function is for creating multiple objects! -->

    <script type="text/javascript">
        /* To create an object, use the following syntax 
        Syntax:
        obj_name = {var1 : value1, var2 : value2, ...};
        */
        Arun = {name:"Arun Prasaad", age:24};
        Chetan = {name:"ChetanKumar", age:23};
    </script>

</head>

<body>

    <script type="text/javascript">
        document.write(Arun.name + " of age " + Arun.age + " plus a few days and " + Chetan.name + " of age " + Chetan.age + " plus 10 months are friends! <br />" );
    </script>

</body>
```

## Adding Methods into Objects

```HTML

<head>

    <title>Adding Object Methods</title>

    <script type="text/javascript">

        // let's create a constructor function first!
        function people(name, age)
        {
            this.name = name;
            this.age = age;
            this.age_after_phd_end = age_after_phd;
            // This way, the method is plugged into the object.
            // You need not need the () !
            // age_after_phd_end is the name of the method age_after_phd inside the object!
        }

        // This is a method for the object to be plugged into it!
        function age_after_phd()
        {
            var phd_years = 3;
            var age = phd_years + this.age;
            // Here, "this" means the object into which the function/method is plugged into.
            return age;
        }
        // An object is also ready!
        var Arun = new people("Arun Prasaad", 24);

    </script>

</head>

<body>

    <script type="text/javascript">

        document.write(Arun.age_after_phd_end());

    </script>

</body>

```

## Arrays in JavaScript

```HTML

<body>

    <script type="text/javascript">

        /* This is how you create a 1D array */
        /* Index starts from 0 */
        var names = new Array ("Arun", "Chetan", "Dipankar", "Senthil", "Gowtham", "Keethi", "Kevin");

        /* This is another way! */
        var name1 = new Array(4);
        // Here, the array has 4 values!
        // To assign the values, use as follows.
        name1[0] = "JRR Tolkien";
        name1[1] = "GRR Martin";
        name1[2] = "JK Rowling";
        name1[3] = "Sidney Sheldon";

        // This is another way of making arrays - This is dynamic!
        var books = new Array();
        // Now, this array "books" is dynamic!

        // To assign the values, use them this way!
        books[0] = "Lord of the Rings";
        books[1] = "A Song of Ice and Fire";
        books[2] = "Harry Potter Series";
        books[3] = "Crime/Murder/Suspense/Thriller";

        // To access any indivual value!
        document.write(names[3]);

        // To print all values
        document.write(names);

        // Some Array Properties and Methods!
        document.write(name1.length); // length of the array

        var new_array1 = name1 + books; // Merges Array Elements
        // May have a small difference!
        var new_array2 = name1.concat(books);
        // Concatenation of 2 arrays

        document.write("<br />"+new_array1);
        document.write("<br />"+new_array2);
        
        var names = new Array ("Arun", "Chetan", "Dipankar", "Senthil", "Gowtham", "Keethi", "Kevin");

        var string1 = names.join();
        // Joins all strings, with commas in between
        var string2 = names.join(" - ");
        // Joins all strings, with hypen in between

        document.write(string1 + "<br />");
        document.write(string2 + "<br />");

        var string3 = names.pop();
        // Removes the last element in names array and saves it inside string3

        document.write(names + "<br />");
        document.write(string3 + "<br />");
        
        // To add the element back, use push method
        names.push("Kevin");

        // Reverses the elements in reverse index order
        names.reverse();

        document.write(names + "<br />");

        names.reverse();

        // This sorts out all the entries in the array!
        names.sort();

        document.write(names + "<br />");
            
    </script>

</body>
```

## Multi-Dimensional Arrays


Creating multi-dimensional arrays is easy!

Source : [stackoverflow question](http://stackoverflow.com/questions/966225/how-can-i-create-a-two-dimensional-array-in-javascript)

```HTML
<script type="text/javascript">
    var items = [[1,2],[3,4],[5,6]]; // Static Array
    alert(items[0][0]); // 1
    
    var xx = [[]]; xx[0][1] = 5; // Dynamic Array
    
    var x = new Array(10);
    for (var i = 0; i < 10; i++)
    {
      x[i] = new Array(20);
    }
    x[5][12] = 3.0; // Creating a 2D array
    
    // In a similar manner, you can extend it to a 3D, 4D array!
    
</script>
```

## Getting User Input using prompt feature and entering data for 2D arrays

```HTML

<script type="text/javascript">

    // Opens a pop-up box with a prompt to enter data
    var pie = prompt("Enter a value for Pie!");
    document.write("The value of Pie is : "+pie+"<br />");

    // Defining a 2D Array!
    // Defining the number of rows and columns!
    var r = 3, c = 2;
    // Making an array with r elements
    var array1 = new Array(r);

    // Making each of the r elements as arrays with c elements
    for(i=0; i<r; i++)
    {
        array1[i] = new Array(c);
    }

    // Essentially, array1 is a r time c 2D array or a matrix!
    // Using Prompt option to get each and every array entry value!

    for(i=0; i<r; i++)
    {
        for(j=0; j<c; j++)
        {
            array1[i][j] = prompt("Enter the value for array1["+(i+1)+"]["+(j+1)+"]:");
        }
    }
    
    // Printing the entire array!
    document.write("<br /> The Array entered is : <br />");
    
    // Printing the entire array in proper format!
    document.write(array1+"<br />");

    for(i=0; i<r; i++)
    {
        for(j=0; j<c; j++)
        {
            document.write(array1[i][j]+"  ");
        }
        document.write("<br />");
    }

</script>

```

## Associative Arrays

```HTML
<script type="text/javascript">

    // These associative arrays are similar to
    // Dictionaries in Python!

    var asso = new Array();
    asso["one"]=1;
    asso["two"]=2;

    document.write(asso["one"]);

</script>
```

The output is

```
    1
```

## Mathematical Object

JavaScript has a lot of mathematical constants and functions.

```HTML
<script type="text/javascript">

    var n = prompt("Enter a number", "");
    // This will prompt the user for a number.
    // The default value is nothing, set by ""

    // Has a lot of constants and in-built functions!
    // Pi
    document.write(Math.PI+"<br />");
    // e
    document.write(Math.E+"<br />");
    // Square root
    var sqrt_n = Math.sqrt(n);
    alert("The Square Root of " + n + " is " + sqrt_n);
</script>
```

## Date and Time Objects

JavaScript has in-built modules to get the date and time.

```HTML

<body>

    <!-- This tag acts as a place holder for the time to be displayed! -->

    <!-- id name is used to address this element -->
    <div id="time"> </div>

    <script type="text/javascript">

        // Some simple function
        function print()
        {
            document.write("Hello!");
        }

        // This function will execute the print function continuously after every 2000 milliseconds or 2 seconds.
        // setInterval("print()", 2000);

        function print_time_date()
        {
            var now = new Date();       // Grabs the date
            var hours = now.getHours();  // Grabs the hour in 24-hr
            var mins = now.getMinutes(); // Grabs the minutes
            var secs = now.getSeconds(); // Grabs the seconds

            document.getElementById("time").innerHTML=hours+":"+mins+":"+secs;

            /* 
                This big command
                * Searches the entire document,
                * Finds the element with the ID namely, "time",
                * And, inside the ID, it will display the time
                in the prescribed format.
            */
        }

        // This function will execute the print_time_date function continuously after every 1000 milliseconds or 1 second(s).
        setInterval("print_time_date()", 1000);

    </script>

      <!-- Start of example
         <script>
           var myDate         = new Date();               // returns the date object
           var myMonth        = myDate.getMonth();        // 0 through 11
           var myDay          = myDate.getDate();         // 1 through 31
           var myDayOfWeek    = myDate.getDay();          // 0 through 6 -  0 = Sunday
           var myYear         = myDate.getFullYear();     // 4 digit year
           var myHour         = myDate.getHours();        // 0 through 23
           var myMinutes      = myDate.getMinutes();      // 0 through 59
           var mySeconds      = myDate.getSeconds();      // 0 through 59
           var myMillSec      = myDate.getMilliseconds(); // 0 through 999
           var months  = new Array("January",   "February", "March",    "April",
                                    "May",       "June",     "July",     "August",
                                  "September", "October",  "November", "December");
           var days    = new Array("Sunday",   "Monday", "Tuesday","Wednesday",
                                   "Thursday", "Friday", "Saturday");
         </script>

         <p><mark> var myDate = new Date();</mark></p>
         <p><mark> var myMillSec = myDate.getMilliseconds();</mark></p>
         <script>
            document.write("<p>The date is <mark> ", myDate, " </mark></p>");
            document.write("<p>The Milli seconds is <mark> ", myMillSec, "</mark></p>");
         </script>

         <p><mark>The getMilliseconds() method returns 0 to 999. </mark></p>

        End of example -->

</body>
    
```

## Form Validation

```HTML

<head>

    <title> Forms and JavaScript! </title>

    <script type="text/javascript">
        function validator()
        {
            if(document.sample.box.checked) // True of box is checked
            {
                alert("Yes Checked!");
            }
            else
            {
                alert("Check the box!");
            }
        }
    </script>

</head>

<body>

    <!-- A Sample Form! -->
    <form name="sample">
        Username: <input type="text" name="uname" />
        <br/>
        Password: <input type="password" name="pword" />
        <br/>
        Want colour(s)? : <input type="checkbox" name="box"/>
        <br/>
        <input type="button" value="Check!" onClick="validator()"/>
        <!-- On clicking the button, the validator function is invoked! -->
        <input type="submit" value="Submit" />
    </form>

    <script type="text/javascript">

        // JavaScripts automatically creates a form array, if a 
        // form field is present! First form will be form 0, next
        // is form 1, form 2 etc.,

        var x = document.forms[0].length;
        // This will access the first form!
        // length is the number of inputs in the form, here it is 3.
        // x = 3
        var y = document.forms[0].elements[0].name; // Accessess uname!
        var z = document.forms[0].elements[1].name; // Accessess pword!

        // Using Form name
        var a = document.sample.uname.name; // Accessess uname!
        var b = document.sample.pword.name; // Accessess pword!

        // document.write(x+" "+y+" "+z+"<br/>");
        // document.write(a+" "+b+"<br/>");

    </script>

</body>

```
