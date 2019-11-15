from jinja2 import Environment, FileSystemLoader
from os import system
from WebsiteData import *

def pandoc2html(title, fname, temp_file, output_file):

	# Use this when using haskell to create a custom pygments parser
	result = system(f"pandoc -F pygments --from=markdown --to=html5 --mathjax {fname} -o {temp_file}")

	## DO NOT USE THE ONES BELOW - SASS file modified a lot to get the haskell executable to work.
	# Use this for a simple syntax highlight
	# system(f"pandoc --from=markdown --to=html5 --highlight-style=pygments --mathjax {fname} -o {temp_file}")
	# This was the standard pandoc fix. Syntax highlight pushed permanently google pretty type.
	# system(f"pandoc --from=markdown --to=html5 --no-highlight --mathjax {fname} -o {temp_file}")

	if result != 0:
		print(f"Error occurred file converting {fname}")
	else:	
		with open(temp_file, "r") as p:
		
			data = {
				'content': p.read(),
				'title': title,
				'L0':False,
				'L1':False,
				'L2':True,
				}

			template = env.get_template('main_pages/blogpost_template.html')
			output = template.render(post=data)

			with open(output_file, 'w') as f2:
				print(output, file=f2)

			print(f'Finished rendering {output_file}')


# Specify the template directory and environment 
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

for folder in Main_Folders:
	# system(f"ls -d ./{folder}/*/ > ./{folder}/dirs_l1.txt")
	system(f'find ./{folder} -name "*.md" -type f > ./{folder}/mdfiles.txt')

	with open(f"./{folder}/mdfiles.txt", 'r') as f:
		mdlines = f.readlines()
	
	for mdline in mdlines:
		md = mdline.rstrip()
		html = f'{md[:-3]}.html'
		temp_file = 'temp.html'
		title = md[2:-3].replace(f"{folder}/", "")
		print(title)
		# print(html)
		pandoc2html(title, md, temp_file, html)

i = 0
for page in main_pages:
	
	data = {
		'title' : titles[i],
		'Banner' : Banners[i],
		'BannerMessage' : BannerMessages[i],
		'BannerImage' : BannerImages[i]
	}

	# Templating Page
	template = env.get_template('main_pages/'+page)
	output = template.render(post=data)
	
	# Create Page
	with open(page, 'w') as f:
		print(output, file=f)
	
	print(f"Created {page} page!")
	i += 1