# DeployWebsite.py - commits the file to github and the website.

from os import system as sys

commit_message = input("Enter the commit message:")
sys("git status")
sys("git add .")
sys("git status")
sys(f"git commit -m {commit_message}")
sys("git push -u origin master")
