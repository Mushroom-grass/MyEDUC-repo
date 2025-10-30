For windows: Git Bash is better

For MacOS: Git has been installed

# Terms:
- Directory: Folder
- Terminal or Command Line: Interface for Text Commands
- CLI: Command Line Interface
- cd: Change Directory
- Code Editor: Word Processor for Writing Code
- Repository: Project, or the folder/place where your project is kept
- Github: A website to host your repositories

# Git Commands:
- git clone
- git status: 
- git add: track your files and changes in Git
eg: git add .  (which means upload all changes)
eg: git add index.html  (upload one specific file)
- commit: save your files in Git
eg: git commit -m ‘message about change’ -m ‘some descriptions’
- git push -v: upload git commits to a remote repo, like GitHub
- pull/git fetch -v: download changes from remote repo to your local machine, the opposite of push

# Folder Commands
- la (mac) / ls -la: list everything including  hidden files and folders.


# ssh keys:
connect your local repo to your GitHub account.

- ssh-keygen -t rsa -b 4096 -c “email@address.com”(GitHub account): generate a ssh key

eg: ssh-keygen -t rsa -C “Yuanqi-hu@outlook.com”
//执行后一直回车即可

- ls | grep testkey(file name): list all ssh keys
- testkey.pub: you can share it with others
- testkey: your private key
- ssh -T git@github.com: test connection of ssh