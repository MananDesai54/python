# iterable => __iter__() || __getitem()
# iterator => __next__()
# iteration

list1 = [1,2,3];
a = list1.__iter__();
print(a.__next__());

#generator => one type of iterator which can be travere only once... they generate value at the time of iterate like range function is generator
for i in range(10):
    print(i);

#here 0 to 9 is not created they are generated while itearting 10 times in for loop....

#creating generator
def gen(n):
    for i in range(n):
        yield i; #yeild will generate value on the fly , so it's a generator....

g = gen(10);
print(g);
#generator are useful for storing ram ... so without storing value we generate on the go.. so whenever needed we use it...

def genFacto(n):
    for i in range(n):
        yield facto(i);

def facto(n):
    if n<=1:
        return 1;
    else:
        return n*facto(n-1);

factogen = genFacto(10);
for i in factogen:
    print(i);