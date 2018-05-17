#Using Regular Expressions to extract a simple phone number pattern.

import re

pattern = re.compile("\d{3}-\d{3}-\d{4}")
string = open("data/text3.txt").read()
matches = re.findall(pattern,string)
print(matches)

#Just a simple code, for illustration.
