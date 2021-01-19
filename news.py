import pyttsx3
import urllib.request
import json
import requests
import pandas as pd



url = "https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=4dbc17e007ab436fb66416009dfb59a8"
engine = pyttsx3.init()
result = requests.get(url)
content = result.content.decode()
world_map = pd.read_json(content)
print(world_map)
countryInfo_df = pd.json_normalize(world_map['articles'])
countries_all_data = pd.concat([countryInfo_df, world_map], axis=1, sort=False)
print(countries_all_data)
print(countryInfo_df)

for i in range(1,4):
        engine.say(countries_all_data['articles'][i])
        engine.runAndWait();

'''
data = urllib.request.urlopen(url).read().decode()


obj = json.loads(data)
print(obj)'''

'''
engine = pyttsx3.init()
c= urllib.request.urlopen('https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=4dbc17e007ab436fb66416009dfb59a8')
print(type(c))
json_string= c.read()
print("parsed_news",json_string)
parsed_news = json.loads(json_string)
print("parsed_news",parsed_news)
for i in range(1,4):
        print(parsed_news['NewsItem'][i]['HeadLine'])
        engine.say(parsed_news['NewsItem'][i]['HeadLine'])
        engine.runAndWait();'''

        
'''        
news=parsed_news['NewsItem'][1]['HeadLine']
news1=parsed_news['NewsItem'][0]['Caption']
news4=parsed_news['NewsItem'][3]['HeadLine']


engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',rate-40)
volume = engine.getProperty('volume')
engine.setProperty('volume',volume + 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)



print(news,news1,news4)
engine.say(news)
engine.runAndWait();
'''
