import re;

mystr = open('mystr.txt').read();

sequence = re.compile(r'[0-9a-zA-Z._]+@[0-9a-zA-Z]+.+[0-9a-zA-Z]+');

matches = sequence.findall(mystr);

print(matches);