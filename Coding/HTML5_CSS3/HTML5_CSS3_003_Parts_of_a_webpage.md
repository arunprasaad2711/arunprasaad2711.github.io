
# Parts of a Webpage

Arun Prasaad Gunasekaran

## Structure of a Webpage

The structure of any webpage looks like this.

<?prettify?>
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

Using "Emmet" extension in **VSCode**, you just have to type ``!<tab>`` to get the structure ready.

## Sandwich method.

Almost all the features of a web-page is built based on tags.
HTML tags follow a sandwich method, wherein all features are placed in pair-tags and all subsequent lower-order pair-tags are placed within other higher-order pair-tags. Also called as "tag-embedding". 
Apparently, the tags appear case-insensitive. The HTML5 standard does not require lowercase tags, but W3C recommends lowercase in HTML4, and demands lowercase for stricter document types like XHTML. 

Source: W3 Schools


### Doctype tag

<?prettify?>
```HTML
<!DOCTYPE html>
```

Short for Document Tag. Not a tag, but a declaration. Tells the web browser what definitions or version the website uses. This is the default doctype for **HTML5** and future versions. This tag is optional, but it is a good practice to put it. This has to be the first tag on the webpage.

Older versions of websites had various definitions and had different versions. Hence, some tags might not be common or available.

**HTML 4.01 Strict**

<?prettify?>
```HTML
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
```

**HTML 4.01 Transitional**

<?prettify?>
```HTML
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
```

**HTML 4.01 Frameset**
<?prettify?>
```HTML
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Frameset//EN" "http://www.w3.org/TR/html4/frameset.dtd">
```

**XHTML 1.0 Strict**
<?prettify?>
```HTML
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
```

**XHTML 1.0 Transitional**

<?prettify?>
```HTML
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
```

**XHTML 1.0 Frameset**
<?prettify?>
```HTML
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Frameset//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-frameset.dtd">
```

**XHTML 1.1**
<?prettify?>
```HTML
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
```

## Rules in Tags
<?prettify?>
```HTML
<tagname> content </tagname>

<title> Home page </title>

<img>

```

* Contents are enveloped in tags.
* Tags are commands enveloped in angle brackets (or less than, greater than signs).
* Most tags are in pairs. Closing tag has a forward slash.
* Some tags are single.

### HTML TAG

This is the starting and the ending of the webpage. Every webpage should begin in this manner.
<?prettify?>
```HTML
<html>
    
    <head>
    
        <!-- Write the important details for the webpage here. Eg: JavaScript links/code, Stylesheets/rules, title and meta-information. -->
    
    </head>
    
    <body>
    
        <!-- Write the body of the webpage here. All the contents you write here will be displayed to the user. -->
    
    </body>
    
</html>
````

## YouTube Video

<iframe width="540" height="315" src="https://www.youtube.com/embed/wPMACUPgYJQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### ``<html> </html>``
This is the wrapper tag for the entire webpage. It starts and ends the webpage. This is compulsory.

### ``<head> </head>``
This is the head tag. It contains metadata that is useful for getting information while searching for webpages in the internet.
The contents of the head tag are not displayed in the website. It has provisions to include JavaScript functions, CSS code and links to JavaScript and CSS files located externally.

### ``<body> </body>``
This is the body tag. All the contents written and displayed on the webpage goes here. You write whatever you want to inside here. Also, you can include small JavaScript functions and code snippets here.

### Comments
<?prettify?>
```HTML
<!-- Write your comment here! -->
```
Comments are ignored. Used for displaying information. They are ignored by default by the browser. It helps the user to write notes and to block code.


### Title
<?prettify?>
```HTML
<title> Hello, World!</title>
```

Title of the webpage. Written in the head tag.

### Paragraph
<?prettify?>
```HTML
<p>
    Hello, World! My name is Arun and this is my website. I love it! :)
</p>
```

Write paragraphs using ``<p> ... </p>`` tag. Long written contents are recommended to be written here.
