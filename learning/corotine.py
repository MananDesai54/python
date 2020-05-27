def corotine():
    book = 'I am Manan Desai';
    import time;
    time.sleep(4);

    while True:
        task = (yield);
        if task in book:
            print('found');
        else:
            print('Not');

search = corotine();
next(search);
search.send('I am');
input('press any key');
search.send('Manan');

search.close();