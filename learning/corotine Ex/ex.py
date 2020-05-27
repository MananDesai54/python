languages = ['javascript','python','java','kotlin','html5','scss','c','c++','rust','wasm','elm','c#','typescript','scala','haskell']

files = [];

def search():
    for i in range(15):
        files.append(open(f'{i}.txt').read());

    while(True):
        word = (yield);
        for language in files:
            if word in language:
                print('found');
                break;
        else:
            print('not found'); 

searchLang = search();
next(searchLang);
searchLang.send('javascript');
input('Press any key');
searchLang.send('python');

searchLang.close();