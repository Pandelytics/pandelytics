import requests
import bs4
import json
import time
from flask import Flask
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--window-size=1920x1080")

app = Flask(__name__)
@app.route("/")



url = 'https://mobile.twitter.com/hashtag/'

def twitterScrapper(hashtag):
    # remove the '#' from the query
    if '#' in hashtag :
        hashtag = hashtag.replace('#', '')

    #get the browser using selenium webdriver
    browser = webdriver.Chrome('C:/Users/ladankhadija/SLKhadeeja/pandelytics/chromedriver.exe')
    browser.get(url + hashtag)
    
    # #scroll the pages 5 times (in this case there are 20 pages per execute).... wait 5 seconds between executing script
    for i in range(5):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

    # source = browser.page_source

    #transferr the source from selenium to beautiful soup
    hashtag_search = requests.get(browser.current_url)
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

    return (data_json)

twitterScrapper('#covid19')

# if __name__ == '__main__':
#     app.run(debug=True)
