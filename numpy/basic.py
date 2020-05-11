import sys
import numpy as np

#creating & editing 1-d array with numpy
a = np.array([1,2,3,4]);

print(a[1]);    #access item

b = a[1:3];     #slicing
print(b);
b = a[-2:-1];
print(b);
b = a[-1::-1];
print(b);

print(a[1],a[2]); #multi indexing to acces more than one element
print(a[[1,2]]);

#if we mix type in array then it will convert them and make one type bcaz it's important in numpy to have same kind of data
    #so mix of int/float+str = str
    # int+float = float
    # int/float+bool = int/float
    # str+bool = str
    # don't do this if not requied bcaz mostly we use numpy for int/float means numeric data
    # as numpy stores all items contineous in memory numpy need a specific type in array to have better performance , you should not mix all the types in numpy array
        # numpy store and allocate memory as per type so we don't mix the types....
        # numpy can't provide consistency for mixed types...
c = np.array([1,2,'a'])
print(c);

#types of passed arrays
a = np.array([1,2,3]);
print(a.dtype)  #as all data is int it provide memory according it like init32,int64 as per machine
a = np.array([1.1,1.2,1.3]);
print(a.dtype);     #as all data is int it provide memory according it like init32,int64 as per machine
a = np.array([1,2,3] , dtype=np.int16);     #specify datatype of numpy array
print(a.dtype);

#you can use numpy to store str , obj but mostly it is use to store numbers , booleans , dates etc...

#creating & editing 2-d array with numpy
a = np.array([
    [1,2,3],
    [4,5,4],
]);
print(a.shape);
print(a.size);
print(a.ndim);


#creating & editing 3-d array with numpy
a = np.array([
    [
        [1,2,3],
        [4,5,6],
    ],
    [
        [7,8,9],
        [7,4,1],
    ]
]);
print(a.shape);
print(a.size);
print(a.ndim);

# take care while creating multi-d array you have to maintain the structure otherwise it won't work as you need
#i.e : a = np.array([
#   [
#       [1,2,3],
#       [4,5,6]        
#   ],
#   [
#       [1,2,3]
#   ]
# ]) => this will not work as 3-d array so maintain structure for all the array

#index and slice multi-d array or matrix
a = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
]);
print(a[0],a[1][2]);
print(a[1,2]); #simple way of indexing

print(a[:,:2]);  #slicing
print(a[:2,:2]);

a[1] = np.array([10,12,16]);    #assign any array to sub array of numPy array
print(a);
a[2] = 45;  #assign some fixed value for perticular row
print(a);


#statasic methods of numpy array
a = np.array([1,2,3,4]);
print(a.sum());     #sum
print(a.mean());    #mean of all elements
print(a.std());     #standard deviation
print(a.var());     #variance


#statasic methods of numpy matrix
a = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
]);
print(a.sum());     #sum
print(a.mean());    #mean of all elements
print(a.std());     #standard deviation
print(a.var());     #variance
# or we can do row or column vise axis=>0=>column & axis=>1=>row for 2-d increase it as per dimension increases...
print(a.sum(axis=0)); #column-vise
print(a.mean(axis=1)); #row vise
print(a.std(axis=1)); #row vise
print(a.var(axis=1));  #row vise

#3-d array
a = np.array([
    [
        [1,2,3],
        [4,5,6],
    ],
    [
        [7,8,9],
        [7,4,1],
    ]
]);
print(a.sum());
print(a.sum(axis=0)); #z-axis
print(a.sum(axis=1)); #y-axis
print(a.sum(axis=2)); #x-axis


#broadcasting and vectorised arrays => this is mostly related to boolean arrays
    #one of the fundamental of numPy
    #vectorised operations are operations performed between array-array , array-vector and they are extremily fast

a = np.arange(4);
print(a);
print(a+10);    #all the elements will be applied this operations....
print(a*10);
a += 10;    #this is array & scaller
print(a);

#we can do it with array-array
b = np.array([10,10,10,10]);
print(a+b); #sum index-index wise


#boolean arrays.... just so much important
a = np.arange(4);
print(a[0],a[3]);
print(a[[0,3]])
print(a[[True,False,False,True]]); #for selecting elements

print(a>=2);    #return boolen array True where >=2 else False
print(a[a>=2]); #passed boolean indexes....

#also do some operations with it
print(a[a > a.mean()]);
print(a[~(a > a.mean())]);
print(a[(a==1) | (a==3)]);
print(a[(a>=2) & (a%2==0)]);
print(a.sum());

#also same usage for matrix
a = np.random.randint(100 , size=(3,3));
print(a);
print(a>30);
print(a[a>30]);
print(a[a > a.mean()]);
print(a[~(a > a.mean())]);
print(a[(a==1) | (a==3)]);
print(a[(a>=2) & (a%2==0)]);


#linear algebra
a = np.random.randint(100 , size=(3,3));
b = np.random.randint(100 , size=(3,3));

print(a.dot(b));
print(a@b); #cross product
print(b.T); #transpose
print(b.T @ a);


#some numPy functions
print('---------------');
#random
print(np.random.normal(size=2));
print(np.random.random(size=2));
print(np.random.rand(2,4));
print(np.random.randint(50,size=(3,3)));
print(np.random.choice(np.arange(5)));

print('---------------');
#arrange
print(np.arange(10)); 
print(np.arange(5,10));
print(np.arange(0,1,0.1));\

#reshape
print(np.arange(10).reshape(2,5));

#linspace give start , stop and parts it will crate array of num of parts from start to end
print(np.linspace(1,5,5));
print(np.linspace(2,2,20));
print(np.linspace(0,1,20,False)); #false will not count end point by default if you dopn't provide it's true

#zeros,ones,enpty
print(np.zeros(5));
print(np.zeros((3,3)));
print(np.ones(5));
print(np.ones((3,3),dtype=np.int));
print(np.empty(5));
print(np.empty((3,3)));


#identity , eye to make identity matix
print(np.identity(3));
print(np.eye(3,3));
print(np.eye(3,3,k=1));
print(np.eye(8,4,k=-3));

#
print("Hello Manan"[6]);

#ones_like  => make array with same shape of passed array but with 1's in it
a = np.arange(4);
print(np.ones_like(a));

#zeros_like  => make array with same shape of passed array but with 0's in it
a = np.arange(4);
print(np.zeros_like(a));

#copy => copy numPy array by reference not saperate created
#all => return true if all elements are non zero
#any => return true if there is any zero available in numPy array
#max => give max value from numPy array