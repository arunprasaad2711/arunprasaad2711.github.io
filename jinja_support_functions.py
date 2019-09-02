# Import the required methods
from jinja2 import Environment, FileSystemLoader

# Import OS file for terminal operations
from os import system

# Beautiful Soup
from bs4 import BeautifulSoup

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
		## Not working! can't fully understand it. The previous error did not come, but something odd is happening.
		# system("pandoc --from markdown --to html5 --mathjax --highlight-style=haddock --css=assets/css/main.css {} > temp.html".format(title))

		# This is working well now thanks to the extracted codehilite.css files. Will work to full capacity when the css definition is full.
		# ABANDONED THE PANDOC HIGHLIGHT AS IT IS ONLY RUDIMENTARY! SWITCHING PERMANENTLY TO GOOGLE PRETTYTYPE!
		# system("pandoc --from markdown --to html5 --mathjax {} > temp.html".format(title))
		# same as above with the option to specify the highlight style. If activated, then the corresponding css should be included in main.scss.
		# system("pandoc --from=markdown --to=html5 --highlight-style=pygments --mathjax {} > temp.html".format(title))

		# This was the standard pandoc fix. Syntax highlight pushed permanently google pretty type.
		system("pandoc --from=markdown --to=html5 --no-highlight --mathjax {} > temp.html".format(title))

		# Read the data from the first temporary file.
		with open("temp.html", "r") as p:
			# change this to bcontent if using the FULL PANDOC PROTOCOL
			content = p.read()

		# convert the html contents into a bs object
		# soup = BeautifulSoup(bcontent, 'html.parser')

		# # # save only the body content elements into a new temp file
		# with open('temp2.html', 'w') as f:
		# 	for line in soup:
		# 		print(line, file=f)

		# with open("temp2.html", "r") as p:
		# 	content = p.read()

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
