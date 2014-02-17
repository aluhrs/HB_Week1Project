"""Project 1: Looping, file manipulation, panic
=======

Introduction
-------
This exercise is difficult and should take several days. 

Resources:
    * http://learnpythonthehardway.org/book/ex32.html
    * http://learnpythonthehardway.org/book/ex34.html
    * http://www.learnpython.org/Lists
    * http://www.learnpython.org/Loops
    * http://www.learnpython.org/Basic_String_Operations
    * http://docs.python.org/library/os.html#os.listdir
    * http://docs.python.org/library/os.html#os.chdir
    * http://docs.python.org/library/os.path.html#os.path.exists
    * http://docs.python.org/library/shutil.html#shutil.move

Concepts required:
    * for loops
    * conditionals
    * lists
    * paths
    * substrings

Description
-------
Included in the exercise is a zipfile, 'files.zip'. 
It contains 200 files with random character strings for names, 
all lowercase. First, unzip this file into a directory named 'original_files'.

Your job is to write a program, ex1.py, that does the following things:

1. Create 26 directories in the current directory, one for each letter of the alphabet:
    ./a/
    ./b/
    ./c/
    etc.

2. Loop through all the files in the original_files directory, 
and organize each of those files into the directory that their name starts with.

### Example:
    The file named 'artichoke.txt' would go into the directory 'a',
    'bartholomew.txt' would go into 'b'.


os.listdir(path)
Return a list containing the names of the entries in the directory given by path. 
The list is in arbitrary order. It does not include the special entries '.' and '..' 
even if they are present in the directory.

os.chdir(path)
Change the current working directory to path.

os.path.exists(path)
Return True if path refers to an existing path. Returns False for broken symbolic links.
 On some platforms, this function may return False if permission is not granted to 
execute os.stat() on the requested file, even if the path physically exists.

shutil.move(src, dst)
Recursively move a file or directory (src) to another location (dst).

If the destination is a directory or a symlink to a directory, then src is 
moved inside that directory. The destination directory must not already exist. 
If the destination already exists but is not a directory, it may be overwritten 
depending on os.rename() semantics.

If the destination is on the current filesystem, then os.rename() is used. 
Otherwise, src is copied (using shutil.copy2()) to dst and then removed.

"""
import os
import shutil
# import re
# ???? woud like to use regex for the alphabet but unsure how to implement regex

#ideas:
# loop through the directory to make a dictionary for each letter of the alphabet
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "y", "z"]

# for letter in alphabet:
	#os.mkdir(letter)
# loop through the files and only check the first letter
# put each file in the corresponding letter directory


path = "/Users/ashleyluhrs/Documents/Hackbright/Week1Project/files"
dirs = os.listdir(path)
# will i need to go through each letter of the alphabet?
for files in dirs: 
	shutil.move(path, )




