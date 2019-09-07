# cloning a github repo

C:\Users\bear>cd \code\

C:\code>git clone https://github.com/feed-me-seymour/silver-happiness
Cloning into 'silver-happiness'...
remote: Enumerating objects: 6, done.
remote: Counting objects: 100% (6/6), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 6 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (6/6), done.

C:\code>

# configuring git for just this repo (add --global before user.* to configure git globally)

C:\code\silver-happiness>git config user.email "bear@bear.com"

C:\code\silver-happiness>git config user.name "Bearbear@bear.com"


# looking at the changed files:

C:\code\silver-happiness>git status
On branch master
Your branch is up to date with 'origin/master'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        BEAR.md

nothing added to commit but untracked files present (use "git add" to track)

# adding a file to tracked files (so it will be added to the next commit)

C:\code\silver-happiness>git add BEAR.md

C:\code\silver-happiness>git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        new file:   BEAR.md

# committing all 'changes to be committed' into a new commit in the chain

C:\code\silver-happiness>git commit -m "chore: Adding BEAR.md, bear's readme for seymour"
[master addc486] chore: Adding BEAR.md, bear's readme for seymour
 1 file changed, 16 insertions(+)
 create mode 100644 BEAR.md

# pushing your changes to github

C:\code\silver-happiness>git push
remote: Permission to feed-me-seymour/silver-happiness.git denied to wrapsbear.
fatal: unable to access 'https://github.com/feed-me-seymour/silver-happiness/': The requested URL returned error: 403
