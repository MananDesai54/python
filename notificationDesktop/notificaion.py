import time
from plyer import notification

if __name__ == "__main__":
    notification.notify(
        title='Think about changing the topic',
        message='Whatever topic you are learning think that how long today you have learnt it if sufficient then change to another topic',
        app_icon='think.ico',
        timeout=5,
    );