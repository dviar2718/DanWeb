1. Clone a Repo
First navigate to the directory where you want the repo to be located
```bash
$pwd
/Users/dlviar/win7/github
$git clone git://github.com/dviar2718/DanWeb.git
Cloning into 'DanWeb'...
remote: Counting objects: 161, done.
remote: Compressing objects: 100% (48/48), done.
remote: Total 161 (delta 22), reused 0 (delta 0)
Receiving objects: 100% (161/161), 24.65 KiB | 0 bytes/s, done.
Resolving deltas: 100% (62/62), done.
Checking connectivity... done
```
2. Add your project files or make changes.
```bash
$ls -ltr
total 0
drwxr-xr-x   9 dlviar  staff  306 Jul 29 21:38 test
drwxr-xr-x  13 dlviar  staff  442 Aug 31 14:53 DanWeb
$cd DanWeb/
$ls -ltr
total 32
drwxr-xr-x  4 dlviar  staff   136 Aug 31 14:53 stylesheets
-rw-r--r--  1 dlviar  staff  2017 Aug 31 14:53 params.json
drwxr-xr-x  3 dlviar  staff   102 Aug 31 14:53 javascripts
drwxr-xr-x  5 dlviar  staff   170 Aug 31 14:53 interests
-rw-r--r--  1 dlviar  staff   343 Aug 31 14:53 index.md
drwxr-xr-x  4 dlviar  staff   136 Aug 31 14:53 images
drwxr-xr-x  3 dlviar  staff   102 Aug 31 14:53 _layouts
drwxr-xr-x  4 dlviar  staff   136 Aug 31 14:53 _includes
-rw-r--r--  1 dlviar  staff    16 Aug 31 14:53 _config.yml
-rw-r--r--  1 dlviar  staff    10 Aug 31 14:53 README.md
$cd interests/
$ls -ltr
total 32
-rw-r--r--  1 dlviar  staff    91 Aug 31 14:53 test.md
-rw-r--r--  1 dlviar  staff  6906 Aug 31 14:53 links.md
-rw-r--r--  1 dlviar  staff   542 Aug 31 14:53 C_Programming.md
$mkdir python
$mkdir python
$cd python/
$touch pluralsight_python_fundamentals_notes.md
```
3. Use "git add ." to add all of your changes
```bash
$pwd
/Users/dlviar/win7/github/DanWeb/interests/python
$cd ..
$pwd
/Users/dlviar/win7/github/DanWeb/interests
$cd ..
$pwd
/Users/dlviar/win7/github/DanWeb
$git add . -n
add 'interests/GitHub_Notes.md'
add 'interests/python/pluralsight_python_fundamentals_notes.md'
$git add .
```
4. Use "git status" to see what needs to be commited
```bash
$git status
# On branch gh-pages
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#	new file:   interests/GitHub_Notes.md
#	new file:   interests/python/pluralsight_python_fundamentals_notes.md
#
```

5. Commit your changes with "git commit"
```bash

```