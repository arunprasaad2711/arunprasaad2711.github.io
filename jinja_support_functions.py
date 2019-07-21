# Import the required methods
from jinja2 import Environment, FileSystemLoader

# Import OS file for terminal operations
from os import system

# Specify the template directory and environment 
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

# Function to convert md files to html snippets using pandoc. 
# Then uses jinja to render them into proper html files.
# This is the active one!
def md2html_conv(category, hfolder, mfolder, folder, leftIndex, rightIndex):
	
	# Extract list of md files in the given folder
	system("ls {0}/{1}/*.md > {0}/{1}/{1}.txt".format(mfolder, folder))
	
	# Consolidate a list of rst files, html names, and article names
	md = []
	name = []
	html = []
	
	# Open up the list of rst files
	with open("{0}/{1}/{1}.txt".format(mfolder, folder), 'r') as f:
		
		# Read all the lines.
		temp_lines = f.readlines()
		# print(temp_lines)
		
		# In each filename, remove the trailing "\n", and save it in rst
		# Remove rst extensiton and folder prefix and save the name
		# Create an HTML file name
		for tl in temp_lines:
			nl = tl.rstrip()
			nl_name = nl[leftIndex:rightIndex]
			nl_html = hfolder+"/"+folder+"/"+nl_name+".html"
			# print(nl, nl_name, nl_html) # uncomment this for cross-check
			md.append(nl)
			name.append(nl_name)
			html.append(nl_html)
	
	# Convert each rst files into a HTML file
	i = 0
	
	# Use pandoc to convert the rst file to HTML5 file and shove it in a temporary file.
	# Read the contents of the file in a variable.
	# Open the template file
	# Render the template to get the output
	# Push the output to the HTML filename created above
	for title in md:
		print(title)
		
		# Converts! - but stuffs a html page inside the template. No JS needed! Provides Syntax highligh codes for themes! - useful for extracting themes out!
		# system("pandoc --from markdown --to html5 --mathjax --highlight-style=haddock --css=assets/css/main.css {} > temp.html".format(title))
		# Simple Markdown to HTML convert command. For code highlight to work, include the code.css file in the main.css file.
		# Used to work, but now some trouble! Surrounds every line by a link
		# system("pandoc --from markdown --to html5 --mathjax {} > temp.html".format(title))
		system("pandoc --from=markdown --to=html5 --no-highlight --mathjax {} > temp.html".format(title))
		# system("pandoc --from=markdown --to=html5 --highlight-style=haddock --mathjax {} > temp.html".format(title))
		
		# A new attempt!
		# system("python -m markdown -x codehilite {} > temp.html".format(title))
		# system("pygmentize -S default -f html > codehilite.css")
		
		with open("temp.html", "r") as p:
			content = p.read()
		# system("cp templates/blog_template.html templates/blog_template_temp.html")
		
		template = env.get_template('writeup_template.html')
		output = template.render(content=content,  L2=True, title=category+" | "+name[i])
		
		# Create Page
		with open(html[i], 'w') as f:
			print(output, file=f)
		
		print("Created {} page!".format(html[i]))
		i += 1

# Function to convert rst files to html snippets using pandoc. 
# Then uses jinja to render them into proper html files.
# This is the passive one! Moving away from rst files to md files.
# Do not use this. Retaining this for future use.
def rst2html_conv(category, mfolder, folder, leftIndex, rightIndex):
	
	# Extract list of rst files in the given folder
	system("ls {0}/{1}/*.rst > {0}/{1}/{1}.txt".format(mfolder, folder))
	
	# Consolidate a list of rst files, html names, and article names
	rst = []
	name = []
	html = []
	
	# Open up the list of rst files
	with open("{0}/{1}/{1}.txt".format(mfolder, folder), 'r') as f:
		
		# Read all the lines.
		temp_lines = f.readlines()
		# print(temp_lines)
		
		# In each filename, remove the trailing "\n", and save it in rst
		# Remove rst extensiton and folder prefix and save the name
		# Create an HTML file name
		for tl in temp_lines:
			nl = tl.rstrip()
			nl_name = nl[leftIndex:rightIndex]
			nl_html = "fluidiccolours/"+folder+"/"+nl_name+".html"
			# print(nl)
			rst.append(nl)
			name.append(nl_name)
			html.append(nl_html)
	
	# Convert each rst files into a HTML file
	i = 0
	
	# Use pandoc to convert the rst file to HTML5 file and shove it in a temporary file.
	# Read the contents of the file in a variable.
	# Open the template file
	# Render the template to get the output
	# Push the output to the HTML filename created above
	for title in rst:
		print(title)
		system("pandoc --from rst --to html5 --mathjax {} > temp.html".format(title))
		with open("temp.html", "r") as p:
			content = p.read()
		# system("cp templates/blog_template.html templates/blog_template_temp.html")
		
		template = env.get_template('writeup_template.html')
		output = template.render(content=content, L2=True, title=category+" | "+name[i])
		
		# Create Page
		with open(html[i], 'w') as f:
			print(output, file=f)
		
		print("Created {} page!".format(html[i]))
		i += 1
