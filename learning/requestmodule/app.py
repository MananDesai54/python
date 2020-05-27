import requests;

r = requests.get('https://jsonplaceholder.typicode.com/todos/1');
print(r.text);
print(r.status_code)

r2 = requests.post(url='https://jsonplaceholder.typicode.com/posts',data='"{title: "foo",body: "bar",userId: 1}"');
print(r2);