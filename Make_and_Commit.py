from jinja_support_functions import md2html_conv, file_loader, env
from os import system as sys
import MakeWebsite

commit_message = input("Enter the commit message:")
sys("git status")
sys("git add .")
sys("git status")
sys("git commit -m {}".format(commit_message))
sys("git push -u origin master")