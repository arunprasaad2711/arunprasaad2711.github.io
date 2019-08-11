# Import md2html function from support function
from jinja_support_functions import md2html_conv, file_loader, env
from os import system as sys

main_pages = ['index.html',
              'faq.html',
              'maths.html',
              'science.html',
              'blogs.html',
              'apps.html',
              'syntax.html'
              ]
titles = ['Home', 'FAQs', 'Maths', 'Science', 'Blogs', 'Apps', 'Code']
Banners = [
	"Hi, my name is Arun!",
	"Hey there, Seeker!",
	"Hey there, Maths Enthusiast!",
	"Hey there, Science Enthusiast!",
	"Hey there, Reader!",
	"Hey there, Curious Mind!",
	"Hey there, Tech Savvy!"
]
BannerMessages = [
	"Welcome to my website! You can read my blog posts, poems, articles, notes, from here.",
	"You can get to know the answers to some of the common questions here!",
	"You can refer to my mathematics subject notes here!",
	"You can read my notes on science topics and subjects here!",
	"You can read my blog posts, poems, short stories, and other writings here!",
	"This is a collection of apps and recommendations I've curated! You're welcome :P",
	"You can read my programming notes, software tips, linux notes and other writings here!"
]

BannerImages = [
	"images/banner_01.jpg",
	"images/special_picture.jpg",
	"images/banner_01.jpg",
	"images/science.jpg",
	"images/blog.png",
	"images/banner_01.jpg",
	"images/syntax.png",
]

# Write down the list of folders, 
# the number of characters to skip from left and right.

# Coding
md2html_conv("Python and Web Programming", "syntax", "code", "Jinja2", 12, -3)
md2html_conv("Python and Web Programming", "syntax", "code", "Bokeh", 11, -3)
md2html_conv("Python and Web Programming", "syntax", "code", "Plotly", 12, -3)
md2html_conv("C Programming", "syntax", "code", "C", 7, -3)
md2html_conv("Geogebra Programming", "syntax", "code", "Geogebra", 14, -3)
md2html_conv("Python Programming", "syntax", "code", "Scientific_Computation_Using_Python", 41, -3)
md2html_conv("Fortran Programming", "syntax", "code", "Fortran", 13, -3)
md2html_conv("CPP Programming", "syntax", "code", "CPP", 9, -3)
md2html_conv("Java Programming", "syntax", "code", "Java", 10, -3)
md2html_conv("LaTeX Programming", "syntax", "code", "LaTeX", 11, -3)
md2html_conv("Parallel Programming", "syntax", "code", "MPI", 9, -3)
md2html_conv("Shell Programming", "syntax", "code", "Shell", 11, -3)
md2html_conv("Python Programming", "syntax", "code", "Python", 12, -3)
md2html_conv("Web Development", "syntax", "code", "CSS3", 10, -3)
md2html_conv("Web Development", "syntax", "code", "HTML5", 11, -3)
md2html_conv("Web Development", "syntax", "code", "JavaScript", 16, -3)
md2html_conv("Web Development", "syntax", "code", "ProcessingJS", 18, -3)
md2html_conv("Web Development", "syntax", "code", "HTML5_CSS3", 16, -3)
md2html_conv("Web Development", "syntax", "code", "Jekyll", 12, -3)
md2html_conv("Web Development", "syntax", "code", "Sass", 10, -3)

# Blogs
md2html_conv("Poems", "fluidiccolours", "blog", "poems", 11, -3)
md2html_conv("Stories", "fluidiccolours", "blog", "short_stories", 19, -3)
md2html_conv("Writings","fluidiccolours", "blog", "articles", 14, -3)

i = 0
for page in main_pages:
	
	# Templating Page
	template = env.get_template('main_pages/'+page)
	output = template.render(title=titles[i], Banner=Banners[i], BannerMessage=BannerMessages[i], BannerImages=BannerImages[i])
	
	# Create Page
	with open(page, 'w') as f:
		print(output, file=f)
	
	print("Created {} page!".format(page))
	i += 1

# # Updating the git repository and loading the files to github pages
# commit = input("Should Commit? Y/N: ")

# if(commit == "Y" or commit == 'y'):
# 	commit_message = input("Enter the commit message:")
# 	sys("git status")
# 	sys("git add .")
# 	sys("git status")
# 	sys("git commit -m {}".format(commit_message))
# 	sys("git push -u origin master")
