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
	system(f"ls -d ./{folder}/*/ > ./{folder}/dirs_l1.txt")

	with open(f"./{folder}/dirs_l1.txt", 'r') as f:
		l1_dirs = f.readlines()

	for lines in l1_dirs:
		l1_dir = lines.rstrip()[2:]
		print(l1_dir)
		system(f"ls ./{l1_dir}*.md > ./{l1_dir}dirs_l2.txt")

		with open(f"./{l1_dir}dirs_l2.txt", 'r') as mdfiles:
			md_file_list = mdfiles.readlines()

			for mdline in md_file_list:
				md = mdline.rstrip()[2:].replace(l1_dir, "")[:-3]
				# print(md)
				html = f'{md}.html'
				
				fname = f"./{l1_dir}{md}.md"
				temp_file = f"./{l1_dir}temp.html"
				output_file = f"./{l1_dir}{html}"
				title = f"{md} | {folder}"

				pandoc2html(title, fname, temp_file, output_file)

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