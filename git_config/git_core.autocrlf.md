https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration
https://stackoverflow.com/questions/1967370/git-replacing-lf-with-crlf
https://stackoverflow.com/questions/2517190/how-do-i-force-git-to-use-lf-instead-of-crlf-under-windows

Fix Line Endings - Force All Line Endings to LF and Not Windows Default CR or CRLF
Taken largely from: https://help.github.com/articles/dealing-with-line-endings/

```
#Set LF as your line ending default.
git config --global core.eol lf

#Set autocrlf to false to stop converting between windows style (CRLF) and Unix style (LF)
git config --global core.autocrlf false

#Save your current files in Git, so that none of your work is lost.
git add . -u
git commit -m "Saving files before refreshing line endings"

#Remove the index and force Git to rescan the working directory.
rm .git/index

#Rewrite the Git index to pick up all the new line endings.
git reset

#Show the rewritten, normalized files.
git status

#Add all your changed files back, and prepare them for a commit. This is your chance to inspect which files, if any, were unchanged.

git add -u
# It is perfectly safe to see a lot of messages here that read "warning: CRLF will be replaced by LF in file."

#Rewrite the .gitattributes file.
git add .gitattributes

#Commit the changes to your repository.
git commit -m "Normalize all the line endings"
```