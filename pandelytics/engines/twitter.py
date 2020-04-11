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
        usernames = soup.select('div.username')
        tweet_links = soup.find_all("td", class_="timestamp")
        tweet_texts = soup.select('div.dir-ltr')

        data = []

        print(usernames, tweet_links, tweet_texts)
        for i in range(len(usernames)):
            rdict = {}
            rdict['username'] = usernames[i].getText().replace(
                '\n', '').replace(' ', '')
            rdict['link_to_tweet'] = self.url + tweet_links[i].a["href"]
            rdict['tweet-text'] = tweet_texts[i].getText().replace('\n', '')

            data.append(rdict)

        return data
