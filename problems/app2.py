list1 = [1,2,3,4,5,6,7,8,9,10];

list1.reverse();
print(list1);
print(list1[::-1]);

listlen = len(list1);

for i in range(int(listlen/2)):
    list1[i],list1[listlen-i-1] = list1[listlen-i-1],list1[i];

print(list1);