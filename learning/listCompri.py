#list compri..
list1 = [i for i in range(100) if i%2==0];
print(list1);

#dict compri..
dict1 = {i:f'item{i}' for i in range(100) if i%2!=0};
print(dict1);
#reverse key value
dict2 = {value:key for key,value in dict1.items()};
print(dict2);

#set compri..
set1 = {a for a in[1,2,1,2,1,3,4,5]};
print(set1);

#generator compri...
gen = (i for i in range(10));
print(gen);
print(gen.__next__());