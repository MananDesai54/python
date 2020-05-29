# sentences = {
#     'Python is a awesome programming language , I like it but not more than js':0,
#     'JavaScript is the first language that attracted me to do awesome stuff so it is my love.It is also awesome but more closer to me than python':0,
#     'C is the language that none hate and i am not exception':0,
#     "Java is the language that attracted me but not for more time , i don't like it but not hate it.":0,
#     'C is first love , java is temporary love , javascript and python are lifetime love.':0,
#     'between javascript and python if choice for love i wiil say javascript is the love that child has for parents and python love for wife and childrens, so in short javscript i love the most':0,
#     "Don't compare languages just use and take benifit and of it.":0,
# }
import time;

sentences_dict = {};
sentences_list = [];

def search(search_words):
    for sentence in sentences_list:
        for word in search_words:
            if word.lower() in sentence.lower():
                sentences_dict[sentence]+=sentence.lower().split(' ').count(word.lower());
    return sentences_dict;

if __name__ == "__main__":
    import json;
    search_words = input('Enter words to search : ').split(' ');
    start = time.time();
    with open('data.json') as data:
        sentences_dict = json.load(data);
        for sentence in sentences_dict:
            sentences_list.append(sentence);
    search(search_words);

    result = [key for key,value in sorted(sentences_dict.items(),key=lambda item:item[1],reverse=True) if value>0];
    end = time.time();
    print(result);
    print(f'Total {len(result)} results : ({end-start})s');