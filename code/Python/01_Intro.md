# Introduction to Python

Python is a programming language written by Dutch Programmer Guido van Rossum. Python as of 2019, is one of the most commonly used programming languages, having its reach expanded to a variety of fields.

Learning Python can be quite useful for a variety of purposes. So, it is quite recommended.

<!-- TOC -->

- [Introduction to Python](#Introduction-to-Python)
  - [Features of Python](#Features-of-Python)
    - [It is an Interpreted Programming Language.](#It-is-an-Interpreted-Programming-Language)
    - [It is a general purpose programming language](#It-is-a-general-purpose-programming-language)
    - [It is object oriented](#It-is-object-oriented)
    - [The design of the language is simple](#The-design-of-the-language-is-simple)
  - [Why Python?](#Why-Python)
  - [Is it undisputed?](#Is-it-undisputed)
  - [Different Versions of Python](#Different-Versions-of-Python)
    - [Python 2](#Python-2)
    - [Python 3](#Python-3)

<!-- /TOC -->

## Features of Python

Python programming language has a lot of features that make in versatile.

### It is an Interpreted Programming Language.
What this means is that each and every line of code written by the programmer is interpreted into its corresponding machine or assembly level programming immediately and executed immediately. The advantage of this kind of architecture is that the programmer can see if his/her code is working well on a line-by-line basis and execute each and every line on their own. So, this architecture is user-friendly to work with. However, this method is inefficient when it comes to using resources. Hence, the speed of execution is quite slow, often taking anywhere between 2-200+ times the speed of a code written in a compiled programming language like C or C++ for the same purpose. However, one of the pragmatic reasons such interpreted languages exist is because such languages are easier to learn and get things done on the fly. In comparison to compiled programming languages, the development time to generate a program for some purposes is quite small. So in a trade-off between Development time versus Execution time, if Execution time is not a big bother, speed is not a major requirement, and the freedom to run commands on the fly is more important, then in such places, Python and other interpreted programming languages are the clear winner. Learning programming using python or interpreted programming language is a gentler way to introduce people into programming by concentrating on the end goal without worrying about the specifics.

Just for an example, look at the simple ``hello, world`` program looks like in ``Java`` -  a compiled programming language vs ``Python`` - an interpreted programming language. The simplicity you see with Python is quite evident. Granted, this is a simple program and it might look like this example is nitpicked. However, when a programmer tries to write a program in a compiled programming language versus any other interpreted language, the latter one will usually look simpler and easy to read.

```java
/* This is a simple "Hello, world" program written in Java. */
class hello 
{ 
    public static void main(String args[]) 
    { 
        System.out.println("Hello, World"); 
    } 
} 
```

```python
# This is a simple "Hello, world" program written in Python
print("Hello, world")
```

In contrast to this, we have compiled programming languages like C, C++, Java etc., in which the entire program gets converted into machine or assembly level programming at the end and executed together. This makes compiled programming languages fast and quite efficient. However, the architecture is not user-friendly. You don't have the freedom to run each and every line one-by-one. So, this makes the programming difficult for the programmer. For the purpose of speed and efficiency, compiled programming languages take the cake by a land-slide. If execution time has to be as small as possible, and programming resources such as availability of processors, memory are of vital importance, then in these situations the compiled programming languages win. These reasons enable them to be used as the foundations of interpreted programming languages and even the architectures of operating systems. Due to the complexities involved, learning programming using such compiled programming languages is a harder way to introduce people to learn programming languages by enforcing the need for good programming practices and systematic thinking.

### It is a general purpose programming language

What this means is that the programming language can be used for a variety of purposes. Most programming languages can be used only for one or two applications. For instance, C, C++, are used for making OS and software. They are also used for scientific computation.

Python is developed in such a manner that it can be used for any sort of programming. It can be used as a teaching tool, as a programming language for scientific computation, for web development, for making software, for making websites, etc., With time, the number of applications for the language will keep on increasing.

Infact, the creator of Python, Guido van Rossum intended and created Python for the same reason: to be able to be used by anyone for any purpose.

### It is object oriented

What this means is that the entire language is built on the concept of objects. In the context of a programming language, an object is an entity that has some data or information with it along with some procedures that work on these data. These data are often known as ``attributes`` and these procedures that work on these ``attributes`` is often known as ``methods``.

This feature can be quite difficult to comprehend for a beginner if not explained correctly. However, in the long run, for a user who is looking for better ways to handle data and make easier procedures, such ``objects`` in the language prove quite useful.

As of now, the context is not well-established here to explain what ``objects`` fully mean. It will be established and explained quite well and in-detail in the subsequent pages.

### The design of the language is simple

The core philosophy of python is to make the programming experience simple for anyone who uses it. To summarize the philosophy behind the language in the best possible way, the Python Enhancement Proposal 20 - shortly known as [PEP-20](https://www.python.org/dev/peps/pep-0020/) has a set of 19 instructions listed down in the document - [_The Zen of Python_](https://www.python.org/dev/peps/pep-0020/). To access this set of instructions, all one has to do is type the command: 

```python
import this
```
... in the terminal to get the instructions as shown.
```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

## Why Python?

If you were to ask me "why should I learn Python when there are many many languages out there?" - I'll simply list-out the following details.

* Simple to use,
* Free and Open Source,
* High Level Programming Language,
* Fast to learn and implement,
* Interoperatability with the linux and unix operating systems,
* Interoperatability with other programming languages,
* Used for General Purpose Programming, Software Development, GUI, Web Design, Scientific Computation, OS etc.,

## Is it undisputed?

By telling all the good parts of the language, It might seem that Python is an undisputed language triumphing over other languages. 

To answer the question, No! Python has its own fair share of advantages and disadvantages. Infact, every language has it's ups and downs. Python is not a perfect programming language.

## Different Versions of Python



### Python 2

* Old version of Python
* Legacy Codes built on it
* No new version anymore
* Library Migration going on

### Python 3

* Newer version of Python
* The future of Python
* Revamped internal architecture - supports future technological implementations
* (Almost all) libraries are translated

We are in the **transition** period. In the future, Python 2 will be obsolete.
