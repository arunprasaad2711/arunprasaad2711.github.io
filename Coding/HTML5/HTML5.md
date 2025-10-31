# HTML

HTML stands for _Hyper Text Markup Language_. It is not a programming language. It helps to write or create contents. Used primaily for creating web pages and web applications, HTML is also used these days in conjuction with other tools and technologies for creating web applications, even GUI, and software.

Web pages and web applications created solely based on HTML are not visually appealing. For that, one needs to use tools such as **CSS** or Cascading Style Sheets.

**JavaScript and PHP** are the defacto programming languages for developing web applications and programming functionality in websites. JavaScript is particularly popular because of its features and powers. The implementation features are great leading to an explosion of library bundles for various purposes such as AngularJS, NodeJS, ReactJS etc., PHP and JavaScript are useful for dynamically creating webpages with variables!

HTML has a long history. Prior to the current standard HTML5, the previous versions have standards issue; each version had rules and protocols, leading to websites developed with one version not compatible with other machines or web browsers and many more. Some of the older versions are XHTML, HTML 1-4.

All of these notes are going to be in __HTML5__

Also, there is another Markup language called **SVG** or Scalable Vector Graphics. It is similar to HTML.

## References
* Traversy media - Brad Traversy youtube channel
* KhanAcademy
* w3schools
* Complete Reference : [w3schools](https://www.w3schools.com/tags/default.asp)

## Requirements
* A Good Browser
    * Recommended
        * Chrome, Firefox, Safari
    * Others
        * Opera, Edge etc.,
* A text editor
    * Pick one you like!
    * Simple ones:
        * Notepad, Notepad++, Leafpad, gedit, Kate, etc.,
    * Fancy ones:
        * Atom, Sublime, Visual Studio Code, Webstorm etc.,

**Quick tip: You can view the source code of the webpage inside a web browser. Also, there are developer tools in Chrome (press ``F12``) (console, elements tab, etc.,) that are particularly useful while developing webpages to look at the various parts of the webpage and also to catch errors while using and running JavaScript and or PHP code**

## Some notes
* No other software needed!
* Cross platform! Not dependent on OS
* The extension is \*.html for the html pages
* The home page is called ``index.html``
* You do not need a server while testing and building
* However, you need a server and domain name for hosting it on the internet.

## Tag structures
* Commands in HTML are in tags
    * ``<tagname> contents </tagname>``
* As mentioned above, tags are in pairs
* Some tags are self-closing or independent, i.e, they do not occur in pairs
    * ``<br/>`` (Older HTML and XHTML implementation) or simply ``<br>`` (HTML5 implementation)

## HTML Page structure
```HTML
<!DOCTYPE html> <!-- This tells the type of the HTML version used -->
<html>

    <head>
        <!-- Head of the file. Has metadata for search.
        Also has scripts and script links for CSS,
        JavaScript -->
        <meta charset="utf-8">
        <title> Title of the Page </title>
        <!-- Other contents -->
    </head>

    <body>
        <!-- This is the body of the file! -->
        <!-- All the contents here are displayed in the browser. -->
        <!-- Other contents -->
    </body>

</html>
```

## Tag types

### Block tags
* They start in a new line.
* They takeup the entire width of the page.
    * eg: ``<div>``, ``<h1>``, ``<p>``, ``<form>``

### Inline Tags
* They start where they are.
* They do not takeup an entire line.
    * eg: ``<span>``, ``<img>``, ``<a>``

### Self closing tags
* Takes no contents
    * eg: ``<br/>`` (HTML4 and before), ``<br>`` (HTML5)
* Comes alone. No pairs.

## Tags

### ``<!DOCTYPE html>``
Documentation type Tag. Tells what kind of HTML page or version is. This is the standard HTML5 DOCTYPE tag. Other versions have different DOCTYPE tags, and those have many structures. HTML5 standard DOCTYPE will be used. This tag is optional, but it is a good practice to put it. This has to be the first tag on the webpage.

### ``<html> </html>``
This is the wrapper tag for the entire webpage. It starts and ends the webpage. This is compulsory.

### ``<head> </head>``
This is the head tag. It contains metadata that is useful for getting information while searching for webpages in the internet.
The contents of the head tag are not displayed in the website. It has provisions to include JavaScript functions, CSS code and links to JavaScript and CSS files located externally.

### ``<title> </title>``
Title tag. Shows the title of the webpage.

### ``<body> </body>``
This is the body tag. All the contents written and displayed on the webpage goes here. You write whatever you want to inside here. Also, you can include small JavaScript functions and code snippets here.

### ``<!-- comment -->``
This is the comment tag. Within the ``-- --`` of the tag, you can write comments. They are ignored by default by the browser. It helps the user to write notes and to block code.

### Conditional Comments
Used to execute tags if and only if certain conditions are met. In other cases, it is ignored.
```HTML
<!--[if IE 9]>
    .... some HTML here ....
<![endif]-->
```

### ``<h1> </h1>``
This is a heading tag. The biggest heading available in the webpage. There are progressively smaller ones namely ``h2, h3, h4, h5, h6``. Each heading has its own size, margin size, and padding.

```HTML
<h1>Heading 1</h1>
<h2>Heading 2</h2>
<h3>Heading 3</h3>
<h4>Heading 4</h4>
<h5>Heading 5</h5>
<h6>Heading 6</h6>
```

### ``<p> </p>``
This is a paragraph tag. **This is a block tag**, meaning this tag appears separately. It cannot lie in the same line as that of another tag. Has ``1em`` margin. (``1em`` = 1 font size)

```HTML
<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
```

### ``<br>``
This is a line break. Used for pushing the contents to the next line.

```HTML
<br>
```

### ``<hr>``
This is a horizontal rule tag. Used for drawing a horizontal line.

```HTML
<hr>
```

### ``<strong> </strong>``
This is the **bold** tag. This tag has _semantic_ importance. The older bold tag does the same and has no _semantic_ importance. The old tag is not recommended.
```HTML
<strong>This text is strong/bold</strong>
<b>This text is bold</b>
```

### ``<em> </em>``
This is the italics tag. Called as *emphasis*. The older italics tag does the same and has no _semantic_ importance. The older italic tag is not recommended.
```HTML
<em>This text is italic/emphasised</em>
<i>This text is italic</i>
```

### ``<small> </small>``
Defines smaller text.
```HTML
<p>This is <small>superscripted</small> text.</p>
```

### ``<mark> </mark>``
Defines a marked or highlighted text.
```HTML
<p>This is <mark>superscripted</mark> text.</p>
```

### ``<del> </del>``
Defines a deleted text.
```HTML
<p>This is <del>superscripted</del> text.</p>
```

### ``<ins> </ins>``
Defines an inserted text.
```HTML
<p>This is <ins>inserted</ins> text.</p>
```

### ``<sub> </sub>``
Defines a subscripted text.
```HTML
<p>This is <sub>subscripted</sub> text.</p>
```

### ``<sup> </sup>>``
Defines a superscripted text.
```HTML
<p>This is <sup>superscripted</sup> text.</p>
```

### ``<a> </a>``
This is the _link_ tag. Used for linking a webpage.
Syntax:
```HTML
<a href="link_to_webpage_or_section" target="_blank"> This is a link </a>
```
**href** is the hytertext reference. Simply put, the location to go when clicked. It can be a new webpage or a section in the current webpage.

**target** is a placeholder to tell where the webpage has to be opened.

* ``_blank`` is used to open the referenced page in a new tab.
* ``_self`` - Opens the linked document in the same window/tab as it was clicked (this is default)
* ``_parent`` - Opens the linked document in the parent frame
* ``_top`` - Opens the linked document in the full body of the window
* ``framename`` - Opens the linked document in a named frame

### ``<ul> </ul>``
Tag for **unordered** lists or **bullet** lists. You can change the bulltes.
```HTML
<ul>
    <li> List Item 1 </li> <!-- List item -->
    <li> List Item 2 </li>
    .........
    <li> List Item n </li>
</ul>
```

### ``<ol> </ol>``
Tag for **ordered** lists or **numbered** lists. Numbers are auto-generated.
```HTML
<ol>
    <li> List Item 1 </li>
    <li> List Item 2 </li>
    .........
    <li> List Item n </li>
</ol>
```

### ``<table> </table>``
The table tag. Requires ``<thead>`` the table head tag, ``<tbody>`` the table body tag, ``<tr>`` the table row tag, ``<th>`` the table headings tag, and ``<td>`` the table data tags.

```HTML
<table>
    <thead>
        <tr>
            <th>  Name </th>
            <th>  Email </th>
            <th>  Age </th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>  Name1 </td>
            <td>  Email1 </td>
            <td>  Age1 </td>
        </tr>
        <tr>
            <td>  Name2 </td>
            <td>  Email2 </td>
            <td>  Age2 </td>
        </tr>
        <tr>
            <td>  Name3 </td>
            <td>  Email3 </td>
            <td>  Age3 </td>
        </tr>
    </tbody>
</table>
```

Earlier, tables were used for making structured webpages by creating layouts. Now, it is not used anymore, as it is not a good practice. Use tables just for tabular data.

### ``<form> </form>``
Used for creating a form for submission and processing. Requires ``JavaScript`` for full functionality. HTML can only be used for creating the elements. Labels and input are **inline** elements. Needs block level elements to place them well, for example ``<div>`` tags.

```HTML
<!-- action submits the form to a certain page. -->
<!-- method tells what we are going to do -->
<form class="" action="index.html" method="post">
    <div class="">
        <label for="">First Name</label> <!-- Fancy Label -->
        <!-- type = data type, name = variable name -->
        <input type="text" name="firstName" value="Enter First Name"> <!-- input option-->
    </div>
    <br>
    <div class="">
        <label for="">Last Name</label>
        <input type="text" name="lastName" value="Enter Last Name">
    </div>
    <br>
    <div class="">
        <label for="">Email Address</label>
        <input type="email" name="email" value="johndoe@unknown.com">
    </div>
    <br>
    <div class="">
        <label for="">Message for user</label>
        <!-- text area tag for typing a message. -->
        <textarea name="message" rows="8" cols="80"></textarea>
    </div>
    <br>
    <div class="">
        <label for="">Gender</label>
        <!-- text area tag for typing a message. -->
        <select class="" name="gender">
            <option value="male">Male</option>
            <option value="female">Female</option>
            <option value="other">Other</option>
        </select>
    </div>
    <br>
    <div class="">
        <label for="">Age</label>
        <!--number type, default value -->
        <input type="number" name="age" value="">
    </div>
    <br>
    <div class="">
        <label for="">Birthday</label>
        <input type="date" name="birthday" value="">
    </div>
    <br>
    <!-- submit button for the form-->
    <input type="submit" name="submit" value="submit">
</form>
```
``post`` (in ``method``) means post a request to a server. Used for adding data to a server. ``get`` means to post and get data from a server.

### ``<button> </button>``
Used for creating a button

```HTML
<button event="functionName" type="button" name="buttonName">Click Me</button>
```

### ``<img>``
Self-closing tag. Not inline. Used for enclosing images.

```HTML
<img src="pathOrLink/to/filename" alt="sample message for image if image not found" width="widthValue" height="heightValue">
```
Usually the image aspect ratios are preserved. When width or height attribute is used, then the image scales accordingly. Usage of both leads to distort the image's aspect ratio.

### ``<blockquote> </blockquote>``
Used for writing a block quote.
```HTML
<blockquote cite="http://websitename.com">
    Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
</blockquote>
```

### ``<abbr> </abbr>``
Abbreviation tag. Used for Abbreviations.
```HTML
<abbr title="American Standard Code for Information Interchange">ASCII</abbr>
```

### ``<cite> </cite>``
Citation tag. Gives a small italics. Used for citations.
```HTML
<cite>HTML notes</cite>
```

### ``<q> </q>``
Short question tag.
```HTML
<p>WWF's goal is to: <q>Build a future where people live in harmony with nature.</q></p>
```

### ``<address> </address>``
Address tag.
```HTML
<address>
Written by John Doe.<br>
Visit us at:<br>
Example.com<br>
Box 564, Disneyland<br>
USA
</address>
```

### ``<bdo> </bdo>``
Used to write the text in right to left or left to right. Bi-directional override.

```HTML
<bdo dir="rtl">This text will be written from right to left</bdo>
```

### ``<div> </div>``
Used for creating divisions in the page or section. Block tag.
```HTML
<div style="color:#0000FF">
    <h3>This is a heading</h3>
    <p>This is a paragraph.</p>
</div>
```

### ``<meta> </meta>``
Includes search keywords and information to be used by search engines for finding them. Stands for metadata.

```HTML
<meta name="description" content="Notes by Arun">
<meta name="keywords" content="notes, html, css, JavaScript, libraries, python, sphinx">
<meta charset="utf-8">
<!-- utf-8 specifies english like script, not others like arabic etc.,-->
```

## HTML5 Semantic Tags.
Tags that tell what it means to both the browser and the developer.

### ``<header> </header>``
The header tag. Has the website logo, social media links etc.,

### ``<footer> </footer>``
The footer tag. Has copyright/trademark symbols, address, external links, etc.,

### ``<aside> </aside>``
Has information that is placed aside in the webpage.

### ``<main> </main>``
Has main information placed in the webpage.

### ``<article> </article>``
Main content / articles in the webpage tag.

### ``<nav> </nav>``
Navigation bar tag. Navigation links are wrapped around using this tag.

### ``<section> </section>``
Defines sections in the webpage.

### ``<details> </details>``
Used for placing details.

## Length measurements
### Relative measurements
* ``em``	Relative to the font-size of the element (2em means 2 times the size of the current font)
* ``ex``	Relative to the x-height of the current font (rarely used)
* ``ch``	Relative to width of the "0" (zero)
rem	Relative to font-size of the root element
* ``vw``	Relative to 1% of the width of the viewport*
* ``vh``	Relative to 1% of the height of the viewport*
* ``vmin``	Relative to 1% of viewport's* smaller dimension
* ``vmax``	Relative to 1% of viewport's* larger dimension

**Tip: The em and rem units are practical in creating perfectly scalable layout!**

**\*Viewport = the browser window size. If the viewport is 50cm wide, 1vw = 0.5cm.**

For more information, [Length Units from w3schools ](https://www.w3schools.com/cssref/css_units.asp)

## Definitions

### Attribute
Similar to functional arguments in other programming languages. Optional. Helps you to give or assign values to the elements.
Attributes are always placed in start tags. Attributes are treated as key-value pairs. Meaning, if an attribute or key is used, then it must be assigned to a value. If not, an error pops up. To avoid errors, either assign a key to a value or do not use a key.
Values are given in double quotes. Single quotes are okay, but usually not preferred.

### Margins
Spacing around the element.

### Padding
Spacing between the core element and the border.

### Entity symbols
Special character symbols. Like the copyright sign.
