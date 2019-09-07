# LaTeX

<!-- TOC -->

- [LaTeX](#latex)
  - [Introduction](#introduction)
  - [Sources, Why, Origin and Forums](#sources-why-origin-and-forums)
    - [Sources](#sources)
  - [Books](#books)
  - [Why LaTeX?](#why-latex)
  - [Forums](#forums)
  - [Requirements](#requirements)
  - [Compiler:](#compiler)
  - [Editor:](#editor)
  - [Cross platform editors:](#cross-platform-editors)
  - [Viewer:](#viewer)
  - [Accessories](#accessories)
  - [Configurations and File types](#configurations-and-file-types)
  - [File Extensions:](#file-extensions)
  - [General notes, Tips and Compiling](#general-notes-tips-and-compiling)
    - [General Notes:](#general-notes)
  - [Document Structure:](#document-structure)
  - [Tips](#tips)
  - [Compiling:](#compiling)
  - [Sample Preamble](#sample-preamble)
  - [Document Class, Doc Details](#document-class-doc-details)
    - [Document class details:](#document-class-details)
  - [Document Details:](#document-details)
  - [Packages](#packages)
  - [Sample Layout](#sample-layout)
  - [Begin Commands](#begin-commands)
  - [Bullets and Numbering](#bullets-and-numbering)
  - [Enumerate](#enumerate)
  - [Bullet and Numbered List](#bullet-and-numbered-list)
  - [Document Modes and Sections](#document-modes-and-sections)

<!-- /TOC -->

## Introduction

$\LaTeX$ is a type setting document

## Sources, Why, Origin and Forums
 
LaTeX has two inventors

1. Donald Knuth

He was the first person to create TeX, the basic compiling code used in LaTeX. When TeX was introduced, it was still difficult to follow.
       
2. Leslie Lamport

He was the person who made an interface on TeX to make LaTeX. This made document production very easy and productive.
 
### Sources
  
1. Video Lectures on LaTeX by Mitchell Krummel in Youtube
2. [Spoken Tutorials](Spoken-tutorials.org) Video Lectures

Lot of online references were taken/compiled from Stack Exchange, Sharetatex.com

Optional reference: moudgalya.org

**Will add more references when a considerable amount of information is collected from a single source. Some unmentioned sources will be present, but those shall contribute less. If more, then it will be cited.**

All these following steps are to be done in TeXMaker. They correspond without any change to TeXstudio. For other editors, there might be changes.

## Books
* LaTeX, A document preparation system, User's guide and reference manual by Leslie Lamport.
* LaTeX companion by F. Mittelbach and M. Goossens (advanced users)

Main website for all LaTeX related updates and sources is [CTAN](http://ctan.org) centraised TeX archive network.

## Why LaTeX?

* Free and Open Source
* What you type is what you get output 
* Cross platform compatibility. Especially with Windows/Mac/Unix/Linux 
* Has excellent features for scientific documents, Especially, the mathematical documents 
* Automatically takes care of formatting, numbering, updating and referencing chapters, figures, tables, page numbers, citations etc., 
* Standard of document print is excellent.
* Lot of user communities
* Excellent Typesetting software
* Easy to produce bibliography index and easy to change the entire document format in a few steps.
* Bibliographic entries are easy to make and produce

## Forums

One good place to check out will be [ShareLaTeX](www.sharelatex.com)
 
For user forums in India.

* Tug India.in
* Fossee.in

## Requirements

LaTeX is a type-setting program used for making scientific documents. It is to be viewed like a programming language.
 
LaTeX requires a few components, namely,

1. Compiler
2. Editor
3. Viewer
4. Accessories

## Compiler:

This is the core of the system. It is the basic codes that helps to produce outputs and results. It is completely mandatory.

It is available in different versions for different OS.

**Windows**:MiKTeX distribution (As of Oct 4, 2014, the Current Version is 2.9)

MikTeX is available from miktex.org

**Linux/Unix** : Comes pre-installed or added along with the editor. (can select and choose the necessary options)

**To be noted: It is very much advisable to install and use a "dedicated" editor (made especially for this purpose) for Linux/Unix systems. This will take care of the installation of the compilers during installation and making changes after edition. Directly installing LaTeX compilers is a bit tricky in Linux/Unix (as far as I have seen). This is not a problem in Windows/Mac because there, the compiler and editor are separate and independent, unlike in Linux/Unix.**

**Mac** : MacTeX distribution
 
## Editor:

This is where the codes are written/edited and saved. There are many editors.

## Cross platform editors:

TexMaker, TexStudio --- These are the ones that I use. Very good, All in one interface. Edits, Compiles and views results in one shot. Both have complimenting features

TexWorks, --- Comes with MiKTeX and MacTeX.  Not bad, but not much tried. All the three are dedicated LaTeX editor.

Emacs --- Good editor with colour differentiation, but cannot offer more features because it is a general purpose editor.
 
**Windows:**

TeXnicCentre : Works pretty well for windows. Similar to TeXmaker and TexStudio. More of "Windows format". But it is a dedicated LaTeX editor.
 
Any editor can be used in this regard. However, the use of a dedicated editor is preferred for ease.

**Mac**: To be checked.
 
**Linux:**

Lync : There are a lot of similarities, but operates differently.

LaTeXilla, : not tried

Kile : This can be a good alternative to TeXStudio and TeXMaker.
 
## Viewer:
It is a pdf viewer to see the results. Sometimes, you can have ghost-script results which need other viewers. Will be updated when the information is received. Most of the editors will have them by default. 

Some examples are,

Adobe PDF : For Windows. All time classic, but does not have "memory", meaning, it will not show the last modified page during recompilations.

Sumatra: Light and handy, has "memory" suits for windows.

Skim : Just like sumatra, but for Mac OS 

Mostly, the default pdf viewers associated with dedicated editors are sufficient.
 
## Accessories

These are additional software, that is not necessary for LaTeX compilation, but assists in making figures or they serve other purposes. Some of them are:
 
1. Xfig : Specifically used for making layouts, flowcharts, and presentation related figures etc., (Available for Mac. Windows and Linux/Unix = to be checked)

## Configurations and File types

Startup Settings for TeXMaker:

0. Open TeXmaker
1. Go to Options>Configure TeXmaker>Commands> Check the embed option in pdf viewer.

This is for having a parallel pdf view along with the pdf.

2. Go to Options>Configure TeXmaker>quick build>select pdfLaTeX+view pdf.

This is for setting the output of our files to be pdf by default. make changes here for different output formats.

3. Go to Options>Configure TeXmaker>editor>Check the word-wrap, completion and show line numbers (check backup after 10 min if needed).

For assistance and ease only.
     
While handling bibliography entries, 

```bash
  use Options>Configure TeXmaker>quick build>select pdfLaTeX + BibTeX 
  pdfLaTex(x2) + view pdf
```    
This is a short method for taking care of bibilography entries easily.
 
## File Extensions:

The LaTeX files have several extensions.

TeX file or the .tex is the important file. It is the script file you write and compile to get the output. This file is mandatory. If this file is deleted without a backup, you have to re do the work from scratch.
 
Bibliography file or the bib file with extension .bib is used for storing bibliographical references. The specific bibliography entries are called when these files are included and keywords associated with them are referred.
 
A log file or .log is present after compilation. It has a list of all the compiling steps involved and has useful messages that can be used for debugging if needed.
 
Most of the other files are backup files and intermediate object/binary/log/executable files that get generated during compilation. Noticeably, all the files, including the pdf file, executables, tex file and intermediates will have the same name as that of the tex file.
 
All the files that have to be included within the pdf file such as figures and other chapters etc., have to be placed in the same folder.
 
So it is better to create a single folder, and save all your files inside it. Transfer figures and other files that you will like to include into the document within this folder.

``.sty`` is a LaTeX style format file. These are available in the libraries, and are included when certain packages are used. They are used for making certain styles and formats available in the documents.

``.toc`` file is a LaTeX table of contents file. When a table of contents generation is invoked, the compiler collects all the possible sections, their names and page numbers within the entire document and saves it here. Then, uses these data for generating the table of contents in the document.

``.bst`` is a bibliography style file. This is needed for changing the alignment/manner in which the citations are generated.

``.aux`` is an auxiliary file. Probably this file  is needed for executing multiple operations. This plays a role in invoking the BibTeX compilations.

``.cls`` is a document class file.

## General notes, Tips and Compiling

### General Notes:

* All commands start with a backslash.
* Almost all the commands usually come in pairs, analogous to html tags. So there is a start command and an end command.
* ``%`` stands for a single line comment. Everything that is typed after % becomes a comment. No multi-comment option is noticed.

LaTex has certain reserved symbols such as,

```latex
$,%,{,},\
```

These symbols are used in certain command contexts and to use them in general context, some alterations are to be done. (Will be explained as the notes progress)
 
some commands need arguments to be filled in. they require to be filled inside ``[]`` and ``{}``.

The arguments filled within ``[]`` are optional and they have a default value. So, even when they are not mentioned, it is fine. If you have no optional arguments, then ignore ``[]``. 

Empty ``[]`` will show an error. When mentioned, they overrule the default settings.

The arguments filled within ``{}`` are compulsory and optional. Some arguments inside it, are mandatory, while some arguments are optional, that will have a default value, which will get overruled when these optional arguments are filled.
 
## Document Structure:

The script for the .tex file goes like this:

```
document class definitions
package declarations
definitions and macros
title page details
 
document beginning
 
All the contents within the document including appropriate commands
 
document ending
 
extra contents
```
 
The contents in red are mandatory and can have changes. The contents in green are optional. The section above the document beginning is called as preamble.

All the contents in preamble are analogous to preprocessors or includes to be done, analogous to including .h files in c program.

The contents in blue are extra contents, which get ignored completely. Can be used as some notes or pointers or comments.
 
## Tips
1. Compile and execute every now and then. This helps in identifying the errors at the beginning stage. if too many errors pop-up, then it will be tedious to rectify them later.
2. Compiling and executing auto-saves the document. If not, it is advisable to save them before compiling.
3. Give comments and proper spacing ,tabbing for readability and explanations.
4. Compile + Build + View the document simultaneously and in parallel or alongside view. This helps to monitor changes and corrections.
5. Windows shortcut key combinations will work. So, use them advantageously.
 
## Compiling:
Compiling is the process of getting the output. For this to work, the LaTeX compiler must be installed.
 
If a dedicated LaTeX editor is used, such as TeXMaker or TeXstudio etc., then "build and view" file button (similar to that) will compile the codes, produces the pdf and displays the pdf.
 
If a general purpose editor is used, then you have to save the .tex file, and go to the command prompt and execute commands to compile them.

In Mac and most probably in Linux/Unix versions, type

```bash
pdflatex filename.tex
```

to compile the code and produce the pdf.

We can omit the ``.tex`` file to get the same result. However, as a practice, .tex is to be used.
 
The compiled results are stored in filename.log file

## Sample Preamble

```latex
\documentclass[10pt,a4paper,twoside]{article}
% Document Class
% Preamble
\usepackage[utf8]{inputenc}
% Setting the input encoding
\usepackage[english]{babel}
% The input language

% symbol is used for typing comments

\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}
% For including mathematical symbols

\usepackage[left=2cm,right=2cm,top=2cm,bottom=2cm]{geometry}
% Used for shaping the size of the page

\author{Arun Prasaad Gunasekaran}
\title{Introduction to LaTeX}
```

## Document Class, Doc Details

### Document class details:

this is the first command and should be present in each and every document at the first line. It goes like this:
 
```latex
\documentclass[font_size]{document_type,specs}
```

there are several kinds of document types:
1. article (most common article format)
2. chapter
3. report
4. beamer (for power point presentations)
5. letter
6. and many more…
 
specs are some document specifications such as
 
font_size defines the font size to be specified. there are 3 default font sizes namely,

10pt, 11pt and 12 pt. 

while mentioning them in LaTeX, you need to mention as follows.

```latex
\documentclass[10pt]{document_type,specs}
```
note that 'pt' is mandatory.

the default font size is 12pt.
 
## Document Details:
 
By default, the document will have a lot of user details. These are filled either by default or present when they are filled in. Those are namely,

```latex
\author[Short Name]{Long Name}   %for the file author
```

the short name is used while displaying in pages while the long name is used in the title pages. The long name can have more than the name, separated by \\ command.

eg:

```latex
\author[Arun]{G. Arun Prasaad\\Centre for Atmospheric and Oceanic Sciences\\Indian Institute of Science}
```

They may make a warning message, but that can be ignored.
 
**This feature of long value and short value will work well in the beamer class. It may not work properly, or might show errors in the other classes.**
 
```latex
\date{date attributes}   %for setting the date

use \date{\today} for using today's date.
```

by default, it will be available even without mentioning it. To avoid the date, use a blank date command.

The date gets displayed, by default, in the American Style format.: Full month name, Date, Year in 4 digits.

You can manually enter the date in the format of your choice.

Just like author name, it can have multiple lines.
 
```latex
\title{title of the document}
 
\subtitle{}
 
\institution{} %Beamer Class Command
 
\logo{}
```
Note: title/document details can be placed before or after begin document command!

## Packages

A Package is a collection of programs of LaTex, done for having certain formatting styles that includes, margin spacing, font and font size settings etc.,

LaTeX has its own set of packages. If external packages are used, latex will ask before implementing.
 
between \document class and \begin document, type
```latex
\usepackage{package name}
```

to set the page formatting package for the entire document.
 
some standard package names are:

1. fullpage
2. geometry

for geometry package, the formatting should be specific
```latex
\usepackage[top=1in, bottom=1in, left=1in, right=1in]{geometry}
```
in stands for inch. it can be centimeter cm or millimeter mm as well. 

```latex
\usepackage[margin=1in, paperwidth=8.5in, paperheight=11in]{geometry} % 8.5*11 inch^2 is the standard A4paper size.
 
\usepackage{amsfonts} %this is used to allow special mathematical fonts
$\mathbb{N}$ %after using the above package, the N will look different.
```
 
some of the packages are:

* graphicx - for including figures.
* cclicenses
* Harvard
* amsmath
* beamer - for ppt
* epstopdf - to convert and put eps figures into the document. It will be converted into a .pdf file and later put inside.
* Mathrsfs for including special curly mathematical notations.

## Sample Layout

The format of a latex document looks like this:

```latex
\documentclass[10pt,a4paper,twoside]{article}
% Document Class
% Preamble
\usepackage[utf8]{inputenc}
% List of packages and commands!
\usepackage[english]{babel}

\begin{document}
\maketitle

% All the contents

\end{document}

```

## Begin Commands

Begin commands form the majority of the commands in LaTeX. They always occur in pairs. For example,

```latex
\begin[options]{args}
contents
\end{args}
```
 
The args or arguments specify what the commands should do in pairs. Options vary depending on the argument used.
There are several arguments.
 
To begin the document, use the following command in a pair.

```latex
\begin{document}
all the contents, figures, tables etc.,
\end{document}
```

Without this, the document will not be processed. This is like a main function in a c program. Everything typed within this command pair forms the body of the document.

## Bullets and Numbering

The itemize command helps in creating bullet arguments. To start it, use

```latex
\begin{itemize}
\item  first bullet sentence
\item  second bullet sentence
\item and so on.
\end{itemize}
```
 
``\item`` is used for the bullet/number based on what option is chosen (itemize or enumerate)

chain bulleting is allowed. For that, create a ``` \begin{itemize} \end{itemize} ``` within an existing itemize command block.
 
## Enumerate
 
This option is used for making a numbered list. Everything is same as itemize. Use "enumerate" instead of "itemize".
 
Chain numbering is also possible. Also, a chain numbering and bulleting is also possible. However, you cannot bullet and number in a single field.
 
To create a list, the command used is with a proper example is shown below. it can be a list within a list as well. This is pretty much self- explanatory.

``\item`` is the bullet indicator.

```latex
\begin{enumerate}
    \item rossby
    \begin{enumerate}
        \item mid-latitude
            \begin{enumerate}
                \item 45 deg latitude
                \item 30 deg latitude
            \end{enumerate}
        \item equatorial
    \end{enumerate}
    \item kelvin
    \item inertia
    \begin{enumerate}
        \item external gravity
        \item internal gravity
    \end{enumerate}
    \item poincare
    \item yanai
\end{enumerate}
```

The tabbing here, is done only for readability. The compilation will take care of it.

To insert bullets rather than numbers, use itemize instead of enumerate.

To change the labels to the symbol of your choice or word of your choice, use [symbol or word] after ``\item``. You can have multiple labels.

Eg:

```latex
\begin{enumerate}
\item [Rossby Wave] Mid latitude 45 degree
\item [Gravity Wave] External Inertia
\item [Others] Poincare
\end{enumerate}
```

## Bullet and Numbered List

```latex
% LaTeX files have many extensions!
% This is a bullet list!

\begin{document}

\begin{itemize}
\item .tex = TeX file. The core file and the most important file. All contents are written/typed within this file.
\item .bib bibliography files. It has the attributes and meta data (author's name, title, pages, abstract, year of publication ....)
\item .log Log file. It contains all the errors, warnings, execution messages, steps while compiling, etc.,
\item .aux .gz support files that come when a .tex file is executed.
\item .sty style format files. They contain TeX instructions and and formats to be included in the file.
\item .bst this is a style file for bibliography.
\item .toc this is a table of contents file
\item .cls class files.
\end{itemize}

% This is a numbered list!
\begin{enumerate}
\item .tex = TeX file. The core file and the most important file. All contents are written/typed within this file.
\item .bib bibliography files. It has the attributes and meta data (author's name, title, pages, abstract, year of publication ....)
\item .log Log file. It contains all the errors, warnings, execution messages, steps while compiling, etc.,
\item .aux .gz support files that come when a .tex file is executed.
\item .sty style format files. They contain TeX instructions and and formats to be included in the file.
\item .bst this is a style file for bibliography.
\item .toc this is a table of contents file
\item .cls class files.
\end{enumerate}

\end{document}
```

## Document Modes and Sections

Use ``%`` for entering a single line comment. Multi-line comments are not available (So far)

 
use ``$ contents $`` to go into a running text mathematical mode or in-line maths mode.

 
use ``$$ contents $$`` to go into a centre justified mathematical mode or display maths mode. If certain symbols are used without defining a mathematical mode, (eg: `^`), the program will show an error.

Contents entered within maths mode will be properly in mathematical format. They will follow a different font with an inclination or in italics.
 
While typing lines, "Enter" key or "Return" key is not taken as a line completion or a line break. By default, the program has a paragraph indent.


Leaving a blank line in the .tex file is interpreted as an end of the paragraph (or a hard return). So, a new line when begun, is taken as a start for a new paragraph.


No matter how many hard returns or blank you give in the tex file, it will be read as a single hard return. Apparently, in a letter format, a blank line is taken as a new paragraph beginning.

 
While typing lines, if you just want a line break without going into the next paragraph, (or a soft return), use \\ at the end of the line and continue typing. This command should have text at the front as well as at the back. This will not create an indent.

 
There are some options to alter the indentations. It is to be explored.

 
If you reach the bottom of a page, and you type certain extra lines, LaTeX will automatically push the contents to the next page, or shrink fit them into the same page. It depends on the length of the content.

 
Similarly, while placing figures and tables, LaTeX will automatically adjust content displays to fit them accordingly.