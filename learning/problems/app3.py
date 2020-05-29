def nextPelindrome(number):
    tempnum = number;
    while str(tempnum)!=str(tempnum)[::-1]:
        tempnum+=1;
    return tempnum;

if __name__ == "__main__":
    list1 = [];

    for i in range(int(input('Enter number of testcases: '))):
        list1.append(int(input()));

    for number in list1:
        print(f'Next pelindrome for {number} is {nextPelindrome(number)}');
