from pandelytics.engines.base import Base


class News(Base):
    name = "Twitter"
    url = 'https://mobile.twitter.com/search?q='
    hash_tag = "#covid-19"

    def get_params(self):
        def get_hash_tags():
            if '#' in self.hash_tag:
                self.hash_tag = self.hash_tag.replace('#', '')
            return self.hash_tag

        params = {}
        params["q"] = get_hash_tags()
        return params

    def parse_soup(self, soup):
        tweets = soup.select('table.tweet')

        data = []

        for tweet in tweets:
            username = tweet.find('div', class_ ='username')
            tweet_link = tweet.find('td', class_='timestamp')
            tweet_text = tweet.find('div', class_='dir-ltr')

            # print(username, tweet_link, tweet_text)

            rdict = {}
            rdict['username'] = username.getText().replace(
                '\n', '').replace(' ', '')
            rdict['link_to_tweet'] = self.url + tweet_link.a["href"]
            rdict['tweet-text'] = tweet_text.getText().replace('\n', '')

            data.append(rdict)

        return data
