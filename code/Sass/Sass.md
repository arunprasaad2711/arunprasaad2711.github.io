# SASS

<!-- TOC -->

- [SASS](#SASS)
  - [Introduction](#Introduction)
  - [Installation](#Installation)
  - [Quickstart](#Quickstart)
  - [About ``config.rb`` file](#About-configrb-file)
  - [Alternate way to create ``sass`` project](#Alternate-way-to-create-sass-project)
  - [Create partials](#Create-partials)
  - [Comments and Notes.](#Comments-and-Notes)
  - [Autocompile ``sass`` files](#Autocompile-sass-files)
  - [Usage of a mixin](#Usage-of-a-mixin)
  - [Includes in ``style.scss``](#Includes-in-stylescss)
  - [Wrapper ID/Class](#Wrapper-IDClass)
  - [To prevent overlap of elements](#To-prevent-overlap-of-elements)
  - [Inheritance - Examples](#Inheritance---Examples)
  - [left-side bar links](#left-side-bar-links)
  - [Nesting CSS properties](#Nesting-CSS-properties)
  - [Extending already existing properties](#Extending-already-existing-properties)
  - [Creating generic properties so that you can use and extend them](#Creating-generic-properties-so-that-you-can-use-and-extend-them)
  - [colour altering commands](#colour-altering-commands)
  - [mixins from compass](#mixins-from-compass)
  - [text-shadow](#text-shadow)
  - [gradient](#gradient)
  - [working with images](#working-with-images)
  - [Transformations](#Transformations)
  - [Drop shadow using compass mixin](#Drop-shadow-using-compass-mixin)
  - [if conditions](#if-conditions)
  - [for loop](#for-loop)
  - [spriting using compass mixins](#spriting-using-compass-mixins)
  - [Table Styling](#Table-Styling)

<!-- /TOC -->

## Introduction
SASS is an extension of CSS with a lot of cool features. Once you compile SASS, you get CSS files.

It adds
* Variables
  * Use variables to store colours or attribute values and use them throughout the SASS document. So, in the future, if you want to change the value at all the places, just change the value at one place and recompile it to get the CSS files.
* Nesting
  * Essentially, list properties one inside the other, like a nest. Avoids repetition of styles and selectors.
* Mixins
  * Helps to reuse chunks of CSS styles.
* Selector Inheritance
  * Can tell one selector to inherit all the styles of another without duplicating the CSS properties.

Essentially, it helps to write CSS very quickly and conveniently.

``Compass`` is an additional plugin used to add more functions to ``sass``.

## Installation

1. Ruby gems

```bash
sudo gem install sass compass
```

2. npm install
   
```bash
npm install -g sass
```

To check if you have SASS installed, you type

```bash
sass --version
```

## Quickstart

To start a ``sass`` project, type this in the terminal

```bash
compass create project_name
```

It will produce a sass folder, a stylesheet folder, and a ruby ``config.rb``.

```bash
arun@hpdv6:~/Website_Experimental/sass_tutorial$ tree
.
├── config.rb
├── sass
│   ├── ie.scss
│   ├── print.scss
│   └── screen.scss
├── sass.md         # This is user-made
├── stylesheets
│   ├── ie.css
│   ├── print.css
│   └── screen.css
└── testing.html    # This is user-made

2 directories, 9 files
```

It will also suggests to add this ``HTML5`` code snippet to any html file.

```HTML
<head>
<link href="/stylesheets/screen.css" media="screen, projection" rel="stylesheet" type="text/css" />
<link href="/stylesheets/print.css" media="print" rel="stylesheet" type="text/css" />
<!--[if IE]>
    <link href="/stylesheets/ie.css" media="screen, projection" rel="stylesheet" type="text/css" />
<![endif]-->
</head>
```

This part is helpful to test the css files using the html file.

## About ``config.rb`` file

At the start, it looks like this

```ruby
require 'compass/import-once/activate'
# Require any additional compass plugins here.

# Set this to the root of your project when deployed:
http_path = "/"
css_dir = "stylesheets"
sass_dir = "sass"
images_dir = "images"
javascripts_dir = "javascripts"

# You can select your preferred output style here (can be overridden via the command line):
# output_style = :expanded or :nested or :compact or :compressed

# To enable relative paths to assets via compass helper functions. Uncomment:
# relative_assets = true

# To disable debugging comments that display the original location of your selectors. Uncomment:
# line_comments = false


# If you prefer the indented syntax, you might want to regenerate this
# project again passing --syntax sass, or you can uncomment this:
# preferred_syntax = :sass
# and then run:
# sass-convert -R --from scss --to sass sass scss && rm -rf sass && mv scss sass

```
You can edit this configuration file as you wish.

* ``require`` - to include a plugin required for the project. Use one require statement per plugin.
* ``http_path`` - The relative path location for the project.
* ``xxxx_dir`` - corresponding directories
* ``output_style`` - the output style of the css files.
  * nested - use indents to display the css output.
  * compact - pushes all the code into a single line.
  * compressed - compact + removes comments and whitespace
  * expand - full-fledged css with comments, white spaces. It is the SCSS files translated to CSS as it is.

## Alternate way to create ``sass`` project

```bash
compass create --sass-dir "sass_directory" --css-dir "css_directory" --javascripts-dir "js" --images-dir "images"
```

## Create partials

These are subdirectories with sass file fragments. These will be included into the main sass files. This is the tree layout after creating the partials.

Also, outside partials folder, create ``styles.scss`` file.

```bash
arun@hpdv6:~/Website_Experimental/sass_tutorial$ tree
.
├── config.rb
├── sass
│   ├── ie.scss
│   ├── partials
│   │   ├── _base.scss
│   │   ├── _layout.scss
│   │   ├── _mixins.scss
│   │   ├── _normalize.scss
│   │   └── _variables.scss
│   ├── print.scss
│   ├── screen.scss
|   └── styles.scss
├── sass.md
├── stylesheets
│   ├── ie.css
│   ├── print.css
│   └── screen.css
└── testing.html

3 directories, 14 files
```

* ``_base.scss``: the basic structure of the webpage
* ``_layout.scss``: the design layout of the webpage
* ``_mixins.scss``: reusable css definitions
* ``_variables.scss``: the variables to be used everywhere
* ``_normalize.scss``: collection of css attributes and html elements to normalize the style across all browsers. 

## Comments and Notes.

```scss

// Single Line Comment
/*
Multi-Line comment. When merging multiple files, it may not appear where you want.
*/

/*!
Loud multi-line comment. It will exactly appear where you want.
*/

```

You can create your own ``_normalize.scss`` file if you know what "normalization" means. Else, you can copy paste it from contents.

## Autocompile ``sass`` files

Using compass, you can automatically compile the ``sass`` files to produce the equivalent ``css`` files.

In the root folder, type this in the terminal.

```bash
arun@hpdv6:~/Website_Experimental/sass_tutorial$ compass watch
 modified config.rb
    clean stylesheets
   delete stylesheets/ie.css
   delete stylesheets/print.css
   delete stylesheets/screen.css
>>> Compass is watching for changes. Press Ctrl-C to Stop.
    write stylesheets/ie.css
    write stylesheets/print.css
    write stylesheets/screen.css

```

Alternatively, you can compile it using just ``sass``

```bash
sass --watch style.scss:style.css
```

As long as it is running, any changes to the ``sass`` files will be immediately reflected to the ``css`` files.

## Usage of a mixin

A mixin is a function. You give some values to it, and it operates on it and gives some other values.

Define one like this:

```scss
/* Mixins */
/* Functions that take in some value and do some work for us. */

// mixin keyword - mixin name - function arguments, default value,
@mixin default-text-color($tc: $black)
{
    // some task.
    color: $tc;
}
```
And implement it in other places like this:

```scss
body 
{
  font-family: Arial, Helvetica, sans-serif;
  font-size: 1em;
  background: $gray;
  line-height: 1em;

  // We are defining the text color with a mixin
  @include default-text-color($black);
}
```

## Includes in ``style.scss``
Write these lines into the ``style.scss`` file.

```scss
@import "compass";
@import "partials/variables";
@import "partials/normalize";
@import "partials/mixins";
@import "partials/base";
@import "compass/css3";
```

## Wrapper ID/Class

```css
#wrapper 
{
    background: $white;
    margin: 0 auto;
    max-width: 800px;
}
```

## To prevent overlap of elements

```scss
// Fixes overlapping issues
// Makes the rendered box elements padding, borders, etc.
// fit into the width
   
*
{
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box;
}
```

## Inheritance - Examples

```scss
article p a
{
    color: $blue;
    &:hover, &:focus 
    {
        color: $duke-blue;
    }
    &:visited
    {
        color: $blue-gray;
    }
}
```

## left-side bar links

Each link is a block. It is mildly transparent. On hover, it becomes fully opaque.
```scss
.left-sidebar-links {
  a {
    display: block;
    color: $main-green;
    opacity: .7;
    &:hover {
      opacity: 1;
    }
  }
}
```

Put a border line at the bottom of each link, except the last one.
```scss
.left-sidebar-links {
  border-bottom: 2px solid $main-green;
  &:last-child {
    border: none;
  }
}
```

## Nesting CSS properties

```scss
// You can nest CSS properties as well
.example-element {
  border: {
    top: 1px solid $blue;
    right: 1px solid $red;
    bottom: 1px solid $yellow;
    left: 1px solid $green;
  }
}
```

## Extending already existing properties

```scss
// @extend existing properties
#riddle{
  padding: 20px;
  background-color: $alice-blue;
}
 
#riddle-answer{
  @extend #riddle;
  margin-top: 10px;
}
```

## Creating generic properties so that you can use and extend them

```scss
// Creating properties just so we can extend them
 
%dotted-box {
 
  border: 2px dotted $duke-blue;
  margin: 10px 0px;
}
 
#riddle-answer{
  @extend %dotted-box;
}
```

## colour altering commands

```scss
// Lighten a color
// You can use darken in the same way
 
.left-sidebar-links{
  border-color: lighten($main-green, 70%);
}
 
// You can generate the 180 degree complement of a color
 
#search-button:hover {
  background-color: complement($main-green);
}
 
// You can invert a color by sending the degree (0 - 360)
 
#search-button:hover {
  background-color: adjust-hue($main-green, 90deg);
}
 
// Specify a background color for the <li> that is the
// first child of #vert-nav ul and desaturate (darken)
 
#vert-nav ul li:nth-child(1) {
  background-color: desaturate($orange, 80%);
}
 
// Saturate a color by a percent
 
#vert-nav ul li:nth-child(2){
  background-color: saturate($orange, 80%);
}
 
// Define transparence (0 to 1 Opaque)
 
#vert-nav ul li:nth-child(3){
  background-color: fade-out($orange, .5);
}
 
// Make a color more opaque (0 to 1 Opaque)
 
#vert-nav ul li:nth-child(3){
  background-color: fade-in($orange, .8);
}
 
// Define the RGB color
 
#vert-nav ul li:nth-child(4){
  background-color: rgba(0, 0, 200, 0.5);
}
 
// Mix 2 colors plus the percent of the first color
 
#vert-nav ul li:nth-child(5){
  background-color: mix($yellow, $white, 50%);
}
 
// Make the color passed grayscale
 
#vert-nav ul li:nth-child(6){
  background-color: grayscale($yellow);
}
 
/*
adjust-color allows you to adjust
red, green and blue : 0 to 255
hue : 0 to 359
saturation : 0 to 100
lightness : 0 to 100
alpha : 0 to 1
Either adjust RGB or HSL
*/
 
#vert-nav ul li:nth-child(7){
  background-color: adjust-color($main-green, $red:0, $green:40, $blue:30);
}
 
#vert-nav ul li:nth-child(7){
  background-color: adjust-color($main-green, $hue:30, $saturation:40, $lightness:30, $alpha:0.2);
}
 
// shade combines the color with a percent of black
 
#vert-nav ul li:nth-child(8){
  background-color: shade($yellow, 50%);
}
 
// tint combines the color with a percent of white
 
#vert-nav ul li:nth-child(9){
  background-color: tint($yellow, 50%);
}
```

## mixins from compass

mixins from compass automatically generate equivalent properties that are compatible with other webbrowsers. Essentially, it produces cross-browser stuff.

Mixin used in ``sass`` from ``compass``

```scss
// Rounds the border and adds a box shadow
 
#riddle-answer {
  @include border-radius(5px);
 
  // Horizontal then vertical offset, blur, spread, color
  @include box-shadow(5px 5px 5px 2px gray);
}
```

The equivalent ``css``.

```css
/* line 273, ../sass/styles.scss */
#riddle-answer {
  -moz-border-radius: 5px;
  -webkit-border-radius: 5px;
  border-radius: 5px;
  -moz-box-shadow: 5px 5px 5px 2px gray;
  -webkit-box-shadow: 5px 5px 5px 2px gray;
  box-shadow: 5px 5px 5px 2px gray;
}
```

## text-shadow

```scss
// Color, horizontal then verical offset, blur amount
#main-title{
  @include text-shadow(rgba(blue, 0.2) 2px 2px 3px);
}
```

## gradient
```scss
// Created for extension
// Direction or left / right / top / bottom, color stops
 
%main-green-gradient{
 
  @include background-image(linear-gradient(left, $main-green 80%, $white));
}
 
footer {
  @extend %main-green-gradient;
}
 
#horz-nav {
  @extend %main-green-gradient;
}
```

## working with images

```scss
// Target the img with the given alt and change the src
// and restore the proper size
 
img[alt="Programming Frameworks"] {
  content: image-url('featured-image.png');
  // can also extract image dimensions
  /*
  width: image-width('../images/featured-image.png');
  height: image-height('../images/featured-image.png');
  */
}
```

## Transformations

```scss
// Use a Compass mixin to scale 2x horz & vert
// Move horz & vert, rotate 45deg and perform multiple transforms
 
#logo {
  @include scale(2,2);
  @include transform(translateX(700px) translateY(10px)
  scale(2,2) rotate(-45deg));
}

```

## Drop shadow using compass mixin

```scss
// Add the compass drop shadow on all text in the p
 
article p:nth-child(2){
  @include filter(drop-shadow($gray 1px 1px 0px));
}
```

## if conditions

```scss
// We can change properties based on conditions
 
$riddle-color: gray;
 
@if $riddle-color == blue {
  #riddle {
    background-color: $alice-blue;
  }
} @else {
  #riddle {
    background-color: $ash-gray;
  }
}
```

## for loop

```scss
// We can use for loops to change as we iterate
 
$prct-yellow: 5%;
 
@for $i from 1 through 14 {
  #vert-nav ul li:nth-child(#{$i}){
    background-color: mix($yellow, $white, $prct-yellow);
  }
 
  $prct-yellow: $prct-yellow + 5%
 
}
```

## spriting using compass mixins

```scss
// Spriting with Compass
// Combines images in the provided folder into 1 image
// to limit server requests
// Define the directory for the images and it provides
// the background image definition and location for use
// by your elements
 
@import "compass/utilities/sprites";

// folder with the images.
@import "icons/*.png";

// sprite mixin
@include all-icons-sprites;

// grouping the images into 1
.icons {
  .clock { @include icons-sprite(clock);}
  .diary { @include icons-sprite(diary);}
  .printer { @include icons-sprite(printer);}
  .weather { @include icons-sprite(weather);}
}

// size of the individual images
.icons * {
  height: 64px;
  width: 64px;
}
```

## Table Styling

```scss
@import "compass/utilities/tables";
 
.baseball-stats {
  table {
    $table-color: $black;
    @include table-scaffolding;
 
    // Define the inner border
    @include inner-table-borders(4px, $table-color);
 
    // Define the outer border
    @include outer-table-borders(4px, $duke-blue);
 
    // Handles table striping even row color, odd row color, intersection, header
    @include alternating-rows-and-columns($alice-blue, $ash-gray, $table-color, $white);
 
    width: 400px;
  }
}
```