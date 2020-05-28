import re;

#finditer , findall , search , sub , split

mystr = open('mystr.txt').read();
# print(mystr);

# pattern = re.compile(r'harry');
# pattern = re.compile(r'.adm');
# pattern = re.compile(r'^Tata');
# pattern = re.compile(r'iin$');
# pattern = re.compile(r'ai*');
# pattern = re.compile(r'ai+');
# pattern = re.compile(r'ai{2}');
# pattern = re.compile(r'(ai){2}');
# pattern = re.compile(r'(ai){1}|Fax');

#special sequence
# pattern = re.compile(r'th\b');
# pattern = re.compile(r'\bth');
# pattern = re.compile(r'\ATata');

#special search
# pattern = re.compile(r'\d{5}-\d{4}');

pattern = re.compile(r'[+][0-9]{2} [0-9]{10}');
matches = pattern.finditer(mystr);
# print(matches);
# matches = pattern.findall(mystr);
# print(matches);
# matches = pattern.search(mystr);
# print(matches);
# matches = pattern.split(mystr);
# print(matches);
# matches = pattern.sub(mystr,'914');
# print(matches);

for match in matches:
    print(match.group());