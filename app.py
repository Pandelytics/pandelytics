import requests
import bs4
import json

def twitterScrapper(hashtag):

    url = 'https://mobile.twitter.com/search?q='

    if '#' in hashtag :
        hashtag = hashtag.replace('#', '')

    hashtag_search = requests.get(url + hashtag)
    hashtag_soup = bs4.BeautifulSoup(hashtag_search.text, features="lxml")

    usernames = hashtag_soup.select('div.username')
    tweetLinks = hashtag_soup.find_all("td", class_="timestamp")
    tweetTexts = hashtag_soup.select('div.dir-ltr')

    data = []

    for i in range(len(usernames)):
        dictionary = {}

        dictionary['username'] = usernames[i].getText().replace('\n', '').replace(' ', '')
        dictionary['link_to_tweet'] = url + tweetLinks[i].a["href"]
        dictionary['tweet-text'] = tweetTexts[i].getText().replace('\n', '')

        data.append(dictionary)

    data_json = json.dumps(data)

    return (data_json)

twitterScrapper('#covid19')