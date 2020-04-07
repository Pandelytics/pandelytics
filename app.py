import requests
import bs4
import json
# from flask import Flask


# app = Flask(__name__)
# @app.route("/")


def twitterScrapper(hashtag):

    url = 'https://mobile.twitter.com/search?q='

    # remove the '#' from the query
    if '#' in hashtag :
        hashtag = hashtag.replace('#', '')

    
    #transferr the source from selenium to beautiful soup
    hashtag_search = requests.get(url + hashtag)
    hashtag_soup = bs4.BeautifulSoup(hashtag_search.text, features="lxml")

    usernames = hashtag_soup.select('div.username')
    tweetLinks = hashtag_soup.find_all("td", class_="timestamp")
    tweetTexts = hashtag_soup.select('div.dir-ltr')

    #create a list where the dictionary for each tweet is to be stored
    data = []

    #loop through the length of the list of names
    for i in range(len(usernames)):
        dictionary = {}

        dictionary['username'] = usernames[i].getText().replace('\n', '').replace(' ', '')
        dictionary['link_to_tweet'] = url + tweetLinks[i].a["href"]
        dictionary['tweet-text'] = tweetTexts[i].getText().replace('\n', '')

        #add dictionay to data list
        data.append(dictionary)

    #convert the list to json
    data_json = json.dumps(data)

    return (print(data_json))

twitterScrapper('#covid19')

# if __name__ == '__main__':
#     app.run(debug=True)
