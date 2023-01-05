`git init`: initialize current folder as a git repository
`git clone <URL>`: brings the git repo from <URL> to current folder
`git status`: tells us waht we need to know about our curreent repository
`git add <FILES>`: add <FILES> to the staging area
`git commit`: open a text editor to write commit message
`git commit -m`: "MESSAGE":write message as a commit wthout a text editor required

`git log`: shows the log (history) of our commits
`git log --oneline`: shows the shorter oneline commit 
`git diff`: compare current uncommited state with last known git state
`git diff --staged`: runs git diff between the stafging area and last known state
git diff HEAD~<NUMBER>`: compares HEAD with commit <Number> age (relateive)
git diff <HASH>`: compared HEAD with the commit in <HASH>

git restore --source <HASH OR HEAD~> <FILE>`: restore files to <HASH OR HEAD~>
git checkout <HASH OR HEAD~> <FILE>`: restore files to <HASH OR HEAD~>
git checkout <HASH OR HEAD~> if you forget the file, you end up in detach>
git checkout main`: go back to main
git switch main : go back to main commit 

warning: LF will be replaced by CRLF in README.md
the file will gave its original line endings in your working directory

`git remote add <NAME> <URL>`: adds the <URL> as a remote with the name <Name>
<NAME> is by convention called origin 
git remote rm <NAME>: to removes the remote called <NAME>
git remote -v: looks at all the remote you have
git push <WHERE> <WHAT>: pushes the <WHAT> branch to <WHERE>
- `git pull <WHERE> <WHAT>`: pulls the <WHAT> branch in <WHERE> to local computer
