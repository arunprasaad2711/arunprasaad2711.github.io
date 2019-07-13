# Jinja2 Notes

## What is it?
Jinja is a template engine (it is like a language on its own) that helps to place strings in documents.
Essentially, you have a document with placeholders or variables called template.
The data to be placed is provided by another file or from user.

Jinja takes the data from the user and places it at the placeholders in the template to give you the desired document.

This is more powerful than the built-in string formatter of Python.

It is used with Flask and Django web frameworks for making web pages.

However, it is generic in nature and can be used in many ways.

These notes are taken from [a YouTube Tutorial on Jinja2 by Jason Rigden](https://www.youtube.com/watch?v=bxhXQG1qJPM)

## Example

Let's say that the template file had a sentence like this:

```
{{name}} had a little {{animal}}
```

Here, ``name`` is a variable and it is placed within backticks. Same with ``animal``.
The curly brackets are placeholders for the variables.

Suppose ``name = 'Mary'`` and ``animal = 'Lamb'`` are the values provided by the user.

Then Jinja will take these values and replace the variables in the template to give this file:

```
Mary had a little Lamb
```

## Where is it used?

* Websites.
* Making large text documents.

## How to go about it?
* Create a template document with placeholders.
* Write python code to generate the output file.
* Give data to the python file either as a text file or as direct input.
* Run the code to generate the output file.

## How to start?

The following examples go from a simplistic case to an advanced case step-by-step.

### Example 1: Read and Print a text file.

Note: This is a preliminary "Hello, World!" program to sort out the basics! 

* Open a Python file and write this line first in it.

```Python
from jinja2 import Environment, FileSystemLoader
```

* Create a file loader variable and pass the folder name where the template files are present.

```Python
file_loader = FileSystemLoader('templates')
```

* Note that the directory/folder name here can by anything!

* Create an enviroment variable and pass the file loader variable to it.

```Python
env = Environment(loader=file_loader)
```

* Now, the environment is ready.

* Now, create an input text file and write contents into it. We'll call it "hello_world.txt"

```
Hello, world!
```

* In the python file, create a template variable and pass the text to it.

```Python
template = env.get_template('hello_world.txt')
```

* Now, create an output variable by rendering the template variable and print it.

```Python
output = template.render()
print(output)
```

* You can pass variables to the ``render()`` method. But, that is for a future example.

* Run the python file and the output will be:

```
Hello, World!
```

This is the full code:

```Python
# Import the required methods
from jinja2 import Environment, FileSystemLoader

# Specify the template directory and environment 
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

# Create a template variable via environment
template = env.get_template('hello_world.txt')

# Render the template and create an output variable.
output = template.render()

# Print it out to see or export it to a new file as you see fit.
print(output)
```

### Example 2: Adding Variables.

* Prerequisite code

```Python
# Import the required methods
from jinja2 import Environment, FileSystemLoader

# Specify the template directory and environment 
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
```

* Create a template file and place variables with curly bracket placeholders. Let's call it ``lamb.txt``

```
{{name}} had a little {{animal}}.
```

* Load the template and render it with variables.

```Python
# Create a template variable via environment
template = env.get_template('lamb.txt')

# Render the template and create an output variable.
output = template.render(name='Mary', animal='Lamb')

# Print it out to see or export it to a new file as you see fit.
print(output)
```

* The output is

```
Mary had a little Lamb.
```

### Example 3: Using Dictionaries

* Prerequisite code

```Python
# Import the required methods
from jinja2 import Environment, FileSystemLoader

# Specify the template directory and environment 
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
```

* Create a template file and place variables with curly bracket placeholders. Let's call it ``lamb.txt``

```
{{data.name}} had a little {{data.animal}}.
```

* Load the template and render it with a dictionary.

```Python
# Create a template variable via environment
template = env.get_template('lamb.txt')

# Create a dictionary
person = {}
person['name'] = 'Mary'
person['animal'] = 'Lamb'

# Render the template and create an output variable.
output = template.render(data=person)

# Print it out to see or export it to a new file as you see fit.
print(output)
```

* The output is

```
Mary had a little Lamb.
```

### Example 4: Using if-else statements.

* Prerequisite code

```Python
# Import the required methods
from jinja2 import Environment, FileSystemLoader

# Specify the template directory and environment 
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
```

* Template file: ``truth.txt``

```Python
{% if truth %}
	This is true
{% else %}
	This is false
{% endif %}
```

* Modifications 1: Set truth variable to be True

```Python
template = env.get_template('truth.txt')
output = template.render(truth=True)
print(output)
```

* Output
```
This is true
```

* Modifications 2: Set truth variable to be False

```Python
template = env.get_template('truth.txt')
output = template.render(truth=False)
print(output)
```

* Output
```
This is false
```

### Example 5: For loops using lists/tuples

* Prerequisite code

```Python
# Import the required methods
from jinja2 import Environment, FileSystemLoader

# Specify the template directory and environment 
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
```

* Template file: ``rainbow.txt``

```Python
{% for colour in colours %}
	{{colour}}
{% endfor %}
```

* Modifications: Pass a list/tuple

```Python
template = env.get_template('rainbow.txt')

colours = ['red', 'green', 'blue']
output = template.render(colours=colours)
print(output)
```

* Output

```
red

green

blue
```

### Example 6: Template inheritance - combine blocks from multiple places.

* Prerequisite code

```Python
# Import the required methods
from jinja2 import Environment, FileSystemLoader

# Specify the template directory and environment 
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
```

* Include file: ``header.html`` - Has the title. It will be included in the template.

```HTML
<head>
	<title>{{title}}</title>
</head>
```

* Base file: ``base.html`` - This is the base file.

```HTML
<html>
	{% include 'header.html' %}
	<body>
	</body>
</html>
```

* Modifications

```Python
template = env.get_template('base.html')

output = template.render(title="Hey, there!")
print(output)
```

* Output

```HTML
<html>
	<head>
		<title>Hey, there!</title>
	</head>
	<body>
	</body>
</html>
```

Observation: Here, the ``base.html`` file automatically called ``header.html`` file.
And inside it, the title variable was automatically placed.

### Example 7: Template rendering + Placing data in body tag

* Prerequisite code

```Python
# Import the required methods
from jinja2 import Environment, FileSystemLoader

# Specify the template directory and environment 
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
```

* Include file: ``header.html`` - Has the title. It will be included in the template.

```HTML
<head>
	<title>{{title}}</title>
</head>
```

* Base file: ``base.html`` - This is the base file with content!

```html
<html>
	{% include 'header.html' %}
	<body>
	{% block content %}
	{% endblock %}
	</body>
</html>
```

* Template file: ``child.html`` - Contents of this file fill be placed.

```html
{% extends "base.html" %}

{% block content %}

	<p>
		{{body}}
	</p>

{% endblock %}
```

* Modifications

```Python
template = env.get_template('child.html')

output = template.render(title="Hey, there!", body="Brown cow!")
print(output)
```

* Output

```HTML
<html>
	<head>
		<title>Hey, there!</title>
	</head>
	<body>
		<p>
			Brown cow!
		</p>
	</body>
</html>
```
