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

    @classmethod
    def fromMix(cls,string):
        #cls.name = 'Manan' #change class variable 
        return cls(*string.split('-'));     #using as alternative to constructor

    @staticmethod
    def static():
        print('hello');

    def __str__(this):
        return f'{this.name} is from {this.country}'

    def __repr__(this):
        return f'Person("{this.name}","{this.country}")'

    def __add__(this):
        print('I am Operator overloading');

manan = Person('Manan','India');
manan.getDetails();
print(manan.email);
manan.email = 'manan.IN@shoppydude.com';
print(manan.email);
print(manan.country);
print(manan);
print(repr(manan));
print(str(manan));

mady = Person.fromMix('mady-IN');
print(mady);
print(mady.email);

Person.static();
manan.static();
mady.static();

del mady.email
print(mady.email);