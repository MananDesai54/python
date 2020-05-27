import os;

words = [];
path = os.getcwd()+'\change';
print(path);


def beautifyfolder(path,file,exetnsion):
    with open(file) as f:
        words = f.read().split('\n');
        os.chdir(path);
        files = os.listdir();
        extFiles = 0;
        for file in files:
            name = file.split('.')[0];
            exetnsion_ = file.split('.')[1];
            if exetnsion_ == exetnsion:
                extFiles+=1;
                os.rename(file,f'{extFiles}.{exetnsion_}');
            else:
                if name not in words:
                    os.rename(file,f'{name.capitalize()}.{exetnsion_}');

beautifyfolder(path,'dict.txt','jpg');