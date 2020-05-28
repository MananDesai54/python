import json;
import requests;
import time;
from colorama import Fore,Back,Style;

api_key = 'YOUR_API_KEY';

number_words = {
    1 : 'first',
    2 : 'second',
    3 : 'third',
    4 : 'forth',
    5 : 'fifth',
    6 : 'sixth',
    7 : 'seventh',
    8 : 'eight',
    9 : 'nineth',
    10: 'tenth'
}

def speech(str):
    from win32com.client import Dispatch;
    speak = Dispatch("SAPI.SpVoice");
    speak.Speak(str);

def getNews():
    news = requests.get(f'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={api_key}');
    return news;


if __name__ == "__main__":
    news_json = open('news.json','w');
    json.dump(getNews().json(),news_json);
    news_json.close();

    with open('news.json','r') as news:
        news_dict = json.load(news);
        news_list = news_dict['articles'];
        
        for news in news_list:
            print(Fore.WHITE , 'For more visit this url ' ,sep='',end=' ')
            print(Fore.GREEN , news["url"] , sep='');
            index = news_list.index(news)+1;
            speech(f'{number_words[index]} news');
            speech('Title')
            speech(news['title']);
            speech('Description')
            speech(news['description']);
            print(Fore.WHITE,'press any key for next news...',sep='');
            input();
