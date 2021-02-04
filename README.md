# PasswordGenerator
A simple app to generate a random password using user input parameters.

2/2/2021
We have a working script, but there are a few things to do. 

~~ 1. Change the program so that when we answer one of the prompts yes, it requires at least one of that kind of char~~

2. Make an API that can be accessed from anywhere so that someone could use this script in a larger app.

Not bad for a few hours tho!

2/4/2021
refactored the generation into a password object. now call the password with th number of characters and 4 bools for numbers, UPPER, lower, and symbols, and youll get out a password. 

Also added a method to check whether each type of symbol was represented. It works, but it's fairly verbose, and I wonder if there is a better way.