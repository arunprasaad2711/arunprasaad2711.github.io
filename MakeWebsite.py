from jinja2 import Environment, FileSystemLoader
from os import system as sys
from pathlib import Path
from WebsiteData import *

def pandoc2html(title, fname, temp_file, output_file):

	# Removing haskell. Including Pandoc-based syntax highlights.
	result = sys(f"pandoc --from=markdown --to=html5 --mathjax --highlight-style=pygments {fname} -o {temp_file}")

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

def recurFind(root, f):

    basePath = Path(f'{root}/{f}/')
    files_in_basepath = basePath.iterdir()
    print(f"Listing files in '{root}/{f}/")
    for item in files_in_basepath:
        if item.is_file():
            if item.name.endswith(".md"):
                title_words = str(item).split("/")
                # print(f"title words = {title_words}")
                title = title_words[-1][:-3]
                for Word in reversed(title_words[:-1]):
                    title += f' | {Word}'
                fname = str(item)
                html = fname[:-3]+'.html'
                temp_file = 'temp.html'
                # print(title, item, html)
                pandoc2html(title, fname, temp_file, html)
        else:
            newRoot = f'{root}'
            root_words = str(newRoot + "/" + str(item)).split('/')
            # Intentionally putting it to stop deep recursion.
            # The depth is: Main folder - ".", Group folder - "Fluidic Colours/Derivative/ ...", Sub-Group - "articles"
            if(len(root_words) <= ScanDepth):
                print(f"Recursion calling in '{newRoot}/{item}/")
                recurFind(newRoot, item)

# Recursive Scan-Depth
ScanDepth = 3

# Specify the template directory and environment 
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

for folder in Main_Folders:
    print(f"inside {folder}")
    recurFind(".", folder)

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

sys("rm ./temp.html")