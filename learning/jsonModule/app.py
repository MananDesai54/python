import json;

string = '{"name":"Manan","languages":["python","javaScript"]}';

json1 = json.loads(string);
print(json1);

with open('data.json') as f:
    a = json.load(f);
    print(a['name']);

dict1 = {
    "name" : "Manan",
    "coder" : True,
    "language" : ('js','py','c/c++'),
    "hobby" : ['coding','designing']
}

dict1S = json.dumps(dict1);
print(dict1S);

fp = open('data2.json','w');
json.dump(dict1,fp);

sortedKey = json.dumps(dict1,sort_keys=True);
print(sortedKey);