from pygame import mixer;
from datetime import datetime;
from time import time;

def musicOnLoop(file,stopper):
    while True:
        mixer.init();
        mixer.music.load(file);
        mixer.music.play();
        a = input();
        if a == stopper:
            mixer.music.stop();
            break;

def logInFile(data):
    with open('log.txt','a') as f:
        f.write(f'{data} at {datetime.now()}\n');

if __name__ == "__main__":
    log_w = time();
    log_e = time();
    log_ex = time();
    water_ = 5;
    eye_ = 10;
    exercise_ = 15;

    while True:
        if time()-log_w > water_:
            print('please drink water, to stop music press "w"');
            musicOnLoop('water.mp3','w');
            log_w = time();
            logInFile('Drank Water');

        if time()-log_e > eye_:
            print('please rest your eyes, to stop music press "e"');
            musicOnLoop('eye.mp3','e');
            log_e = time();
            logInFile('Rested eyes');

        if time()-log_ex > exercise_:
            print('please do exercise, to stop music press "ex"');
            musicOnLoop('physical.mp3','ex');
            log_ex = time();
            logInFile('Done Exercise');