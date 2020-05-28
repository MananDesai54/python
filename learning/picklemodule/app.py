import pickle;

list1 = ['js','ts','py','c/c++'];

fpkl = open('my.pkl','wb');
pickle.dump(list1,fpkl);
fpkl.close();

fpkl = open('my.pkl','rb');
a = pickle.load(fpkl);
print(a);

fpkl.close();