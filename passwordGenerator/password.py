import string;
import random;

if __name__ == "__main__":
    
    s1 = string.ascii_lowercase;
    s2 = string.ascii_uppercase;
    s3 = string.digits;
    s4 = string.punctuation;

    allChar = [];
    allChar.extend(list(s1));
    allChar.extend(list(s2));
    allChar.extend(list(s3));
    allChar.extend(list(s4));
    random.shuffle(allChar);

    passWordLength = input('Enter Length of password : ');
    if passWordLength.isdigit():
        passWordLength = int(passWordLength);
        password = '';

        # for i in range(passWordLength):
        #     password += allChar[random.randint(0,len(allChar)-1)];

        password = ''.join(allChar[0:passWordLength]);
        print(password);

        password = ''.join(random.sample(allChar,passWordLength));
        print(password);
    else : 
        print('Please Enter a valid number');