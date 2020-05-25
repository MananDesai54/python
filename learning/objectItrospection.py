#object intro spection is knowing details about object
#like JS everyhing is object in py

class Person:
    public = 'I am Public';
    _protacted = 'I am Protected';
    __private = 'I am pivate';
    def __init__(this,name,country):
        this.name = name;
        this.country = country;

    def getDetails(this):
        print(f'{this.name} belong to {this.country}');

    @property #maiking property
    def email(this):
        return f'{this.name}.{this.country}@shoppydude.com';

    @email.setter #setter for property
    def email(this,string):
        mail = string.split('@')[0];
        this.name,this.country = mail.split('.');

    @email.deleter
    def email(this):
        this.name = None;
        this.country = None;

manan = Person('Manan','India');
print(manan.email);
print(type(manan));
print(id(manan));

o = 'MANAN';
print(dir(o));

import inspect;
print(inspect.getmembers(manan));

def inspectObject(obj):
    for i in inspect.getmembers(obj):
        if inspect.ismethod(i[1]):
            print(i[0]);
        elif inspect.isbuiltin(i[1]):
            print(i[0]);
inspectObject(manan);
