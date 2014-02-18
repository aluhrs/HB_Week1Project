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
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for letter in alphabet:
	os.mkdir(letter)
# loop through the files and only check the first letter
# put each file in the corresponding letter directory


path = "/Users/ashleyluhrs/Documents/Hackbright/Week1Project/files"
dirs = os.listdir(path)
# will i need to go through each letter of the alphabet?
for files in dirs:
	if files[0] == "a": 	
		shutil.move(path + "/" + files, "/Users/ashleyluhrs/Documents/Hackbright/Week1Project/a/")
	elif files[0] == "b": 	
		shutil.move(path + "/" + files, "/Users/ashleyluhrs/Documents/Hackbright/Week1Project/b/")
	elif files[0] == "c": 	
		shutil.move(path + "/" + files, "/Users/ashleyluhrs/Documents/Hackbright/Week1Project/c/")
	elif files[0] == "d": 	
		shutil.move(path + "/" + files, "/Users/ashleyluhrs/Documents/Hackbright/Week1Project/d/")
	elif files[0] == "e": 	
		shutil.move(path + "/" + files, "/Users/ashleyluhrs/Documents/Hackbright/Week1Project/e/")
	elif files[0] == "f": 	
		shutil.move(path + "/" + files, "/Users/ashleyluhrs/Documents/Hackbright/Week1Project/f/")
	elif files[0] == "g": 	
		shutil.move(path + "/" + files, "/Users/ashleyluhrs/Documents/Hackbright/Week1Project/g/")
	elif files[0] == "h": 	
		shutil.move(path + "/" + files, "/Users/ashleyluhrs/Documents/Hackbright/Week1Project/h/")
	elif files[0] == "i": 	
		shutil.move(path + "/" + files, "/Users/ashleyluhrs/Documents/Hackbright/Week1Project/i/")
	elif files[0] == "j": 	
		shutil.move(path + "/" + files, "/Users/ashleyluhrs/Documents/Hackbright/Week1Project/j/")
	elif files[0] == "k": 	
		shutil.move(path + "/" + files, "/Users/ashleyluhrs/Documents/Hackbright/Week1Project/k/")
	elif files[0] == "l": 	
		shutil.move(path + "/" + files, "/Users/ashleyluhrs/Documents/Hackbright/Week1Project/l/")
	elif files[0] == "m": 	
		shutil.move(path + "/" + files, "/Users/ashleyluhrs/Documents/Hackbright/Week1Project/m/")
	elif files[0] == "n": 	
		shutil.move(path + "/" + files, "/Users/ashleyluhrs/Documents/Hackbright/Week1Project/n/")
	elif files[0] == "o": 	
		shutil.move(path + "/" + files, "/Users/ashleyluhrs/Documents/Hackbright/Week1Project/o/")
	elif files[0] == "p": 	
		shutil.move(path + "/" + files, "/Users/ashleyluhrs/Documents/Hackbright/Week1Project/p/")
	elif files[0] == "q": 	
		shutil.move(path + "/" + files, "/Users/ashleyluhrs/Documents/Hackbright/Week1Project/q/")
	elif files[0] == "r": 	
		shutil.move(path + "/" + files, "/Users/ashleyluhrs/Documents/Hackbright/Week1Project/r/")
	elif files[0] == "s": 	
		shutil.move(path + "/" + files, "/Users/ashleyluhrs/Documents/Hackbright/Week1Project/s/")
	elif files[0] == "t": 	
		shutil.move(path + "/" + files, "/Users/ashleyluhrs/Documents/Hackbright/Week1Project/t/")
	elif files[0] == "u": 	
		shutil.move(path + "/" + files, "/Users/ashleyluhrs/Documents/Hackbright/Week1Project/u/")
	elif files[0] == "v": 	
		shutil.move(path + "/" + files, "/Users/ashleyluhrs/Documents/Hackbright/Week1Project/v/")
	elif files[0] == "w": 	
		shutil.move(path + "/" + files, "/Users/ashleyluhrs/Documents/Hackbright/Week1Project/w/")
	elif files[0] == "x": 	
		shutil.move(path + "/" + files, "/Users/ashleyluhrs/Documents/Hackbright/Week1Project/x/")
	elif files[0] == "y": 	
		shutil.move(path + "/" + files, "/Users/ashleyluhrs/Documents/Hackbright/Week1Project/y/")
	elif files[0] == "z": 	
		shutil.move(path + "/" + files, "/Users/ashleyluhrs/Documents/Hackbright/Week1Project/z/")
	




