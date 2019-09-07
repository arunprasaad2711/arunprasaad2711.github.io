# LaTeX

<!-- TOC -->

- [LaTeX](#latex)
  - [Symbols:](#symbols)
  - [Parenthesis:](#parenthesis)
  - [Document Basics, Environment Commands, Document Classes](#document-basics-environment-commands-document-classes)
  - [Document Sections and Subsections](#document-sections-and-subsections)
  - [Mathematical Notations](#mathematical-notations)
    - [Subscripts and Superscripts:](#subscripts-and-superscripts)
  - [Mathematical Notations](#mathematical-notations-1)
    - [Subscripts and Super-Scripts](#subscripts-and-super-scripts)
    - [Greek Symbols](#greek-symbols)
    - [Functions](#functions)
      - [Square root and Root](#square-root-and-root)
      - [Logarithms](#logarithms)
      - [Trigonometry](#trigonometry)
      - [Fractions and Brackets](#fractions-and-brackets)
      - [Other Symbols](#other-symbols)
  - [Array of Equations](#array-of-equations)
  - [Equation Arrays](#equation-arrays)
  - [Letter Writing](#letter-writing)
  - [Letter Writing](#letter-writing-1)
  - [Tables](#tables)
    - [Table Command](#table-command)
  - [Tables, Labels, Captions](#tables-labels-captions)
  - [Text and Page Formatting](#text-and-page-formatting)
  - [Arrays and Tabbing](#arrays-and-tabbing)
    - [Arrays:](#arrays)
    - [Tabbing:](#tabbing)
    - [Creating Matrix](#creating-matrix)
  - [Figures](#figures)

<!-- /TOC -->
 
**Document Sections:**
 
To create a section in the document is easy.

```latex
use \section{section name}  to create a section in the document.
use \subsection{}  to create a sub section
use \subsubsection{}  to create a sub sub section
```

Apparently, only 3 levels of hierarchy are allowed. Chapters are also allowed. That is a different category.

The sizes of these sections are decreasing in size. All these sections are in bold.

Multiple number of sections are allowed. They get automatically numbered.
 
using these sections is necessary for making the table of contents. They get numbered accordingly, based on the document type and their position within the document.

## Symbols:

Symbols in LaTeX are pre-assigned. So, you cannot use them directly.

Use backslash symbol to type the characters.

eg: ``\$ \% \& ``

## Parenthesis:

Circular/Round brackets do not have any meaning. ``()``. Square brackets have meaning in commands, but they can stand alone. ``[]``.

But! flower/curly brackets are reserved. You cannot print them directly! ``{}``
To print them, use backslash `` \{ \}. ``

In commands, ``[]`` are used for filling optional arguments/instructions, whereas ``\{\}`` brackets are used for filling the command name.

use package commands are used for including special packages into the file (they add more features to the document)

## Document Basics, Environment Commands, Document Classes

```latex

\begin{document}
\maketitle

Documents are of many types, and they are defined by the class files. So, the default class is article.

Other documents are reports, chapters, letters, beamer, papers, proposals, etc.,

You have facility to create your own document class using the class files having the extension .cls

The default standard fonts in LaTeX are 10, 11, 12. However, short-range increase/decrease of fonts is possible.

The user details are: author name, date, title, sub-title, institution, logo etc.,

All of these come under the make title command. All these fields are not available for all class files. They vary for different class files.

Commands and Environment commands:
Commands in LaTeX start with the backslash symbol. eg: today, maketitle, makeindex etc.,

Environment commands start with backslash just like normal commands, but they occur in pairs. Environment commands create a region of special formats or special features within the document. They start with a begin and end with an end.
eg: begin document - end document, 

\end{document}
```

## Document Sections and Subsections

```latex
\begin{document}

\maketitle

\tableofcontents

\newpage

\section{Para1}
Hello everyone! LaTeX was made/created by Leslie Lamport! \\

Hello everyone! LaTeX was made/created by Leslie Lamport! \\

\subsection{Para1:2}

Hello everyone! LaTeX was made/created by Leslie Lamport! \\

Hello everyone! LaTeX was made/created by Leslie Lamport! \\

Hello everyone! LaTeX was made/created by Leslie Lamport! \\

Hello everyone! LaTeX was made/created by Leslie Lamport! \\

Hello everyone! LaTeX was made/created by Leslie Lamport! \\

Hello everyone! LaTeX was made/created by Leslie Lamport! \\

Hello everyone! LaTeX was made/created by Leslie Lamport! \\

Hello everyone! LaTeX was made/created by Leslie Lamport! \\

\section{Para2}
I am in the second paragraph! \\

\section{Para3}
Hello everyone! LaTeX was made/created by Leslie Lamport! \\

Hello everyone! LaTeX was made/created by Leslie Lamport! \\

Hello everyone! LaTeX was made/created by Leslie Lamport! \\

\subsection{para3:1}
Hello everyone! LaTeX was made/created by Leslie Lamport! 

\subsubsection{para3:1:1} 
 
I am using TeXmaker for writing this document!\\

\section{Para4}
Hello everyone! LaTeX was made/created by Leslie Lamport!\\

\section{Para5}
Hello everyone! LaTeX was made/created by Leslie Lamport! \\
\end{document}
```

## Mathematical Notations

### Subscripts and Superscripts:
 
This section includes how to use subscripts and superscripts.

**Superscripts:**

start the maths mode, (inline or display)

```latex
x^4 will type it in proper mode.
x^45 will type x^4 properly and 5 in the same line and size of x.
To avoid that, use {}
x^{45} will type it in proper mode.
```
 
Chain superscripts are possible. For that, the {} are to be used properly. Otherwise, it is not a big deal.
Noticed upto 3 levels. May be more.
 
**Subscripts:**
 
start the maths mode, (inline or display)

```latex
x_4 will type it in proper mode.
x_45 will type x subscript 4 properly and 5 in the same line and size of x.
To avoid that, use {}
x_{45} will type it in proper mode.
```
 
these are more {} sensitive than superscripts.

Chain subscripts are possible. For that, the {} are to be used properly. Otherwise, it is not a big deal.
Noticed upto 3 levels. May be more.
 
To include both subscripts and superscripts, use the above rules together and with proper use of {},^ and _
 
**Greek Letters:**
 
To type Greek letters,
 
go into maths mode (inline or display)

type \ followed by a simplified equivalent English pronunciation word for the letters.

```latex
eg: \pi for the Greek letter pi
 
\alpha
\beta
\gamma
\omega and so on.
```
 
if you do not know the proper one, you can always check it out in the insert symbols options.
 
After typing a Greek letter, leave a space. Or else, all the letters along with it will be taken as a big command.

```latex
eg: $A = \pi r^2$
```
$A = \pi r^2$

**Functions:**
 
For trigonometric functions,
 
type ``\`` followed by the function name in English (exactly or equivalently depending on the case)

```latex
eg \cos{} for the cosine function, \cosh{} for hyperbolic cosine. similar methods exist for other functions and inverse functions.
```

**For log functions**:

```latex
type \log{} for base 10 log function without 10 at the base
type \ln{} for natural log function without e at the base
type \log_{sub}{} for base sub log function with subscript eg: log base 3 or log base 4.5 etc.,
```

**for square roots and other roots,**

```latex
type \sqrt{} for regular square roots
type \sqrt[root]{} for other roots. eg: cube root, 4.5th root, etc.,
```

chain functions are possible. Use ``{}`` and endings properly.
 
similarly, definitions exists for other functions.
 
**Fractions:**
 
To type a fraction,
 
go to maths mode,

use ``\frac{Nr}{Dr}``
 
if used in the in-line maths mode, the fraction will look smaller in font.

to avoid that, wrap the fraction within display style command.

```latex
eg: \displaystyle{\frac{Nr}{Dr}}
```

$$\displaystyle{\frac{Nr}{Dr}}$$
 
chain fractions are possible. Also, commands and fractions nesting is also possible.

space between two lines intentionally made in the script will give line break in the document.

use tab for jumping between ``{}`` from left to right.

use space between functions as you type them when you write a nested function statement.

This space will not appear in the preview. this will ensure readability of the code.
 
eg:

to type fractions:

```latex
$\frac{numerator}{denominator}$
```
eg:

``$\frac{2}{3}$`` for 2/3 in fraction representation. this shrinks the fraction size to fit in-line

$$\frac{2}{3}$$
 
``$\displaystyle{\frac{2}{3}}$`` will print the fraction to the original size.

$$\displaystyle{\frac{2}{3}}$$

``$\frac{x}{x^2+2x+1}$`` 

$$\frac{x}{x^2+2x+1}$$

``$\frac{x}{\sqrt{x^2+2x+1}}$``

$$\frac{x}{\sqrt{x^2+2x+1}}$$
 
fraction within a fraction

``$\frac{\frac{2}{3}}{\frac{5}{6}}$`` will print (2/3)/(5/6) in proper format

$$\frac{\frac{2}{3}}{\frac{5}{6}}$$
 
``\displaystyle{content}`` will print the entire content without size shrinking in a single line.
 
Symbols and Brackets:
 
(), [] are non-reserved brackets. so they can be used inside maths mode and inside text without any alterations.
 
{} are reserved brackets. they can be used only with commands, especially for coding.

to use them without commands, use \{ and \}
 
similarly, $ is a reserved symbol.

To use it elsewhere, use \$

```latex
$$3(\frac{2}{5})$$ will display 3*(2/5) with the () brackets being short.
```

to extend them, or enlarge them use \left and \right command in pairs

```latex
eg: $$3\left(\frac{2}{5}\right)$$
```
$$3\left(\frac{2}{5}\right)$$

applies for [] as well. when using {}, you need to put them as \{ or \}

```latex
eg: $\left\{25\right\}$
```

$\left\{25\right\}$
 
\left and \right always should occur in pairs. you can change the brackets between \left and \right.

if you do not want a bracket in the left or right, use a dot or period

```latex
eg: \left. or \right.
```

\left and \right can be used for enveloping other symbols as well, for instance the | symbol

```latex
$$3(1+[23])$$ will print 3(1+[23]).
```

except for curly brackets{}, inserting other brackets is not a problem and it is direct.
 
{} are reserved symbols in LaTeX options so,

```latex
${a,b,c}$ will print a,b,c alone without the brackets.

to solve this, use the backslash operator as follows,
$\{a,b,c\}$ will print {a,b,c} with brackets.
```

similarly \$ symbol is a reserved in LaTeX so, to print a dollar symbol in LaTeX, use the \$ notation.

```latex
$3(\frac{2}{4})$ will print 3(2/4) but () brackets will be short and will not be printed to the size of the fraction.
 
to rectify this, use left and right functions as below
$3\left(\frac{2}{4}\right)$ will print 3(2/4) but the () brackets will grow large enough to cover the fraction.
this function is available for [] brackets as well.
```
 
for {} brackets, just as above, but use \ symbol as shown below
```latex
$3\left\{\frac{2}{4}\right\}$
```

$$3\left\{\frac{2}{4}\right\}$$
 
this methodology works for all symbols as it is. LaTeX treats all symbols and brackets (except{}) alike

```latex
$|\frac{x}{x+1}|$ will print x/x+1 in proper notation within absolute symbol, but the size of the absolute symbol will be short and will not cover the fraction.
```

use the same left and right function as with brackets to grow the symbol.
 
left and right functions work as a pair, meaning, if left is present, then right has to be present,
 
suppose you don't want a bracket or a symbol that grows to fit the fraction either in the left or right, use the period (.) symbol to avoid it.

eg:

```latex
$$\left\{x^2\right\}$$ will print {x^2} in proper notation.
$$\left\{x^2\right.$$ will print {x^2 in proper notation. It will ignore the need for }
$$\left.\frac{dy}{dx}\right|_x=0$$ will print dy/dx in full fraction with | fully covering the derivative on the right with x=0 at the subscript in proper notation.
```

$$\left\{x^2\right\}$$

$$\left\{x^2\right.$$

$$\left.\frac{dy}{dx}\right|_x=0$$
 
on the same note, if you want one side of the brackets to be of the different bracket, then again it is possible. try this out!

note that the commands must be executed in pair but the arguments or symbols they take need not be the same.
 
**Other symbols**

```latex
\pm symbol is used for plus or minus symbol

\approx is used for approximately equal symbol

\ne \ge \le is for not equal to, greater than or equal to, less than or equal to signs

\gg \ll is for greater, greater than and lesser, lesser than signs

\rightarrow \leftarrow \leftrightarrow are for arrow symbols

\times is for the large multiplication symbol

\LaTeX is for the LaTeX symbol

\cdots, \rdots, \ldots symbols for 3 continuous dots oriented in the centre, right and left.

Similarly there are \vdots and \ddots for vertical 3 dots and diagonal 3 dots

\infty for infinity symbol

\sum \prod for summation and product symbols

\int for integral symbol

\bynsca for 3 symbols of creative common license. Needs cclicense package to print them

```
 
**Special Mathematical Symbols:**

Include package mathrsfs and use \mathcal{character name} for getting the stylish/curly character symbols as in Laplace/Fourier Transforms.
 
A list of important symbols:
http://oeis.org/wiki/List_of_LaTeX_mathematical_symbols
 
This source is from wiki.

## Mathematical Notations

```latex
The heron's formulae for the area of a triangle is given by $A = \sqrt{s(s-a)(s-b)(s-c)} $
```
$A = \sqrt{s(s-a)(s-b)(s-c)} $

```latex
For a quadratic equation, $ax^2 + bx + c = 0$, the solution of x is given by the notation: $$ x = \frac{-b \pm \sqrt{b^2 -4ac}}{2a}$$
```
For a quadratic equation, $ax^2 + bx + c = 0$, the solution of x is given by the notation: $$ x = \frac{-b \pm \sqrt{b^2 -4ac}}{2a}$$

### Subscripts and Super-Scripts

The algebraic identities are very vital for evaluating arithmetic operations.

```latex
$$ (a+b)^2 = a^2 + 2ab + b^2 $$
$$ (a+b)^3 = a^3 + 3a^2b + 3ab^2 + b^3$$
```

$$ (a+b)^2 = a^2 + 2ab + b^2 $$
$$ (a+b)^3 = a^3 + 3a^2b + 3ab^2 + b^3$$

Taylor series expansion
```latex
$$ (1-x)^{-1} = 1 + x + x^2 + x^3 + x^4 + .... $$
```
$$ (1-x)^{-1} = 1 + x + x^2 + x^3 + x^4 + .... $$

```latex
$U^{235}_{92}$ is radio active and naturally unstable!
```
$U^{235}_{92}$ is radio active and naturally unstable!

```latex
$$ U^{35^{-45}}_{{45}_{-35}}$$
```
$$ U^{35^{-45}}_{{45}_{-35}}$$

The FTBS FD scheme for Linear Advection equation is given as:
```latex
$$ u_{i+1,j} = u_{i,j} - \frac{c\Delta t}{\Delta x}[u_{i,j}-u_{i,j-1}]$$
```

$$ u_{i+1,j} = u_{i,j} - \frac{c\Delta t}{\Delta x}[u_{i,j}-u_{i,j-1}]$$

### Greek Symbols

```latex
$\alpha\ \beta\ \ \ \ \ \ \gamma\ \delta\ \Delta\ \Gamma$
```
$\alpha\ \beta\ \ \ \ \ \ \gamma\ \delta\ \Delta\ \Gamma$

The area of a circle is:

```latex
$$ A = \pi r^2$$

$\Pi$
```
$$ A = \pi r^2$$

$\Pi$

### Functions

#### Square root and Root

```latex
$$\Delta = \sqrt{b^2 -4ac}$$
$$ a = \sqrt[0.5]{b}$$
```

$$\Delta = \sqrt{b^2 -4ac}$$
$$ a = \sqrt[0.5]{b}$$

#### Logarithms
Base 10 log without 10 at the base
```latex
$$ \log{b} $$
```
$$ \log{b} $$

Natural Logarithm
```latex
$$ \ln{b} $$
```

$$ \ln{b} $$

Non-standard logarithm
```latex
$$ \log_{8}{64} = 2 $$
```

$$ \log_{8}{64} = 2 $$

#### Trigonometry

Sine function

```latex
$ sin(A+B) = sin(A)cos(B) + cos(A)sin(B)$

$ \sin(A+B) = \sin(A)\cos(B) + \cos(A)\sin(B)$

$ \sin{A+B} = \sin{A}\cos{B} + \cos{A}\sin{B}$

$\cosh^2(A)$
```

$ sin(A+B) = sin(A)cos(B) + cos(A)sin(B)$

$ \sin(A+B) = \sin(A)\cos(B) + \cos(A)\sin(B)$

$ \sin{A+B} = \sin{A}\cos{B} + \cos{A}\sin{B}$

$\cosh^2(A)$

#### Fractions and Brackets

```latex
$\frac{4}{5}$ means, you take 4 parts of something after it is divided into 5 equal parts.
```

$\frac45$

```latex
$\displaystyle{\frac{4}{5}}$ means, you take 4 parts of something after it is divided into 5 equal parts.
```
$\displaystyle{\frac{4}{5}}$


The FTBS FD scheme for Linear Advection equation is given as:

```latex
$$ u_{i+1,j} = u_{i,j} - \left[\frac{c\Delta t}{\Delta x}\right][u_{i,j}-u_{i,j-1}]$$

$$ \left( \frac{c\Delta t}{\Delta x} \right)$$

$$ \left[ \frac{c\Delta t}{\Delta x} \right)$$

$$ \left( \frac{c\Delta t}{\Delta x} \right]$$

$$ \left. \frac{c\Delta t}{\Delta x} \right\rangle$$
```

$$ u_{i+1,j} = u_{i,j} - \left[\frac{c\Delta t}{\Delta x}\right][u_{i,j}-u_{i,j-1}]$$

$$ \left( \frac{c\Delta t}{\Delta x} \right)$$

$$ \left[ \frac{c\Delta t}{\Delta x} \right)$$

$$ \left( \frac{c\Delta t}{\Delta x} \right]$$

$$ \left. \frac{c\Delta t}{\Delta x} \right\rangle$$

The definition of a derivative:

```latex
$$ \left.\frac{dy}{dx}\right|_{x\rightarrow 0} = \frac{f(y+dy)-f(y)}{dx}$$
```

$$ \left.\frac{dy}{dx}\right|_{x\rightarrow 0} = \frac{f(y+dy)-f(y)}{dx}$$

#### Other Symbols

```latex
$ \pm \ \approx \ \ne \ \ge \ \le $

$ \cdots \ \ldots \ \vdots \ \ddots $
```

$ \pm \ \approx \ \ne \ \ge \ \le $

$ \cdots \ \ldots \ \vdots \ \ddots $

## Array of Equations

Equation Arrays using eqnarray

To type a set of equations with equation numbers, the command use is eqnarray

```latex 
\begin{eqnarray}
equation 1 \\ equation 2 \\ .....
\end{eqnarray}
```
 
this set of equations need not need the \$\$ sign. Once typed, it will generate the equation number automatically. To avoid numbers, use ``` \nonumber ``` command before \\

this will not align the equations with centre justification or having the equal signs in the exact middle. 

for that, use & before and after the equal sign
 
example

```latex
\begin{eqnarray*}
5x^2 + 3x &=& 7y^2 + 5y \\
3x &=& 5 \\
x^2 &\approx& \pm \sqrt{3}
\end{eqnarray*}
```
 
this will print the 3 equations in proper format without equation numbers. the asterisk sign in eqnarray avoids the equation numbers. remove them to include eqn numbers.
 
**Equation Arrays using align**

This environment is used for writing equations  with equation numbers. This environment does not need dollar signs. The * prevents the equations being numbered. If removed, the equations will be numbered. Align environment cannot have blank lines. To include blank lines, put a % and leave the line empty

```latex
\begin{align*}
Equation 1 \\
Equation 2 ….
\end{align*}
```
 
To align the equations, put & infront of the equal sign.
 
If you have a very long equation, you can write it down in two or more lines using \\ command. For alignment, you can use & symbol. This will create multiple equation numbering. To avoid that, use the command \nonumber before the \\ command. If \left and \right symbols are used, then each line of equation needs a \left and \right command. Refer to the mathematical notations page for more details.
 
To introduce text in between the equations, use

\intertext{text you want to put. This text, if has maths terms, needs the dollar symbols. Display maths mode may not work here}

** No text can be written inside eqnarray or align. Even blank lines are not allowed. \intexttext command is possible only inside align environment field**
 
To refer to an equation, create a ``` \label{ref_name} ``` and use ``` \ref{ref_name} ``` to refer to it in the document.


## Equation Arrays

```latex
\begin{eqnarray}
x^2 + 2x + 1 &=& (x+1)^2\\
%
x^3 + 3x^2 + 3x + 1 &=& \nonumber \\
(x+1)^3
% Use & for manual alignment
% The output will have the first equation numbered
% The equations will be aligned properly!
\end{eqnarray}

$$ x^2 + 2x + 1 = (x+1)^2 $$

$$ x^3 + 3x^2 + 3x + 1 = (x+1)^3 $$

\begin{eqnarray}
x^2 + 2x + 1 &=& (x+1)^2 \\
%
x^3 + 3x^2 + 3x + 1 &=& \\
(x+1)^3
% The equation will not have numbers
% Proper alignment
% The second equation will be in 2 lines.
\end{eqnarray}

$$ x^2 + 2x + 1 = (x+1)^2 $$

$$ x^3 + 3x^2 + 3x + 1 = 
(x+1)^3 $$

\begin{eqnarray*}
x^2 + 2x + 1 = (x+1)^2\\
x^3 + 3x^2 + 3x +1 = \\
\left[(x+1)^3\right]\\
\left[-(x+1)^3\right]\\
\left[(x+1)^3\right]\\
\end{eqnarray*}

\begin{align}
x^2 + 2x + 1 = (x+1)^2  \\
x^3 + 3x^2 + 3x +1 = \nonumber \\
(x+1)^3\\
\intertext{This is a set of identities in algebra}
\end{align}

\begin{align*}
x^2 + 2x + 1 &=& (x+1)^2\\
x^3 + 3x^2 + 3x +1 &=& \\
(x+1)^3
\intertext{This is a set of identities in algebra}
\end{align*}

\begin{align}
x^2 + 2x + 1 = (x+1)^2\\
x^3 + 3x^2 + 3x +1 = \nonumber\\
\left[(x+1)^3
-(x+1)^3
(x+1)^3\right]\intertext{This is a set of identities in algebra}
\end{align}

```

\begin{eqnarray}
x^2 + 2x + 1 &=& (x+1)^2\\
%
x^3 + 3x^2 + 3x + 1 &=& \nonumber \\
(x+1)^3
% Use & for manual alignment
% The output will have the first equation numbered
% The equations will be aligned properly!
\end{eqnarray}

$$ x^2 + 2x + 1 = (x+1)^2 $$

$$ x^3 + 3x^2 + 3x + 1 = (x+1)^3 $$

\begin{eqnarray}
x^2 + 2x + 1 &=& (x+1)^2 \\
%
x^3 + 3x^2 + 3x + 1 &=& \\
(x+1)^3
% The equation will not have numbers
% Proper alignment
% The second equation will be in 2 lines.
\end{eqnarray}

$$ x^2 + 2x + 1 = (x+1)^2 $$

$$ x^3 + 3x^2 + 3x + 1 = 
(x+1)^3 $$

\begin{eqnarray*}
x^2 + 2x + 1 = (x+1)^2\\
x^3 + 3x^2 + 3x +1 = \\
\left[(x+1)^3\right]\\
\left[-(x+1)^3\right]\\
\left[(x+1)^3\right]\\
\end{eqnarray*}

\begin{align}
x^2 + 2x + 1 = (x+1)^2  \\
x^3 + 3x^2 + 3x +1 = \nonumber \\
(x+1)^3\\
\intertext{This is a set of identities in algebra}
\end{align}

\begin{align*}
x^2 + 2x + 1 &=& (x+1)^2\\
x^3 + 3x^2 + 3x +1 &=& \\
(x+1)^3
\intertext{This is a set of identities in algebra}
\end{align*}

\begin{align}
x^2 + 2x + 1 = (x+1)^2\\
x^3 + 3x^2 + 3x +1 = \nonumber\\
\left[(x+1)^3
-(x+1)^3
(x+1)^3\right]\intertext{This is a set of identities in algebra}
\end{align}


## Letter Writing

to start a letter file, use the following format

```latex
\documentclass{letter}
\address{all the contents of from address separated by \\ for line breaks}
\date{}
\signature{your name}
 
% All the above address and date are printed in the top right corner of the page. The signature comes below the body at the final greetings part.
% The contents below become left justified. Empty address is allowed.
 
\begin{document}
\begin{letter}
Address of the person referred to.
 
\opening{Dear sir, madam, sir, Hello...etc.,}
Contents of the letter
 
\closing{yours sincerely, etc.,}
\cc{}  % if any
\end{letter}
\end{document}

````

## Letter Writing

```latex

\documentclass[10pt, a4paper]{letter}

\usepackage[left=1in, right=1in, top=1in, bottom=1in]{geometry}

\signature{Arun Prasaad Gunasekaran}

\address{From: \\ Arun Prasaad Gunasekaran \\ Classified Address}

\date{31 August 2001, Bangalore}

\begin{document}

\begin{letter}{To: \\ John Doe \\ Unknown place \\ Unknown Street \\ City \\ Country}

\opening{Dear John Doe!}

\begin{center}
Subject : Want to meet you!
\end{center}

I want to know who you are! Are you a real person? Are you anonymous? Are you a product of fiction? Why are you so famous?

I want to meet you in person and have a chat!

If you get this letter, you know how to find me!

See you!

\closing{Yours Anonymously,}

\ps{PS: In case you are wondering, go to youtube and type my name! :p}

\encl{I have enclosed a few documents!}

\cc{To All youtube viewers} %Optional

\end{letter}

\end{document}

```
 For more detailed sources : 
 
* https://en.wikibooks.org/wiki/LaTeX/Letters 
* http://texblog.org/2007/08/15/writing-a-letter-in-latex/ 
* http://tex.stackexchange.com/questions/133836/writing-an-official-letter

## Tables

to begin a table, tabular command is used.

**Tabular Command**

```latex
\begin{tabular}{args}
 
\end{tabular}
```
 
to start a table, a format is as follows

```latex
\begin{tabular}{rlcrlc}
contents
\end{tabular}
```
 
tabular is the parameter for beginning a table. the {} after will decide how many columns to fit.

this table has 6 columns with

columns 1 and 4 right justified,

columns 2 and 5 left justified, and

columns 3 and 6 centre justified
 
to write the contents of the rows, type them naturally. the first content will go to row 1 column 1.

Use ampersand symbol & to swap columns from left to right.

eg:
```latex
12345 & 67890 will print 12345 in column 1 and 67890 in column 2.
use \\ at the end of one line to go to the next column. \\ will introduce a forced line break.
```
 
**note**: if the content in a page reaches its end and if you add one more content that intuitively be half placed in one page and half in the other, LaTeX will either force shrink the page contents to accommodate the contents or shift the contents to the next page automatically with proper formatting.
 
this table command will not print any lines as it is. to make lines and to explain a proper table, see the example

```latex
\begin{tabular}{|c|c|c|c|c|c|}
\hline
$x$ & 1 & 2 & 3 & 4 & 5\\ \hline
$f(x)$ & 1 & 4 & 9 & 16 & 25\\ \hline
\end{tabular}
```

This will put all the lines to form a simple table as you intuitively think of. \hline is for a horizontal line and | symbol in {} between letters is for the vertical line.
 
Multiple | lines can be placed. Also, multiple \hline can be placed.
 
If you want a blank entry, just leave a space between the & symbols. To merge cells, read the contents below,
 
**Merging cells:**
 
To merge cells along a row, use multi column command

```latex
\multicolumn{N}{A}{C}
N = number of columns in a particular row to be merged from the right to form a cell
A = cell content alignment with or without |
C = cell content
```
 
To merge cells along a row, use empty entries and centre line command.

```latex
\cline{n1-n2}
```

This will draw a line between the current row and the row below, only between columns n1 and n2.

** If n1 = n2, then the centre line will be drawn only for one cell**
 
To merge cells row and column wise, use the above methods in a combined manner properly.
 
### Table Command

 This command is used to treat the table generated in the tabular command to behave as a single independent object instead of a symbol.
 
This is the format:

```latex
\begin{table} % avoid this command in beamer class. Use tabular directly
\centering
\caption{name1} % caption is usually put on top of the table
\label{name2} % label should be below the caption as it is the one that creates the table number.
\begin{tabular}
Contents
\end{tabular}
\end{table}
```
 
\centering is for centre justifying the table, while the label is for referencing purpose. \caption{} is for the title of the table. These are optional, but if included, will be better.

## Tables, Labels, Captions

```latex

Table \ref{Tab1} has details of some houses in ASOIAF.

\begin{table}[h]
\centering
\caption{Details of Houses in ASOIAF}
\label{Tab1}
\begin{tabular}{|r|c|c|c|l|r|c|c|c|}
\hline
Sl.no & House & Kingdom & Sigil & Knightship & Leader & Weather & Origins & Capital \\\hline
1. & Stark & North & Direwolf & None & Eddard & Cold & First men & Winterfell\\\hline \hline
2. & Baratheon & Crownlands & Stag & Yes & Robert & Normal & Andals & King's Landing\\\hline
\end{tabular}
\end{table}

Table \ref{Tab1} has details of some houses in ASOIAF. Table \ref{Tab1} has details of some houses in ASOIAF.Table \ref{Tab1} has details of some houses in ASOIAF.

\begin{table}[h]
\centering
\begin{tabular}{|r|r|l|c|}
\hline
Sl.no & House & Kingdom & Sigil \\\hline
1. & Stark & North & Direwolf \\\hline
2. & Baratheon & Crownlands & Stag \\\hline
3. & Blackfyre & \multicolumn{2}{c|}{Not Applicable}\\\hline
4. & Targeryen & Valyria & Dragon\\
\cline{3-3}
 &  & Crownlands & \\ \hline 

\end{tabular}
\end{table}

\begin{tabular}{|c|c|c|c|c|}
\hline 
Sno & House & Leader & Captial & Sigil \\ 
\hline 
1 & Stark & Eddard & Winterfell & Direwolf \\ 
\hline 
2 & Martell & Doran & Dorne & Sun \\ 
\hline 
\end{tabular} 

\end{document}
```




## Text and Page Formatting


**Text:** 

```latex
for italicized words use, \textit{word}
for bold face words use, \textbf{word}
for small cap words use, \textsc{word}
for typewriter font use, \texttt{word} ! specifically used to distinguish normal fonts with web-page links.
for making a word look little larger than normal font use, \begin{large} word(s) \end{large}
for making a word look little larger than large font use, \begin{Large} word(s) \end{Large}
```
```latex 
priority of sizes tiny<small<normal<large<Large<huge<Huge
 
for a single sentence to be justified use \begin{justification} sentence \begin{justification}
justifications are center, flushleft, flushright. These can be used for tables, figures, a chunk of document etc.,
 
\tt{} \bf{} \sc{} \it{} works the same way as that of the top (looks like so)
```

**Page and Line:**
```latex
\newpage command for making a new page
\newline is used for a page break.
```
 
**Colouring:**
```latex
Select/envelop a group of text using {} brackets and put \color{colour name} to change the colour of the enveloped text/content. Works well in beamer. (to be checked in documents). For this option to work, add \usepackage{color} at the preamble!
```
 
**Spacing**

```latex
Use \quad for tab spacing, \qquad for double tab spacing. Use them appropriately for extended spacing
Use \hspace{length} for horizontal spacing. Eg: \hspace{4cm}
To create a very small horizontal space, use \,
Use \vspace{length} for vertical spacing. Eg: \vspace{1ex} = size of 1 ex character ?! (needs check)
\hfill is used for filling the horizontal spaces
 
Paragraph and line indenting: Worst Case Situations:
Use \<space> \newline \\ in proper order for manipulate spacing and tabbing. Crude method, but can act as a quick fix
```

Document and text formatting

```latex
\documentclass[10pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[english]{babel}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage{graphicx}

\usepackage{color}
% For colours
\usepackage{latexsym}
% for some special symbols

\setlength{\parindent}{4em}
% Set the Paragraph indent
% 1 em means the length of 1 letter "m" in the current font size.
\setlength{\parskip}{1em}
% Set the distance between paragraphs
\renewcommand{\baselinestretch}{2.0}
% Set the line spacing. 2 means twice the normal spacing

\usepackage[left=2cm,right=2cm,top=2cm,bottom=2cm]{geometry}
\author{Arun Prasaad Gunasekaran}
\title{Text and Document Formatting}
\begin{document}
\maketitle

\tableofcontents

\section{Text Styles}
%\slshape %slant font
%\textsl{} % for a small content
%\textup{} %default font
%\upshape
%\itshape %italic font
%\textit{}

%\scshape % Capitalize
%\textsc{}
%\mdseries % default medium size
%\textmd
%\bfseries % Bold font
%\textbf{}

%\rmfamily % Regular roman font
%\textrm{}
%\sffamily % Sans Serif Font
%\textsf{}
%\ttfamily % Type writer font
%\texttt{}

%\rm %roman font
%\it % italic
%\em %emphasis
%\bf % bold
%\sl %slant 
%\sc %small caps
%\sf %Sans serif font
%\tt % type writer font

Text emphasis is given using \textbf{Commands (Like this!)} and \textit{functions (Like this!)}. The purpose of \textsc{Commands and functions (Like This!)} here, is to enable certain contents \textsf{distinguished} from other contents. These commands \textsl{enhance reading} as they make contents \texttt{stand out} uniquely!

\emph{This sentence is \emph{emphasized!}}

\color{red}

This sentence is in red!

\color{black}

%\itshape
You can change the text font as well. \textup{"This"} is the normal font! \textmd{"This"} is the medium size! \textrm{"This"} is the regular font family

Font sizes can be changed!\\ 
%\tiny Size\\ 
%\scriptsize Size \\
%\footnotesize Size \\
%\small Size\\
%\normalsize Size\\
%\large Size\\
%\Large Size\\
%\LARGE Size\\
%\huge Size\\
%\Huge Size\\

\section{Special Symbols}

\$ \% \# \{ \& \_ are special symbols. G\"ottingen

\t{oo}

\AA \oe \dag \ddag

\pounds   \copyright

$\pi \ \Pi$

$\sigma \ \Sigma$

$ \Xi \ \vartheta$

$\mathcal{F} \mathcal{L}$

$ x \not \ge y$

$ \pm \mp $

$ A \cap B$

$ \Delta ABC \equiv \Delta DEF$

$ A \gg B \  C \propto D$

$ \Longleftrightarrow $

$ \nabla \surd \partial$

$ \Box \ \Diamond$

$ \backslash $

$ \clubsuit \diamondsuit \heartsuit \spadesuit$

$ \int^b_a $

$\displaystyle{\oint \limits^b_a}$

$ \displaystyle{\lim \limits_{x \to 0} \frac{\sin{x}}{x} = 1}$

$ \vec{A} = a_1\vec{i} + a_2\vec{j} + a_3\vec{k}$

$ \lim \limits_{x \to 0} \frac{\sin{x}}{x} = 1$

$\lg \gcd$

\( \lim \limits_{n \rightarrow \infty} \)

$ \lim \limits_{n \rightarrow \infty}$

$$ \lim \limits_{n \rightarrow \infty}$$

\[ \lim \limits_{n \rightarrow \infty} \]

$$ \lim_{n \rightarrow \infty} $$

\section{Document Formatting}

\subsection{Spacing}
Spacing is possible using the backslash command. For instance, if you want to write something like Zuckerberg and co.\ \ \ \ \ and proceed writing, you might see an additional space.

\hspace{5cm} hspace command is used for making a space horizontally. While \vspace{2cm} is used for making space vertically. 

\hfill Hfill command is used to fill the sentence accordingly, so that the right margin is fine!

\subsection{Document Symbols}
Quotations are easy! Use '' for quotations 'like this one' "or this one" For the quote to "open" and "close" properly, use reverse quotes ``Like this"\\

Use --- for a long dash! use \TeX and \LaTeX for TeX and LaTeX symbols.\\

For underlining, use \underline{Underline command}. For overhead and under-head symbols, use $\overbrace{O}  \underbrace{U}  \overbrace{\underbrace{B}} $

\section{Document sections}

\subsection{Foot notes}

To type a foot note, use "footnote" \footnote{This is a command for foot notes} option.

To write a paragraph, use paragraph command to name it

\subsection{Paragraphs and Subparagraphs}

\paragraph{Paragraph1}
This is paragraph1. This is paragraph1. This is paragraph1. This is paragraph1. This is paragraph1. This is paragraph1. This is paragraph1. This is paragraph1. This is paragraph1. This is paragraph1. This is paragraph1. 

To write a sub-paragraph use sub-paragraph command
\subparagraph{Subpara1}
This is paragraph1. This is paragraph1. This is paragraph1. This is paragraph1. This is paragraph1. This is paragraph1. This is paragraph1. This is \par paragraph1. This is paragraph1. This is paragraph1. This is paragraph1.

\subparagraph{Subpara}This is paragraph1. This is paragraph1. This is paragraph1. This is paragraph1. This is paragraph1. This is paragraph1. This is paragraph1. This is paragraph1. This is paragraph1. This is paragraph1. This is paragraph1.

paragraph and subparagraph are just titles!

par command is used for producing a new paragraph on the run. The indentation and spacing are set by the commands

\subsection{Quotes}

To write a quote, use begin quote (for a small one) and begin quotation (for a large one) environment.

\begin{quote}
Brevity is the soul of wit
\end{quote}

\begin{quotation}
I can write a very very very big quotation here!
\end{quotation}

\subsection{Poetry}

To write a poetry, use begin verse environment.

\begin{verse}
TWO roads diverged in a yellow wood,\\	
And sorry I could not travel both,\\	
And be one traveller, long I stood,\\	
And looked down one as far as I could,\\	
To where it bent in the undergrowth;\\
 
Then took the other, as just as fair,\\	
And having perhaps the better claim,\\	
Because it was grassy and wanted wear;\\	
Though as for that the passing there\\	
Had worn them really about the same,\\

\hfill - Robert Frost
\end{verse}

\subsection{Description}

To add a description, use begin description environment.

\begin{description}
\item [stark] House with the sigil Direwolf
\item [lannister] House with the sigil Lion
\item [baratheon] House with the sigil Stag
\end{description}

This is repeatable using enumerate as well, but there is a difference!

\begin{enumerate}
\item [\textbf{stark}] House with the sigil Direwolf
\item [\textbf{lannister}] House with the sigil Lion
\item [\textbf{baratheon}] House with the sigil Stag
\end{enumerate}


\end{document}
```

\$ \% \# \{ \& \_ are special symbols. G\"ottingen

\t{oo}

\AA \oe \dag \ddag

\pounds   \copyright

$\pi \ \Pi$

$\sigma \ \Sigma$

$ \Xi \ \vartheta$

$\mathcal{F} \mathcal{L}$

$ x \not \ge y$

$ \pm \mp $

$ A \cap B$

$ \Delta ABC \equiv \Delta DEF$

$ A \gg B \  C \propto D$

$ \Longleftrightarrow $

$ \nabla \surd \partial$

$ \Box \ \Diamond$

$ \backslash $

$ \clubsuit \diamondsuit \heartsuit \spadesuit$

$ \int^b_a $

$\displaystyle{\oint \limits^b_a}$

$ \displaystyle{\lim \limits_{x \to 0} \frac{\sin{x}}{x} = 1}$

$ \vec{A} = a_1\vec{i} + a_2\vec{j} + a_3\vec{k}$

$ \lim \limits_{x \to 0} \frac{\sin{x}}{x} = 1$

$\lg \gcd$

\( \lim \limits_{n \rightarrow \infty} \)

$ \lim \limits_{n \rightarrow \infty}$

$$ \lim \limits_{n \rightarrow \infty}$$

\[ \lim \limits_{n \rightarrow \infty} \]

$$ \lim_{n \rightarrow \infty} $$


## Arrays and Tabbing

### Arrays:

Arrays are similar to tables

```LaTeX

$$ 

\begin{array}{clcr}

1 & 2 & 3 & 4 \\
5 & 6 & 7 & 8

\end{array}

$$

```

### Tabbing:

Tabbing is again similar to tables.

```LaTeX

\begin{tabbing}

Column 1 \= Column 2 \\
\= \= Column 5 
\end{tabbing}

```

### Creating Matrix

To create a matrix, use the following code

```LaTeX

$$\begin{matrix}
a & b & c \\
d & e & f & g \\
\end{matrix}$$
```
 
The above command will create a bracket less 2x4 matrix with a14 being empty
Using pmatrix will create a matrix with curved brackets, bmatrix will create a matrix with rectangular brackets.
Bmatrix for curly bracket matrix
 
One complex example:

```LaTeX

$$\begin{pmatrix}
a & a^2 & \cdots & a^n \\
b & b^2 & \cdots & b^n \\
\vdots & & \ddots \\
n & n^2 & \cdots & n^n
\end{pmatrix}$$
```

## Figures


To include figures, use the package,

```LaTeX
\usepackage{graphicx}
```

To use .eps figures (Encapsulated Post Script), use the package,

```LaTeX
\usepackage{eps2pdf}
```
 
To include a figure use  % do not use  ``` \begin{figure} \end{figure} ``` in presentations. Use include graphics directly.

```LaTeX
\begin{figure}
\centering
\includegraphics[size parameters]{figure_name.ext}
\caption{figure title}  % for figures, the caption/title is given, usually after the figure
\label{reference}        % the label should be given after caption.
\end{figure}
```
 
``` \centering ``` centre justifies the figures. Wrapping the image with ``` \begin{center} ``` and ``` \end{center} ``` will also work. ``` \centering ``` will work within the entire begin field ``` \begin{figure} \end{figure} ``` is used to make the figure an independent whole object that can be moved around together, so that it does not act like alphabets or symbols or numbers.

``` \label ``` is used to give a reference name to the file, so that it can be referred within the file at other places.

``` \caption ``` is used to give the figure a title.

Only a selected few formats can be placed, namely,

```
.png, .jpeg, .pdf, .eps, .giff, .jpg
```

**Size parameters ** are:

Width or height = some value with unit.

Eg: 
```LaTeX
Width=5in, width=0.5\pagewidth, 0.7\pageheight, 0.8\linewidth % page width and line width apparently works for documents and beamer (possibly) 
```


Scale = value between (0,inf] if value greater than 1, then the image is magnified, else it is shrunked. If value equals 1, then same size.
Eg: scale = 0.5, 0.05, 2
 
Angle = value between [0,360] rotates the image accordingly in ccw. Angle can be negative.
Eg: angle = 45
All the figures must be in the same folder where the .tex file is kept. Also, the figure names should have no spaces.

## Multiple Figures in a Page

Source: http://tex.stackexchange.com/questions/119905/insert-multiple-figures-in-latex As on 12th May, 2015

Below is how to insert two figures. Pls adapt this as per your needs. You need subcaption package.

```LaTeX
\documentclass{article}
\usepackage[demo]{graphicx}
\usepackage{subcaption}
\begin{document}
\begin{figure}
\begin{subfigure}{.5\textwidth}
\centering
\includegraphics[width=.8\linewidth]{image1}
\caption{1a}
\label{fig:sfig1}
\end{subfigure}%
\begin{subfigure}{.5\textwidth}
\centering
\includegraphics[width=.8\linewidth]{image2}
\caption{1b}
\label{fig:sfig2}
\end{subfigure}
\caption{plots of....}
\label{fig:fig}
\end{figure}
\end{document}
```

Other Source:

Using subfloats and minipages

http://texblog.org/2011/05/24/placing-figures-side-by-side-subfig/

http://tex.stackexchange.com/questions/9584/how-to-put-subfigures-in-several-rows

## Minipages and Boxes

Minipage divides the page into multiple pages width-wise. fbox is used for putting a box around contents. hfill ensures that the contents are nicely spaced out width-wise. A blank line pushes the minipage to the next line. A soft return retains the minipage on the same line, provided the dimensions of the page do not interfere.

```LaTeX

\begin{minipage}[t]{0.48\textwidth}
	I am in a Hot city, on top of a big mountain, with few trees, eating a banana on a starry evening, looking for a shooting star!
\end{minipage}
\hfill
\begin{minipage}[t]{0.4\textwidth}
	I am in a Hot city, on top of a big mountain, with few trees, eating a banana on a starry evening, looking for a shooting star!
\end{minipage}
\hfill
\begin{minipage}[t]{0.25\textwidth}
	I am in a Hot city, on top of a big mountain, with few trees, eating a banana on a starry evening, looking for a shooting star!
\end{minipage}
\hfill
\begin{minipage}[t]{0.25\textwidth}
	I am in a Hot city, on top of a big mountain, with few trees, eating a banana on a starry evening, looking for a shooting star!
\end{minipage}

\begin{minipage}[t]{0.25\textwidth}
	I am in a Hot city, on top of a big mountain, with few trees, eating a banana on a starry evening, looking for a shooting star!
\end{minipage}
\begin{minipage}[t]{0.25\textwidth}
	I am in a Hot city, on top of a big mountain, with few trees, eating a banana on a starry evening, looking for a shooting star!
\end{minipage}
\begin{minipage}[t]{0.25\textwidth}
	I am in a Hot city, on top of a big mountain, with few trees, eating a banana on a starry evening, looking for a shooting star!
\end{minipage}
\begin{minipage}[t]{0.25\textwidth}
	I am in a Hot city, on top of a big mountain, with few trees, eating a banana on a starry evening, looking for a shooting star!
\end{minipage}

\fbox
{
	\begin{minipage}[t]{0.33\textwidth}
	I am in a snowy city, on top of a big mountain, with few trees, eating a banana on a starry evening, looking for a shooting star!
	\end{minipage}
}

\fbox
{
\begin{minipage}[t]{0.33\textwidth}
	I am in a Hot city, on top of a big mountain, with few trees, eating a banana on a starry evening, looking for a shooting star!
\end{minipage}
}
\hfill
\fbox
{
\begin{minipage}[t]{0.33\textwidth}
	I am in a Hot city, on top of a big mountain, with few trees, eating a banana on a starry evening, looking for a shooting star!
\end{minipage}
}

```

## Report Writing

Use the report class. It is similar to article class, except that, report class accepts chapters. Article class does not accept chapters.

To include chapters on the run, use

```latex
\chapter{Chapter name}
```
If chapters are in a separate file, use

```latex
\chapter{Chapter name}
\input{Chapter file}
% Provided, the input file does not have a "chapter" command!

\include{Chapter file}
% Provided, the input file has a "chapter" command

```


## Writing Source Code

This is done in two ways:

* Using verbatim environment
* Using listing environment

### Verbatim Environment

This is an easy way, but not much colourful. Write the contents within a verbatim environment

```LaTeX
\begin{verbatim}
code ...
\end{verbatim}
```

The other way is to use listing environment.

### Listing Environment

Source: https://en.wikibooks.org/wiki/LaTeX/Source_Code_Listings

This has more features.

To use the package, you need:

```LaTeX
\usepackage{listings}
```

The listings package supports highlighting of all the most common languages and it is highly customizable. If you just want to write code within your document the package provides the lstlisting environment:

```LaTeX
\begin{lstlisting}
Put your code here.
\end{lstlisting}
```

You can also import the source code, specify the language, starting and ending lines and a frame box.

```LaTeX
\lstinputlisting[language=Python, firstline=37, lastline=45, frame=single]{source_filename.py}
```

You can modify several parameters that will affect how the code is shown. You can put the following code anywhere in the document (it doesn't matter whether before or after **\begin{document} **), change it according to your needs. The meaning is explained next to any line.

```LaTeX
\usepackage{listings}
\usepackage{color}

\definecolor{mygreen}{rgb}{0,0.6,0}
\definecolor{mygray}{rgb}{0.5,0.5,0.5}
\definecolor{mymauve}{rgb}{0.58,0,0.82}

\lstset{ %
  backgroundcolor=\color{white},   % choose the background color; you must add \usepackage{color} or \usepackage{xcolor}
  basicstyle=\footnotesize,        % the size of the fonts that are used for the code
  breakatwhitespace=false,         % sets if automatic breaks should only happen at whitespace
  breaklines=true,                 % sets automatic line breaking
  captionpos=b,                    % sets the caption-position to bottom
  commentstyle=\color{mygreen},    % comment style
  deletekeywords={...},            % if you want to delete keywords from the given language
  escapeinside={\%*}{*)},          % if you want to add LaTeX within your code
  extendedchars=true,              % lets you use non-ASCII characters; for 8-bits encodings only, does not work with UTF-8
  frame=single,	                   % adds a frame around the code
  keepspaces=true,                 % keeps spaces in text, useful for keeping indentation of code (possibly needs columns=flexible)
  keywordstyle=\color{blue},       % keyword style
  language=Octave,                 % the language of the code
  otherkeywords={*,...},            % if you want to add more keywords to the set
  numbers=left,                    % where to put the line-numbers; possible values are (none, left, right)
  numbersep=5pt,                   % how far the line-numbers are from the code
  numberstyle=\tiny\color{mygray}, % the style that is used for the line-numbers
  rulecolor=\color{black},         % if not set, the frame-color may be changed on line-breaks within not-black text (e.g. comments (green here))
  showspaces=false,                % show spaces everywhere adding particular underscores; it overrides 'showstringspaces'
  showstringspaces=false,          % underline spaces within strings only
  showtabs=false,                  % show tabs within strings adding particular underscores
  stepnumber=2,                    % the step between two line-numbers. If it's 1, each line will be numbered
  stringstyle=\color{mymauve},     % string literal style
  tabsize=2,	                   % sets default tabsize to 2 spaces
  title=\lstname                   % show the filename of files included with \lstinputlisting; also try caption instead of title
}
```

Style definition inside the package lets you define multiple styles, i.e. profiles specifying a set of settings.

```latex

\lstdefinestyle{customc}{
  belowcaptionskip=1\baselineskip,
  breaklines=true,
  frame=L,
  xleftmargin=\parindent,
  language=C,
  showstringspaces=false,
  basicstyle=\footnotesize\ttfamily,
  keywordstyle=\bfseries\color{green!40!black},
  commentstyle=\itshape\color{purple!40!black},
  identifierstyle=\color{blue},
  stringstyle=\color{orange},
}

\lstdefinestyle{customasm}{
  belowcaptionskip=1\baselineskip,
  frame=L,
  xleftmargin=\parindent,
  language=[x86masm]Assembler,
  basicstyle=\footnotesize\ttfamily,
  commentstyle=\itshape\color{purple!40!black},
}

% And use them separately
\lstset{escapechar=@,style=customc}

```

### Minted Package

This is similar to listing package. It uses the _pygments_ package and colouring scheme of python for colouring and styling code. You need to include this package in the document preamble. **Python 2.5 and above should be installed in the system to use this package.**

## Bibliography using BiBTeX

To make bibliography entries, you can use bib files. Bib Files have all the citation entries.

* Go to google scholar
* Type a paper name, click cite
* Get the bibtex citation code
* Paste it inside a bib file
* Do this for all the entries

Once done, your bib file is ready.

A sample citation entry looks like this:

```LaTeX
@article{forget_1991,
  title={Improved general circulation models of the Martian atmosphere from the surface to above 80 km},
  author={Forget, Fran{\c{c}}ois and Hourdin, Fr{\'e}d{\'e}ric and Fournier, Richard and Hourdin, Christophe and Talagrand, Olivier and Collins, Matthew and Lewis, Stephen R and Read, Peter L and Huot, Jean-Paul},
  journal={Journal of Geophysical Research: Planets (1991--2012)},
  volume={104},
  number={E10},
  pages={24155--24175},
  year={1999},
  publisher={Wiley Online Library}
}
```

The first one is the keyword or the id of the article. All the others are the article properties. You can have articles, books, magazines, papers, url links, etc., You can create your own citation entry as you wish!

**Citing in the Document**

Include this line in the document preamble

```LaTeX
\bibliographystyle{apalike} % This is a bibliography style
```

Include the bib file in the document with this line.

```LaTeX
\bibliography{references} % This is the reference file. bib extension not needed.
```

Cite the entries inside the document using ``` \cite{keyword} or \citep{keyword} ``` or equivalent.

```latex
There is a paper by a person named Forget \citep{forget_1991} on Martian Atmosphere GCM. Other papers, for instance, Gierasch \citep{gierasch1968study}, Conrath, \cite{conrath1975thermal} also explain some research topics on Mars.
```

And based on the styling chosen, the bibliography entries appear accordingly. **Only the selected entries will be referenced!**

Bibliography styles : plain, alpha, apalike, ieeetr, unsrt, acm etc.,

**Natbib**

Natbib is a separate bibliography style collection. It has several bibliography styles. **apalike** style under natbib is excellent.

To include natbib, use the line

```latex
\usepackage{natbib}
```
